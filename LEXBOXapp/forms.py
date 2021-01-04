from django import forms 
from .models import CarteIdentitate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CarteIdentitateForm(forms.ModelForm): 
  
    class Meta: 
        model = CarteIdentitate 
        fields = ['name', 'carte_identitate_img']


class SignUpForm(UserCreationForm):
    firstName = forms.CharField(max_length=30, required=True)
    lastName = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=50, required=True)
    cnp = forms.CharField(max_length=15, required=True,help_text="Codul numeric personal")
    ciSeries = forms.CharField(max_length=12, required=True,help_text="Seria de pe buletin")
    ciNumber = forms.CharField(max_length=12,required=True, help_text="Numar buletin")
    city = forms.CharField(max_length=25, required=True, help_text="Orasul de provenienta")
    street = forms.CharField(max_length=30,required=True, help_text="Strada unde locuiti")
    number = forms.CharField(max_length=10,required=False,help_text="Numarul de locuinta")
    stair = forms.CharField(max_length=10, required=False, help_text="Etajul unde locuiti")
    block = forms.CharField(max_length=10, required=False, help_text="Numarul blocului")
    apartment = forms.CharField(max_length=10, required=False, help_text="Numarul apartamentuli unde locuiti")
    county = forms.CharField(max_length=20, required=True, help_text="Judetul de provenienta")



    class Meta:
        model = User
        fields = ('firstName','lastName','email','cnp','ciSeries','ciNumber','city','street','number','stair','block','apartment','county','password1','password2',)





