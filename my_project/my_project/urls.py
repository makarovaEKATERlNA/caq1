from django.contrib import admin
from django.urls import path
import my_site.views

urlpatterns = [
    path('', my_site.views.index),
    path('create', my_site.views.create)
]
