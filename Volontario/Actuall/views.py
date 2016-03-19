from django.shortcuts import render, get_object_or_404
from .models import Aktual
from .forms import AktualForm

from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse


def aktual_list(request):
    
    news = Aktual.objects.all
    

    return render(request, 'aktual/aktual_list.html', {'news':news})
###################################################################################
def aktual_detal(request, pk):
    
    new = get_object_or_404(Aktual,pk=pk)
 
    
    return render(request, 'aktual/detail.html', {'news': new})
################################################################################
def aktual_new(request):
    if request.method == "POST":
        form = AktualForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.publication_date = timezone.now()
            new.save()
            return redirect('Actuall.views.aktual_detal', pk=new.pk)
    else:
        form = AktualForm()
    return render(request, 'aktual/aktual_edit.html', {'form': form})
##########################################################################################################
def aktual_edit(request, pk):
    new = get_object_or_404(Aktual,pk=pk)
    if request.method == "POST":
        form = AktualForm(request.POST, instance=new)
        if form.is_valid():
            new = form.save(commit=False)
            new.publication_date = timezone.now()
            new.save()
            return redirect('Actuall.views.aktual_detal', pk=new.pk)
    else:
        form = AktualForm(instance=new)
    return render(request, 'aktual/aktual_edit.html', {'form': form})


##########################################################################################################
def aktual_remove(request, pk):
    new = get_object_or_404(Aktual,pk=pk)
    new.delete()
    return redirect('Actuall.views.aktual_list')

