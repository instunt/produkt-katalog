from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Produkt(models.Model):
  nazov = models.CharField(max_length=100)
  shoplinka = models.CharField(max_length=600, default="n/a")
  obrlinka = models.CharField(max_length=600, default="n/a")
  created_date = models.DateTimeField(default=timezone.now)
  
  def __unicode__(self):
    return self.nazov