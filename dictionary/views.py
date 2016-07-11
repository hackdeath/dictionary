from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Word, Language

def detailWord(request, word):
    ids = [obj.id for obj in Word.objects.filter(term=word)]
    words = Word.objects.filter(id_word__in=ids)

    template = loader.get_template('detailWord.html')
    context = {
            'words': words,
    }

    return HttpResponse(template.render(context, request))

def index(request):
    return HttpResponse("index")
