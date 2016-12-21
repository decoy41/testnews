from __future__ import unicode_literals

from django.db import models

class NewsEnt(models.Model):
	title = models.CharField(max_length=200)		
	body = models.TextField()
	pub_date = models.DateTimeField()
	