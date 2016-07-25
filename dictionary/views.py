from  django.shortcuts import render
from  django.http      import HttpResponse
from  django.template  import loader
from .models           import Word, Language
from .forms            import WordForm

def detailWord(request, word):
    ids = list(set([obj.id_word for obj in Word.objects.filter(term=word, stage='n')]))
    template = loader.get_template('dictionary/detailWord.html')
    result = Word.objects.filter(id_word__in=ids)
    words = [] # Agrupa as palavras de acordo com o id_word

    for key in ids:
        words += [[word for word in result if word.id_word == key]]

    template = loader.get_template('dictionary/detailWord.html')
    context = { 'title': word, 'words': words, }

    return HttpResponse(template.render(context, request))

def submitWord(request):
    template = loader.get_template('dictionary/submitWord.html')

    if request.method == 'GET':
        form = WordForm(initial={'language': 'en-us'})
        return HttpResponse(template.render({'form': form }, request))
    else:
        form = WordForm(request.POST)

        if form.is_valid():
            new_word = Word.objects.create(language   = Language.objects.get(language=form.cleaned_data['language']),
                                           id_word    = Word.objects.all().last().id_word + 1,
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

def letter(request, lang, letter):
    word_list = Word.objects.filter(language=lang).filter(term__startswith=letter).order_by('term')
    alphabet_list = Language.objects.filter(language=lang)
    context = {
        'word_list': word_list,
        'alphabet_list': alphabet_list,
        'letter': letter,
    }
    return render(request, 'dictionary/letter.html', context)
