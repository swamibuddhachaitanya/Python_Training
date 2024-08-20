"""
homeapp/views.py
"""

from django.shortcuts import render, HttpResponse

# Create your views here.
# def my_index_page(request):
#     return HttpResponse("Welcome")

# Create your views here.
def my_index_page(request):
    return render(request, 'newindex.html', {})

def my_about_page(request):
    return render(request, 'newabout.html', {})

def my_weatherapi_page(request):
    return render(request, 'newweatherapi.html', {})

def my_weatherreport_page(request):
    city_name = request.POST.get('city')
    api_endpoint = f'https://demoqa.com/utilities/weather/city/{city_name}'
    import requests
    api_response = requests.get(api_endpoint)
    api_response = api_response.json()
    return render(request, "newweatherreport.html", {"api_data": api_response})