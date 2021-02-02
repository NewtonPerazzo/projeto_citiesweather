from django import forms

from app.models import Cidade


class CidadeForm(forms.ModelForm):
    class Meta():
        model = Cidade
        fields = ['nome', 'pais']

