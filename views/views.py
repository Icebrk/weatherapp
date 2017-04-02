"""weatherapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Author : Nyameko Mateke
         060 995 3488
         nyameko.mateke@gmail.com
Date   : 2017-03-31

"""
from django.shortcuts import render
from .models import Weather

def index(request):
    return HttpResponse("Hello, world. You're at the Weather Forcast.")
