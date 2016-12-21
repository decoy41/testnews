from django.shortcuts import render
from django.http import HttpResponse

def get_news():
	return HttpResponse("You are on /news endpoint")

def post_new():
	return HttpResponse("You are on /new endpoint")

def login():
	return HttpResponse("You are on /login endpoint")					