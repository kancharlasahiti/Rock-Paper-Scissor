from django import forms

class RPSForm(forms.Form):
    CHOICES = [
        ('rock', 'Rock'),
        ('paper', 'Paper'),
        ('scissors', 'Scissors')
    ]
    choice = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
