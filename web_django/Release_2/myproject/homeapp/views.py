"""
homeapp/views.py
"""

from django.shortcuts import render
from django.shortcuts import redirect

def my_index_page(request):
    return render(request, 'homeapp/newindex.html',{})

def my_about_page(request):
    return render(request, 'homeapp/newabout.html',{})

def my_logout_page(request):
    request.session.pop("username")
    return redirect("/login")

def my_weatherapi_page(request):
    if request.session.get("username"):
        return render(request, 'homeapp/newweatherapi.html', {})
    else:
        return redirect("/login")



