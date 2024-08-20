"""
loginapp/views.py
"""

from django.shortcuts import render, HttpResponse

# Create your views here.
def my_login_page(request):
    return render(request, 'newlogin.html', {})

def my_register_page(request):
    return render(request, 'newregister.html', {})

def my_addnewuser_page(request):
    """
    Form data will be captured by framwork and it will keep im
    POST request: request.POST dictionary
    PUT request: request.PUT dictionary
    """

    from .models import MyModel

    if request.method == "POST":
        entered_username = request.POST.get('uname')
        entered_password_1 = request.POST.get('pw1')
        entered_password_2 = request.POST.get('pw2')
        entered_email = request.POST.get('email')
        if entered_password_1 != entered_password_2:
            return HttpResponse("Both Passwords should match")

        users_count = MyModel.objects.filter(username=entered_username).count()
        if users_count > 0:
            return HttpResponse("Account already exists")
        else:
            new_user = MyModel()
            new_user.username = entered_username
            new_user.password =entered_password_1
            new_user.email = entered_email
            new_user.save()
            return HttpResponse("Account Created")
    else:
        return HttpResponse("Method Not Supported")


def my_validatelogin_page(request):
    from .models import MyModel

    if request.method == "POST":
        entered_username = request.POST.get('uname')
        entered_password_1 = request.POST.get('pw')

        users_count = MyModel.objects.filter(username=entered_username, password=entered_password_1).count()
        if users_count > 0:
            import sqlite3
            con = sqlite3.connect("my_data_db.sqlite3")
            cur = con.cursor()
            cur.execute("select * from my_data_table")
            res = cur.fetchall()
            return render(request, 'newlogreport.html', {'my_db_data': res} )
        else:
            return HttpResponse("Login Failed")
    else:
        return HttpResponse("Method Not Supported")