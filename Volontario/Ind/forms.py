from django import forms
from django.forms import ModelForm, DateField
from .models import Volin
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class VolinForm(forms.ModelForm):

    class Meta:
       model = Volin
       fields = ('author', 'title','destination','description')
       widgets = {
                 'description' : SummernoteWidget(),
           }
