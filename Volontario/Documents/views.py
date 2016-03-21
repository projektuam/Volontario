# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from .models import Docs
from .forms import DocsForm
from django.shortcuts import redirect
from django.utils import timezone
from weasyprint import HTML, CSS
from mako.template import Template
from mako.runtime import Context
from io import StringIO
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from pdfrw import PdfReader
from django.contrib.auth.models import User

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

            buf = StringIO()
            ctx = Context(buf, **request.POST)
            mytemplate.render_context(ctx)
            # '/tmp/'
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="zwolnienie indywidualne.pdf"'

            html = HTML(string=buf.getvalue())
            html.write_pdf(response, stylesheets=[CSS('Documents/html&css/style.css')])
            return response
    else:
        form = DocsForm()
    return render(request, 'documents/zwolnienie_edit.html', {'form': form})
##########################################################################################################
def zwolnienie_edit(request, pk):
    doc = get_object_or_404(Docs,id=pk)
    if request.method == "POST":
        form = DocsForm(request.POST, instance=doc)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.publication_date = timezone.now()
            doc.form_type = 1
            doc.save()

            mytemplate = Template(filename='Documents/html&css/zwolnienie.mako')

            buf = StringIO()
            ctx = Context(buf, **request.POST)
            mytemplate.render_context(ctx)
            # '/tmp/'
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="zwolnienie indywidualne.pdf"'

            html = HTML(string=buf.getvalue())
            html.write_pdf(response, stylesheets=[CSS('Documents/html&css/style.css')])
            return response
    else:
        form = DocsForm(instance=doc)
    return render(request, 'documents/zwolnienie_edit.html', {'form': form})
##########################################################################################################
def zwolnienie_generate(request, pk):
    doc = get_object_or_404(Docs,pk=pk)
    form = DocsForm(request.POST, instance=doc)

    mytemplate = Template(filename='Documents/html&css/zwolnienie.mako')

    buf = StringIO()
    ctx = Context(buf, **request.POST)
    mytemplate.render_context(ctx)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="zwolnienie indywidualne.pdf"'

    html = HTML(string=buf.getvalue())
    html.write_pdf(response, stylesheets=[CSS('Documents/html&css/style.css')])

    return response
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

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Podanie o patronat.pdf"'

            html = HTML(string=buf.getvalue())
            html.write_pdf(response, stylesheets=[CSS('Documents/html&css/style.css')])
            return response
    else:
        form = DocsForm()
    return render(request, 'documents/patron_edit.html', {'form': form})
###########################################################################################################
def patron_edit(request, pk):
    doc = get_object_or_404(Docs,pk=pk)
    if request.method == "POST":
        form = DocsForm(request.POST, instance=doc)
        if form.is_valid():
            doc = form.save(commit=False)
            doc.publication_date = timezone.now()
            doc.form_type = 2
            doc.save()

            mytemplate = Template(filename='Documents/html&css/patron.mako')

            buf = StringIO()
            ctx = Context(buf, **request.POST)
            mytemplate.render_context(ctx)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="Podanie o patronat.pdf"'

            html = HTML(string=buf.getvalue())
            html.write_pdf(response, stylesheets=[CSS('Documents/html&css/style.css')])
            return response
    else:
        form = DocsForm(instance=doc)
    return render(request, 'documents/patron_edit.html', {'form': form})
###########################################################################################################
def patron_generate(request, pk):
    doc = get_object_or_404(Docs,pk=pk)
    form = DocsForm(request.POST, instance=doc)

    mytemplate = Template(filename='Documents/html&css/patron.mako')

    buf = StringIO()
    ctx = Context(buf, **request.POST)

    import pdb; pdb.set_trace()

    mytemplate.render_context(ctx)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Podanie o patronat.pdf"'

    html = HTML(string=buf.getvalue())
    html.write_pdf(response, stylesheets=[CSS('Documents/html&css/style.css')])

    return response
###########################################################################################################
def docs_remove(request, pk):
    docs = get_object_or_404(Docs,pk=pk)
    docs.delete()
    return redirect('Documents.views.docs_list')
###########################################################################################################
def docs_edit(request, pk):
    doc = get_object_or_404(Docs, pk=pk)
    if doc.form_type == '1':
        return redirect('Documents.views.zwolnienie_edit', pk=doc.pk)
    else:
        if doc.form_type == '2':
            return redirect('Documents.views.patron_edit', pk=doc.pk)
###########################################################################################################
def docs_generate(request, pk):
    doc = get_object_or_404(Docs, pk=pk)
    if doc.form_type == '1':
        return redirect('Documents.views.zwolnienie_generate', pk=doc.pk)
    else:
        if doc.form_type == '2':
            return redirect('Documents.views.patron_generate', pk=doc.pk)
##########################################################################################################
def docs_list(request):
    docs = Docs.objects.all
    return render(request, 'documents/docs_list.html', {'docs':docs})
###########################################################################################################