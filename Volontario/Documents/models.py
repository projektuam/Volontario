from django.db import models

class Docs(models.Model):
    date_place = models.CharField(max_length=40)
    date = models.DateField()
    place = models.CharField(max_length=30)
    dest_to = models.TextField()
    title = models.CharField(max_length=60)
    text = models.TextField()
    sign1 = models.TextField()
    sign2 = models.TextField()
    header = models.TextField()
    #users = models.ManyToManyField()

    def add_doc(self):
        #self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.id

