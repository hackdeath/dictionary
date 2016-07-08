from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def detailWord(request):
	return HttpResponse("This is the page of word's details")