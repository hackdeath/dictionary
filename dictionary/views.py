from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Word, Language

def detailWord(request, word):
    ids = [obj.id for obj in Word.objects.filter(term=word)]
    result = Word.objects.filter(id_word__in=ids)
    words = [] # Agrupa as palavras de acordo com o id_word
    title = ""

    if (result):
        title = result[0].term

    for key in ids:
        words += [[word for word in query if word.id_word == key]]

    template = loader.get_template('dictionary/detailWord.html')
    context = {
        'title': title,
        'words': words,
    }

    return HttpResponse(template.render(context, request))

def index(request):
    languages = Language.objects.all()
    context = {'languages' : languages,}
    return render(request, 'dictionary/index.html', context)

def letter(request, letter):
    word_list = Word.objects.filter(term__startswith=letter)
    context = {
        'word_list': word_list,
        'letter': letter,
    }
    return render(request, 'dictionary/letter.html', context)
