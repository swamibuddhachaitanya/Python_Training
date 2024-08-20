"""
myapiapp/urls.py
"""
from django.urls import path
from .views import MyAPIClass

urlpatterns = [
    path('', MyAPIClass.as_view())
]