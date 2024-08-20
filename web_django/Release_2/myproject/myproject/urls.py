"""
myproject/urls.py
"""
from django.contrib import admin
from django.urls import path, include
import homeapp.urls
import loginapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(homeapp.urls)),
    path('login/', include(loginapp.urls)),
]