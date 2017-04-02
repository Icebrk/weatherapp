"""weatherapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Author : Nyameko Mateke
         060 995 3488
         nyameko.mateke@gmail.com
"""
from django.db import models

class User(models.Model):
    email_address = models.CharField(max_length=70)
    password = models.CharField(max_length=70)
    password_repeat = models.CharField(max_length=70)

    def __str__(self): # __unicode__ on Python 2
        return self.email_address

class Weather(models.Model):

    pub_date = models.DateField()
    headline = models.CharField(max_length=450)
    min_temp = models.Interger()
    max_temp = models.Interger()
    wind = models.Interger()
    rain = models.Interger()
    wind = models.Interger()

    def __str__(self): # __unicode__ on Python 2
        return self.headline
