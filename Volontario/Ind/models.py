from django.db import models
from django.utils import timezone





#Wolontariat indywidualny model

class Volin(models.Model):
    author = models.CharField('auth.user',max_length=20)
    title = models.CharField("Nazwa zadania", max_length=100)
    destination = models.CharField("Miejsce ", max_length=50, blank=True)
    description = models.TextField("Opis")
    publication_date = models.DateTimeField("Data publikacji", blank=True,null=True)
    
    
    class Meta:
        ordering = ['-id']
   

    def add_volin(self):
        self.publication_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



