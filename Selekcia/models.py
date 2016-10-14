from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Produkt(models.Model):
  nazov = models.CharField(max_length=100)
  shoplinka = models.CharField(max_length=600, default="n/a")
  obrlinka = models.CharField(max_length=600, default="n/a")
  created_date = models.DateTimeField(default=timezone.now)
  cena = models.FloatField(default=0)  
  mena = models.CharField(max_length=3, default="EUR")
  
  def __unicode__(self):
    return self.nazov
    
class Ceny(models.Model):
  nazov = models.CharField(max_length=100)
  vyrobca = models.CharField(max_length=100, default="n/a")
  cena = models.FloatField(default=0)
  mena = models.CharField(max_length=3, default="EUR")  
  datum = models.DateTimeField(default=timezone.now, blank=True)
  miesto = models.CharField(max_length=200)
  obrlinka = models.CharField(max_length=600, default="n/a")
  
  def __unicode__(self):
    return self.nazov
      