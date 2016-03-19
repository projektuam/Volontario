from django import forms
from django.forms import ModelForm, DateField
from .models import Event
from .models import Task
from django.utils import timezone
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.contrib.admin.widgets import AdminDateWidget


class EventForm(forms.ModelForm):

    class Meta:
       model = Event
       fields = ('author', 'title','time','date','destination','description')
       widgets = {
                 'description' : SummernoteWidget(),
                 'date' : AdminDateWidget(),
           
                                        
               
                 
                 }
       class Media:
           css = {
               'all': ('layout.css',)
                 }
 
class TaskForm(forms.ModelForm):
    class Meta:
       model = Task
       fields = ('title', 'description')
       widgets = {
                 'description' : SummernoteWidget(),
                 }



