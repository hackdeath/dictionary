from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Word, Language

def detailWord(request, word):
    ids = [obj.id_word for obj in Word.objects.filter(term=word)]
    ids = list(set(ids))
    result = Word.objects.filter(id_word__in=ids)
    words = [] # Agrupa as palavras de acordo com o id_word

    for key in ids:
        words += [[word for word in result if word.id_word == key]]

    template = loader.get_template('dictionary/detailWord.html')
    context = { 'title': word, 'words': words, }

    return HttpResponse(template.render(context, request))

def index(request):
    languages = Language.objects.all()
    context = {'languages' : languages,}
    return render(request, 'dictionary/index.html', context)

def letter(request, lang, letter):
    word_list = Word.objects.filter(language=lang).filter(term__startswith=letter).order_by('term')
    alphabet_list = Language.objects.filter(language=lang)
    context = {
        'word_list': word_list,
        'alphabet_list': alphabet_list,
        'letter': letter,
    }
    return render(request, 'dictionary/letter.html', context)
