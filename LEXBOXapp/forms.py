from django import forms 
from .models import CarteIdentitate


class CarteIdentitateForm(forms.ModelForm): 
  
    class Meta: 
        model = CarteIdentitate 
        fields = ['name', 'carte_identitate_img']