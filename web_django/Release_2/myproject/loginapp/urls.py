"""
loginapp/urls.py
"""
from django.urls import path
from .views import my_login_page
from .views import my_register_page
from .views import my_addnewuser_page
from .views import my_validatelogin_page


urlpatterns = [
    path('', my_login_page),
    path('register/', my_register_page),
    path('addnewuser/', my_addnewuser_page),
    path('validatelogin/', my_validatelogin_page),

]
