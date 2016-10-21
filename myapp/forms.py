from __future__ import unicode_literals
from datetime import *
from django import forms
from django.http import HttpResponse
from django.shortcuts import render

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 100,required = False )
	password = forms.CharField(widget = forms.PasswordInput(), required = False)

class ProfileForm(forms.Form):
	name = forms.CharField(max_length = 100,required = False)
	pictures = forms.FileField()

def formView(request):
		if request.session.has_key('username'):
			username = request.session['username']
			return render(request, 'loggedin.html', {"username" : username})
		else:
			return render(request, 'login.html', {})