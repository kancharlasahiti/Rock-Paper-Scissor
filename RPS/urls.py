from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.RPS_home,name='RPS_home')
]
