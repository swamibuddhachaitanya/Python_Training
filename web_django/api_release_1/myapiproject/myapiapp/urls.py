"""
myapiapp/urls
"""

from django.urls import path
from .views import mytestapi
from .views import getdbdata
from .views import postdbdata
from .views import putdbdata
from .views import patchdbdata
from .views import deletedbdata
from django.urls import path

urlpatterns= [
    path('',mytestapi),
    path('getdbdata/',getdbdata),
    path('postdbdata/',postdbdata),
    path('putdbdata/',putdbdata),
    path('patchdbdata/',patchdbdata),
    path('deletedbdata/',deletedbdata),
]