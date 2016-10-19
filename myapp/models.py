from __future__ import unicode_literals

from django.db import models

class myclass(models.Model):
	website = models.CharField(max_length = 50)
	mail = models.CharField(max_length = 50)
   	nam = models.CharField(max_length = 50)
   	phonenumber = models.IntegerField()

class Meta:
	db_table = "mytable"

class Profile(models.Model):
	name = models.CharField(max_length = 50)
	picture = models.ImageField(upload_to = 'pictures')

	class Meta:
		db_table = "profile"