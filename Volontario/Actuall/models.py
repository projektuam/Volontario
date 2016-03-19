from django.db import models
from django.utils import timezone
import datetime


class Aktual(models.Model):
    author = models.ForeignKey("auth.User",max_length=20)
    title = models.CharField("Nazwa wydarzenia", max_length=100)
    description = models.TextField("Opis")
    publication_date = models.DateTimeField("Data publikacji",    blank=True,null=True)
   
    
    class Meta:
        ordering = ['-publication_date']
   

    def add_aktual(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

