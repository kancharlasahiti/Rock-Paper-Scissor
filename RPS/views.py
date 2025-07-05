import random
from django.shortcuts import render
from .forms import RPSForm

def RPS_home(request):
    if request.method == 'POST':
        form = RPSForm(request.POST)
        if form.is_valid():
            user_choice = form.cleaned_data['choice']
            computer_choice = random.choice(['rock', 'paper', 'scissors'])

            if user_choice == computer_choice:
                result = "It's a Tie!"
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                 (user_choice == 'paper' and computer_choice == 'rock') or \
                 (user_choice == 'scissors' and computer_choice == 'paper'):
                result = "You Win!"
            else:
                result = "Computer Wins!"

            return render(request, 'result.html', {
                'result': result,
                'user_choice': user_choice,
                'computer_choice': computer_choice
            })
    else:
        form = RPSForm()

    return render(request, 'game.html', {'form': form})
