from django.shortcuts import render

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello how does this thing work I don't know.")
	