from django import forms
from django.forms import ModelForm
from .models import Docs
from django.utils import timezone

class DocsForm(forms.ModelForm):

    class Meta:
       model = Docs
       fields = ('place','date','title','text','sign1')

class ZwolnieniaForm(forms.ModelForm):

    class Meta:
      model = Docs
      fields = ('date', 'place','text')

