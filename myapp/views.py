from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from myapp.models import myclass
from datetime import datetime
from myapp.forms import LoginForm


def hello(request):
	today = datetime.now().date()
	return render(request,"practice.html",{"today":today})

def another(request):
	text = """<h2>another hello world!</h1>"""
	return HttpResponse(text)

def viewArticle(request,num1,num2):
	text = """article no. %s|%s"""%(num2,num1)
	return HttpResponse(text)

def crudops(request):
	mytable = myclass(
		website = "www.cse.iitb.ac.in/~iankan",
		mail = "ankansardarth@gmail.com",
		nam = "Ankan",
		phonenumber = "911")
	mytable.save()
	objects = myclass.objects.all()
	res ='Printing all Dreamreal entries in the DB : <br>'
	for elt in objects:
		res+= elt.nam+"<br>"
	qs = myclass.objects.filter(nam = "Ankan")
	res += "Found : %s results<br>"%len(qs)
	return HttpResponse(res)

def hello1(request):
	today = datetime.now().date()
	return redirect("https://www.google.com",permanent=True)

class StaticView(TemplateView):
	template_name = "practice.html"

def login(request):
	username = "none"

	if request.method == "POST":
		MyLoginForm = LoginForm(data = request.POST)

		if MyLoginForm.is_valid():
			username = "aa"
			username = MyLoginForm.cleaned_data['username']
	else:
		MyLoginForm = LoginForm()

	return render(request, 'loggedin.html', {"username" : username})