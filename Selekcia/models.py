from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Produkt(models.Model):
  autor = models.ForeignKey('auth.User')
  nazov = models.CharField(max_length=100)
  linka = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  
  def __unicode__(self):
    return self.nazov