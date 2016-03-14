
from django.shortcuts import render, get_object_or_404
from .models import Event
from .forms import EventForm
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User



############################################################################################################
def event_list(request):
    
    events = Event.objects.all
    

    return render(request, 'event/event_list.html', {'events':events})


###########################################################################################################
def task_list(request):
    
    tasks = Task.objects.all


    return render(request, 'event/task_list.html',{'tasks':tasks})
###########################################################################################################

def event_detal(request, pk):
    
    detal = get_object_or_404(Event,pk=pk)
    task = Task.objects.all().filter(event_id=pk)
    users = User.objects.all().filter(event_id=pk)
    
    return render(request, 'event/detail.html', {'events': detal, 'tasks':task, 'users':users})


##########################################################################################################
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.publication_date = timezone.now()
            event.save()
            return redirect('Event.views.event_detal', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'event/event_edit.html', {'form': form})
##########################################################################################################
def event_edit(request, pk):
    event = get_object_or_404(Event,pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            event.publication_date = timezone.now()
            event.save()
            return redirect('Event.views.event_detal', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'event/event_edit.html', {'form': form})


##########################################################################################################
def event_remove(request, pk):
    event = get_object_or_404(Event,pk=pk)
    event.delete()
    return redirect('Event.views.event_list')
##########################################################################################################
def new_task(request,pk):
    event = get_object_or_404(Event,pk=pk)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            
            task = form.save(commit=False)
            task.event_id = pk
            task.save()
            
                        
            return redirect('Event.views.event_detal', pk=event.pk)
    else:
        form = TaskForm()
    return render(request, 'event/task_edit.html', {'form': form})
##########################################################################################################
def task_remove(request, pk, task_id):
    event = get_object_or_404(Event,pk=pk)
    task = get_object_or_404(Task,id=task_id)
    task.delete()
    return redirect('Event.views.event_detal', pk=event.pk)
##########################################################################################################    
def login_user(request):
  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            
            if user.is_active:
               
                login(request, user)
                return redirect('Event.views.event_list')
            else:
                
                return HttpResponse("Konto wylaczone")
        else:
            
            
            return HttpResponse("Bledny login lub haslo")

    
    else:
       
           return render(request, 'event/login.html', {})

##############################################################################################################
def event_user(request,pk):
    events = get_object_or_404(Event,pk=pk)
    current_user= request.user
    
   
        
        
            
           
            
            
    if request.user.is_authenticated():
         current_user= request.user
        
         events.users_id = current_user.id
         
         return redirect('Event.views.event_detal', pk=events.pk)
    else:
         return HttpResponse("Bledny login lub haslo")
    

  
    

