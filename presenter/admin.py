"""weatherapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Author : Nyameko Mateke
         060 995 3488
         nyameko.mateke@gmail.com
"""

from django.contrib import admin
from . import models

admin.site.register(models.User)

admin.site.register(models.Weather)
