from __future__ import unicode_literals

from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 100,required = False )
	password = forms.CharField(widget = forms.PasswordInput(), required = False)

class ProfileForm(forms.Form):
	name = forms.CharField(max_length = 100,required = False)
	pictures = forms.FileField()