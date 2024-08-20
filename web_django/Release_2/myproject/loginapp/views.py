"""
loginapp/views.py
"""

from django.shortcuts import render, HttpResponse

# Create your views here.
from .forms import MyLoginForm
def my_login_page(request):
    current_cookie_value = request.COOKIES.get("MyCookie")
    print("current_cookie_value:", current_cookie_value)
    login_form = MyLoginForm()
    return render(request, "loginapp/newlogin.html", {"login_form": login_form})

from .forms import MyRegisterForm
def my_register_page(request):
    new_form = MyRegisterForm()
    return render(request, "loginapp/newregister.html", {"new_form": new_form})


def my_addnewuser_page(request):
    """
    """

    from .models import MyModel
    from .forms import MyRegisterForm

    if request.method == "POST":
        form_data = MyRegisterForm(request.POST)
        if form_data.is_valid():
            form_data = form_data.cleaned_data
            if form_data.get("pw1") != form_data.get("pw2"):
                return HttpResponse("Both Passwords should match")
            users_count = MyModel.objects.filter(username=form_data.get("uname")).count()
            if users_count > 0:
                return HttpResponse("Account already exists")
            else:
                new_user = MyModel()
                new_user.username = form_data.get("uname")
                new_user.password = form_data.get("pw1")
                new_user.email = form_data.get("email")
                new_user.save()
                return HttpResponse("Account Created")
        else:
            return HttpResponse("Invalid data")
    else:
        return HttpResponse("Method Not Supported")


def my_validatelogin_page(request):
    from .models import MyModel
    from .forms import MyLoginForm

    if request.method == "POST":

        login_data = MyLoginForm(request.POST)
        if login_data.is_valid():
            login_data = login_data.cleaned_data

            users_count = MyModel.objects.filter(username=login_data.get("uname"), password=login_data.get("pw")).count()
            if users_count > 0:
                # request.session["some_key"] = "some_value"
                request.session["username"] = login_data.get("uname")
                import sqlite3
                con = sqlite3.connect("my_data_db.sqlite3")
                cur = con.cursor()
                cur.execute("select * from my_data_table")
                res = cur.fetchall()
                response = render(request, 'loginapp/newlogreport.html', {'my_db_data': res} )
                response.set_cookie("MyCookie", login_data.get("uname"))
                return response
            else:
                return HttpResponse("Login Failed")
        else:
            return HttpResponse("Please pass valid data")
    else:
        return HttpResponse("Method Not Supported")