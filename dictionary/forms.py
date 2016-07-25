from  django import forms
from .models import Language, Word

class WordForm(forms.Form):
    id_word    = forms.CharField(Word.objects.all().last().id_word + 1)
    language   = forms.ModelChoiceField(queryset = Language.objects.all())
    term       = forms.CharField(max_length=30)
    definition = forms.CharField(max_length=150)
    category   = forms.ChoiceField(choices = ((1, ('hardware')), (2, ('concept')), (3, ('software'))))

