from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def detailWord(request, word):
	return HttpResponse("This is the page of word's details")

def index(request):
	return HttpResponse("index")