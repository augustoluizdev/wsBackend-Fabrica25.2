from django import forms
from .models import Pessoa, Livro

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ['nome', 'idade', 'email']

class LivroForm(forms.Form):
    isbn = forms.CharField(label='ISBN', max_length=13)