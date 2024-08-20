"""
myapiproject/urls.py
"""
from django.contrib import admin
from django.urls import path,include
import myapiapp.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(myapiapp.urls)),
]
