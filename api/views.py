from django.shortcuts import render
from django.http import HttpResponse

def get_news(request):
	return HttpResponse("You are on /news endpoint")

def post_new(request):
	return HttpResponse("You are on /new endpoint")

def login(request):
	return HttpResponse("You are on /login endpoint")					