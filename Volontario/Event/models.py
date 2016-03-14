from django.db import models
from django.utils import timezone
from datetime import timedelta
import datetime

class Event(models.Model):
    author = models.CharField("Autor",max_length=20)
    title = models.CharField("Nazwa wydarzenia", max_length=100)
    time = models. TimeField("Godzina", auto_now=False)
    date = models.DateField("Data",auto_now=False)
    destination = models.CharField("Miejsce ", max_length=50, blank=True)
    description = models.TextField("Opis")
    #tasks = models.ForeignKey(Task,blank=True,null=True, on_delete=models.CASCADE)
    publication_date = models.DateTimeField("Data publikacji", blank=True,null=True)
    #attach = models.FieldFile()
    #image = models.ImageField(upload_to=None, height_field=50, width_field=50)
    
  
    
    class Meta:
        ordering = ['-id']
   

    def add_event(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Task(models.Model):
    id = models.AutoField(primary_key=True,blank=True)
    title = models.CharField("Nazwa", max_length=100,blank=True)
    description = models.TextField("Opis", blank=True)
    event = models.ForeignKey(Event,null=True, blank=True,on_delete=models.CASCADE)
    class Meta:
        ordering = ['-id']

    def add_task(self):
        self.save()
        event_id = Event.id
 
    def __str__(self):
        return self.title

