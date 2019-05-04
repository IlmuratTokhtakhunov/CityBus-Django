from django import forms
from .models import User, Admin, Bus
class Authform(forms.Form):
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password    ")
class Regform(forms.Form):
	log = forms.CharField(required = True, min_length=3, max_length=20, label="Enter Login")
	pas = forms.CharField(required = True, min_length=6, max_length=20, label="Enter Password")
	nam = forms.CharField(required = True, min_length=2, max_length=20, label="Enter Name")
	sur = forms.CharField(label="Enter Surname")
	age = forms.IntegerField(label="Enter Age", min_value=1)
class Busform(forms.Form):
	num = forms.CharField(required = True, min_length=7, max_length=8, label="Enter Register Number")
	mar = forms.CharField(required = True, min_length=3, max_length=20, label="Enter Mark")
	mod = forms.CharField(required = True, min_length=2, max_length=20, label="Enter Model")
	path = forms.CharField(required = True, min_length=2, max_length=20, label="Enter Path")
	yea = forms.IntegerField(label="Enter Year of Manufacture", min_value=1960)
	sea = forms.IntegerField(label="Enter Number of Seats", min_value=10)
	cap = forms.IntegerField(label="Enter Capacity(in kg)", min_value=3000)
class Driform(forms.Form):
	log = forms.CharField(required = True, min_length=3, max_length=20, label="Enter Login")
	pas = forms.CharField(required = True, min_length=6, max_length=20, label="Enter Password")
	nam = forms.CharField(required = True, min_length=2, max_length=20, label="Enter Name")
	sur = forms.CharField(label="Enter Surname")
	path = forms.CharField(required = True, min_length=2, max_length=20, label="Enter Path")
	age = forms.IntegerField(label="Enter Age", min_value=18)
	cla = forms.IntegerField(label="Enter Class of Driver", min_value=1, max_value=13)
class Schform(forms.Form):
	sou = forms.CharField(required = True, min_length=8, max_length=40, label="Enter source location of trip")
	des = forms.CharField(required = True, min_length=8, max_length=40, label="Enter destination location of trip")
	dep = forms.CharField(required = True, min_length=8, max_length=25, label="Enter leaving time")
	arr = forms.CharField(required = True, min_length=8, max_length=25, label="Enter arrival time")
	pri = forms.IntegerField(required = True, min_value=1, label="Enter price of one seat")