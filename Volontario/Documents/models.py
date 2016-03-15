from django.db import models

class Docs(models.Model):
    date_place = models.CharField(max_length=40)
    date = models.DateField(help_text='Data (RRRR-MM-DD)')
    place = models.CharField(help_text='Miejscowosc', max_length=30)
    dest_to = models.TextField()
    title = models.CharField(help_text='Naglowek', max_length=60)
    text = models.TextField(help_text='Tekst')
    sign1 = models.TextField(help_text='Podpis')
    sign2 = models.TextField()
    header = models.TextField()
    #users = models.ManyToManyField()

    def add_doc(self):
        #self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.id

