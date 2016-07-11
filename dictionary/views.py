from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Language, Word

def detailWord(request, word):
	return HttpResponse("This is the page of word's details")

def index(request):
    alphabet_list = Language.objects.order_by('language')
    context = {'alphabet_list': alphabet_list}
    return render(request, 'index.html', context)