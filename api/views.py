from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone
from django.utils.html import strip_tags, escape
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from .models import NewsEnt

def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

def get_news(request):
	news = NewsEnt.objects.order_by('-pub_date')[:10]
   	news = json.dumps([n.dump() for n in news], default=date_handler)
   	return HttpResponse(news);
        #serializers.serialize('json', news),
        #content_type='application/json'
        #news
   		#)

def post_new(request):
	return HttpResponse("You are on /new endpoint")

def login(request):
	return HttpResponse("You are on /login endpoint")					