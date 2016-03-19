from django.shortcuts import render, get_object_or_404
from .models import Volin
from .forms import VolinForm
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User



def volin_list(request):
    
    volins = Volin.objects.all


    return render(request, 'volin/volin_list.html', {'volins':volins})

############################################################################
def volin_new(request):
    if request.method == "POST":
        form = VolinForm(request.POST)
        if form.is_valid():
            volin = form.save(commit=False)
            volin.publication_date = timezone.now()
            volin.save()
            return redirect('Ind.views.volin_list')
    else:
        form = VolinForm()
    return render(request, 'volin/volin_edit.html', {'form': form})
#############################################################################
def volin_detal(request, pk):
    
    detal = get_object_or_404(Volin,pk=pk)
    users = User.objects.all().filter(volin=pk)

    return render(request, 'volin/detail.html', {'volins': detal, 'users':users})
##############################################################################
def volin_remove(request, pk):
    volin = get_object_or_404(Volin,pk=pk)
    volin.delete()
    return redirect('Ind.views.volin_list')
###############################################################################
def volin_edit(request, pk):
    volin = get_object_or_404(Volin,pk=pk)
    if request.method == "POST":
        form = VolinForm(request.POST, instance=volin)
        if form.is_valid():
            volin = form.save(commit=False)
            volin.publication_date = timezone.now()
            volin.save()
            return redirect('Ind.views.volin_detal', pk=volin.pk)
    else:
        form = VolinForm(instance=volin)
    return render(request, 'volin/volin_edit.html', {'form': form})
##################################################################################
def volin_user(request,pk):
    volin = get_object_or_404(Volin,pk=pk)
    users = User.objects.filter(volin=pk)
    current_user= request.user
    cur_id = current_user.id
    if request.user.is_authenticated():
        
        if users.filter(id=cur_id).exists(): 
            return redirect('Ind.views.volin_detal', pk=volin.pk)
             
        else:
            current_user.volin.add(pk)
            return redirect('Ind.views.volin_detal', pk=volin.pk)
            
    else:
        return HttpResponse("Jesteś nie zalogowany ;)")

#####################################################################################
def user_remove(request, pk,usr):
    volin = get_object_or_404(Volin,pk=pk)
    current_user = request.user
    cur_id = current_user.id
    user = get_object_or_404(User,id=usr)
    if request.user.is_authenticated():
         
        user.volin.remove(pk)
        return redirect('Ind.views.volin_detal', pk=volin.pk)    
    else:
        return HttpResponse("Blad")
