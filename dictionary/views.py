from  django.shortcuts import render
from  django.http      import HttpResponse, HttpResponseRedirect
from  django.template  import loader
from .models           import Word, Language
from .forms            import WordForm

def detailWord(request, word):
    ids = list(set([obj.id_word for obj in Word.objects.filter(term=word, stage='n')]))
    template = loader.get_template('dictionary/detailWord.html')
    result = Word.objects.filter(id_word__in=ids, stage='n')
    words = [] # Agrupa as palavras de acordo com o id_word

    for key in ids:
        words += [[word for word in result if word.id_word == key]]

    template = loader.get_template('dictionary/detailWord.html')
    context = { 'title': word, 'words': words }

    return HttpResponse(template.render(context, request))

def submitWord(request, id_word):
    template = loader.get_template('dictionary/submitWord.html')

    if request.method == 'GET':
        if id_word != '0':
            form = WordForm(initial={'language': 'en-us', 'id_word': id_word})
        else:
            form = WordForm(initial={'language': 'en-us', 'id_word': Word.objects.all().last().id_word + 1})
            
        return HttpResponse(template.render({'form': form }, request))
    else:
        form = WordForm(request.POST)

        if form.is_valid():
            new_word = Word.objects.create(language   = Language.objects.get(language=form.cleaned_data['language']),
                                           id_word    = form.cleaned_data['id_word'],
                                           term       = form.cleaned_data['term'],
                                           definition = form.cleaned_data['definition'],
                                           category   = form.cleaned_data['category'],
                                           stage      = 'y')

            new_word.save()

        return HttpResponse(template.render({}, request))

def index(request):
    languages = Language.objects.all()
    context = {'languages' : languages,}
    return render(request, 'dictionary/index.html', context)

def letter(request, lang):
    word_list = Word.objects.filter(language=lang, stage='n').order_by('term')
    alphabet_list = Language.objects.get(language=lang)
    words = []

    for letter in list(alphabet_list.alphabet):
        words += [[word.term for word in word_list if word.term[0] == letter]]

    context = {
        'word_list': words,
        'alphabet_list': alphabet_list,
        'letter': letter,
    }

    return render(request, 'dictionary/letter.html', context)

def stagearea(request):
    words = Word.objects.filter(stage='y')
    context = { 'words': words, }
    template = loader.get_template('dictionary/stagearea.html')

    return HttpResponse(template.render(context, request))

def accept(request, id):
    new_word = Word.objects.get(pk=id)
    old_word = Word.objects.filter(language=new_word.language, id_word=new_word.id_word, stage='n')

    if old_word.exists():
        old_word[0].delete()

    new_word.stage = 'n'
    new_word.save()

    return HttpResponseRedirect('/dictionary/stage')

def refuse(request, id, redirect):
    if redirect == 'stage':
        topage = '/dictionary/stage/'
    else:
        topage = "/dictionary/letter/{0}/".format(redirect)

    deleteWord(id)

    return HttpResponseRedirect(topage)

def deleteWord(id):
    word = Word.objects.get(pk=id)

    word.delete()
