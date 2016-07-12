from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def detailWord(request, word):
    return HttpResponse("This is the page of {0}'s details".format(word))

def index(request):
    return render(request, 'dictionary/index.html')
