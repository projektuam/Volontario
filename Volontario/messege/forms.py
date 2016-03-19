from django import forms
from django.forms import ModelForm, DateField
from .models import Message
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class MessageForm(forms.ModelForm):

    class Meta:
       model = Message
       fields = ('title','text')
       widgets = {
                 'description' : SummernoteWidget(),
           
                 }

