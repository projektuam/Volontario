from django import forms
from django.forms import ModelForm, DateField
from .models import Aktual
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class AktualForm(forms.ModelForm):

    class Meta:
       model = Aktual
       fields = ('author', 'title','description')
       widgets = {
                 'description' : SummernoteWidget(),
           
                                        
               
                 
                 }
