from django.db import models
from django.forms import ModelForm

persons = (

    ('Prezes Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM','Prezes Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM'),
    ('Opiekun Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM','Opiekun Wydziałowego Centrum Wolontariatu „VOLONTARIO” WSE UAM'),
    ('Prodziekan','Prodziekan'),
    ('Dziekan','Dziekan'),  
)


class Docs(models.Model):

    form_type = models.CharField(max_length=5, null=True, blank=True)
    date_place = models.CharField(max_length=40)
    date = models.DateField()
    place = models.CharField(help_text='Miejscowosc', max_length=30)
    dest_to = models.TextField()
    title = models.CharField(help_text='Naglowek', max_length=60)
    text = models.TextField(null=True, blank=True) #edytor summernote
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    chart = models.CharField(max_length=20, null=True, blank=True)
    chart2 = models.CharField(max_length=20, null=True, blank=True)
    chart3 = models.CharField(max_length=50, null=True, blank=True)
    chart4 = models.CharField(max_length=20, null=True, blank=True)
    sign1 = models.CharField(max_length=100, choices=persons, null=True, blank=True)
    sign2 = models.CharField(max_length=50, null=True, blank=True)
    sign3 = models.CharField(max_length=100, choices=persons, null=True, blank=True)
    sign4 = models.CharField(max_length=50, null=True, blank=True)
    header = models.TextField()
    #users = models.ManyToManyField()
    

    class Meta:
        ordering = ['-id']

    def add_doc(self):
        #self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.id


