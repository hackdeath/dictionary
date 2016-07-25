from  django import forms
from .models import Language

class WordForm(forms.Form):
    language   = forms.ModelChoiceField(queryset = Language.objects.all())
    term       = forms.CharField(max_length=30)
    definition = forms.CharField(max_length=150)
    category   = forms.CharField(max_length=30)

