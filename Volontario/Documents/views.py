# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Docs
from .forms import DocsForm
from django.shortcuts import redirect
from django.utils import timezone
from weasyprint import HTML, CSS
from mako.template import Template
from mako.runtime import Context
from io import StringIO

# typy formularzy
#    1 - zwolninie
#    2 - prośba o patronat
##########################################################################################################
def zwolnienie_new(request):
    if request.method == "POST":
        form = DocsForm(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.publication_date = timezone.now()
            doc.form_type = 1
            doc.save()
            
            mytemplate = Template(filename='Documents/html&css/zwolnienie.mako')

            #t = Template("""START->\\ for x in xrange(10):${x}\\endfor""") 

            buf = StringIO()
            ctx = Context(buf, **request.POST)
            mytemplate.render_context(ctx)

            HTML(string=buf.getvalue()).write_pdf('Documents/wygenerowane/zwolnienie indywidualne.pdf',
                stylesheets=[CSS(string='body { font-family: serif !important }')])
            return redirect('Documents.views.docs_list')
    else:
        form = DocsForm()
    return render(request, 'documents/zwolnienie_edit.html', {'form': form})
##########################################################################################################
def docs_list(request):
    
    docs = Docs.objects.all


    return render(request, 'documents/docs_list.html', {'docs':docs})
	
###########################################################################################################
def patron_new(request):
    if request.method == "POST":
        form = DocsForm(request.POST)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.publication_date = timezone.now()
            doc.form_type = 2
            doc.save()
            
            mytemplate = Template(filename='Documents/html&css/patron.mako')

            buf = StringIO()
            ctx = Context(buf, **request.POST)
            mytemplate.render_context(ctx)

            HTML(string=buf.getvalue()).write_pdf('Documents/wygenerowane/wniosek o patronat i dofinansowanie.pdf',
                stylesheets=[CSS(string='body { font-family: serif !important }')])

            return redirect('Documents.views.docs_list')
    else:
        form = DocsForm()
    return render(request, 'documents/patron_edit.html', {'form': form})