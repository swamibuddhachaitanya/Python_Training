"""
homeapp/urls.py
"""
from django.urls import path
from .views import my_index_page
from .views import my_about_page
from .views import my_logout_page
from .views import my_weatherapi_page

urlpatterns = [
    path('', my_index_page),
    path('about/', my_about_page),
    path('logout/', my_logout_page),
    path('weatherapi/', my_weatherapi_page),
]