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
		if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
			request.COOKIES['username']
			last_connection = request.COOKIES['last_connection']
			last_connection1 = datetime.strptime(last_connection[:-7], "%Y-%m-%d %H:%M:%S")
			if datetime.now() - last_connection1 < timedelta(seconds=2):
				# return render(request, 'loggedin.html', {"username" : username})
				HttpResponse("bye")

			else :
				return render(request, 'practice.html', {})
		else:
			return render(request, 'profile.html', {})