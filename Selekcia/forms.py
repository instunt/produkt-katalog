from django import forms
from .models import Produkt, Ceny

class produktForm(forms.ModelForm):
  class Meta:
    model = Produkt
    fields = ('nazov', 'shoplinka', 'obrlinka', 'cena', 'mena')

class cenyForm(forms.ModelForm):
  class Meta:
    model = Ceny
    fields = ('nazov', 'vyrobca', 'cena', 'mena', 'datum', 'miesto')
    
  