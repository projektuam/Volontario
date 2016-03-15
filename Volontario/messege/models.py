from django.db import models

# Create your models here.
class Message(models.Model):
	title = models.CharField("Temat Wiadomosci ",max_length = 50)
	text = models.TextField("Tresc Wiadomosci")
	#users = models.ManyToManyField('auth.user',blank = True)

	def add_messege(self):
		self.save()
	def __str__(self):
		return self.title
