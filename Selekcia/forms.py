from django import forms
from .models import Produkt

class produktForm(forms.ModelForm):
  class Meta:
    model = Produkt
    fields = ('nazov', 'shoplinka', 'obrlinka', 'cena', 'mena')
    
  