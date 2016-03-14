from django import forms
from django.forms import ModelForm
from .models import Docs
from django.utils import timezone

class DocsForm(forms.ModelForm):

    class Meta:
       model = Docs
       fields = ('date', 'place','text','sign1','title')

class ZwolnieniaForm(forms.ModelForm):

    class Meta:
      model = Docs
      fields = ('date', 'place','text')

