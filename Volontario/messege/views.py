from django.shortcuts import render
from .models import Message
# Create your views here.
def messege_list(request):
	message = Message.objects.all
	return render(request, 'messege/contact.html',{'message':message})
