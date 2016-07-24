from django import forms

class WordForm(forms.Form):
    language   = forms.CharField(max_length=5)
    id_word    = forms.IntegerField()
    term       = forms.CharField(max_length=30)
    definition = forms.CharField(max_length=150)
    category   = forms.CharField(max_length=30)

