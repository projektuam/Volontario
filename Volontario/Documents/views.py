from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Docs
from .forms import DocsForm, ZwolnieniaForm
from django.shortcuts import redirect
from django.utils import timezone
from weasyprint import HTML, CSS

##########################################################################################################
def new(request):
    if request.method == "POST":
        form = DocsForm(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.publication_date = timezone.now()
            doc.save()
            HTML(string=doc.place + " " + str(doc.date) + '<br><br>' + doc.title + '<br>' + doc.text + '<br><br>' + doc.sign1).write_pdf('Documents/wygenerowane/przyklad.pdf',
                stylesheets=[CSS(string='body { font-family: serif !important }')])
            return redirect('Documents.views.docs_list')
    else:
        form = DocsForm()
    return render(request, 'documents/docs_edit.html', {'form': form})
##########################################################################################################
def docs_list(request):
    
    docs = Docs.objects.all


    return render(request, 'documents/docs_list.html', {'docs':docs})
	
###########################################################################################################
def zwolnienie(request):
    if request.method == "POST":
        form = ZwolnieniaForm(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.publication_date = timezone.now()
            doc.save()
            return redirect('Documents.views.docs_list')
    else:
        form = ZwolnieniaForm()
    return render(request, 'documents/docs_edit.html', {'form': form})
