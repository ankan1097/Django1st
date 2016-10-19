from django.conf.urls import *
from django.views.generic import *
from myapp.views import *
urlpatterns = [ 	
		url(r'^hello/', hello, name = 'hello'),
		url(r'^bye/', another, name = 'me'), 
		url(r'^article/(\d+)/(\d+)', viewArticle, name = 'view'),
		url(r'^db/', crudops, name = 'nam'),
		url(r'^hello1/', hello1, name = 'hello1'),
		url(r'^static/$',StaticView.as_view()),
		url(r'^loogin/', TemplateView.as_view(template_name = 'login.html')),
		url(r'^login/', login, name = 'login'),
		url(r'^upload/', TemplateView.as_view(template_name = 'profile.html')),
		url(r'^saved/', SaveProfile, name = 'saved')]
