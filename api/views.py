from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone
from django.utils.html import strip_tags, escape
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
import json

from .models import NewsEnt

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def get_news(request):
	news = NewsEnt.objects.order_by('-pub_date')[:10]
   	news = json.dumps([n.dump() for n in news], default=date_handler)
   	return HttpResponse(news);

def post_new(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			json_data = json.loads(request.body)
			new = NewsItem()
			new.title = escape(strip_tags(json_data['title']))
			new.body = escape(strip_tags(json_data['body']))
			new.pub_date = timezone.now()
			new.save()
			return HttpResponse(status=200)
		else:
			return HttpResponse(status=403)	
	else:
		return redirect('./login')

def login(request):
	return HttpResponse("You are on /login endpoint")					