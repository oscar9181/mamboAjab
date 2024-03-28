from django import forms
from django.forms import ModelForm
from .models import Rentals
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class RentalsForm(ModelForm):
    
    class Meta:
        model = Rentals
        fields = ("image","location","house_type","bedrooms","house_price")
        widgets=(
            
        )



        