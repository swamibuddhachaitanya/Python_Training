"""
homeapp/urls.py
"""
from django.urls import path
from .views import my_index_page
from .views import my_about_page
from .views import my_weatherapi_page
from .views import my_weatherreport_page

urlpatterns = [
    path('', my_index_page),
    path('about/', my_about_page),
    path('weatherapi/', my_weatherapi_page),
    path("weatherreport/", my_weatherreport_page),
]

# http://127.0.0.1:8000/weatherreport/