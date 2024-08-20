"""
loginapp/forms.py
"""

from django import forms

class MyRegisterForm(forms.Form):
    uname = forms.CharField(max_length=100,empty_value="Enter Your Name")
    pw1 = forms.CharField(widget=forms.PasswordInput)
    pw2 = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

class MyLoginForm(forms.Form):
    uname = forms.CharField(max_length=100,empty_value="Enter Your Name")
    pw = forms.CharField(widget=forms.PasswordInput)

# Test in shell
# C:\python_training\web_django\Release_2\myproject> python manage.py shell
# >>> from loginapp.forms import MyRegisterForm
# >>> m = MyRegisterForm()
# >>> m.uname = 'u1'
# >>> m.pw1='p1'
# >>> m.pw2='p2'
# >>> m.email='asda'
# >>>
# >>> dir(m)