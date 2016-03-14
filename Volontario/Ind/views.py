from django.shortcuts import render, get_object_or_404
from .models import Volin
from .forms import VolinForm
from django.shortcuts import redirect
from django.utils import timezone

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
    

    return render(request, 'volin/detail.html', {'volins': detal})
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
