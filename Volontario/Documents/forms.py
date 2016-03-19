from django import forms
from django.forms import ModelForm
from .models import Docs
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class DocsForm(forms.ModelForm):

    class Meta:
       model = Docs
       fields = ('date', 'place','chart3','text','text2','text3','text4','chart','chart2','chart4','sign1','sign2','sign3','sign4')
       widgets = {
          'text': SummernoteWidget(attrs={'width': '90%', 'height': '300px'}),
          'text2': forms.Textarea(attrs={'rows':1, 'cols':80}),
          'text3': forms.Textarea(attrs={'rows':1, 'cols':80}),
          'text4': forms.Textarea(attrs={'rows':3, 'cols':100}),           
        }
