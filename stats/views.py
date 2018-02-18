import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
# Create your views here.
from django.template.context_processors import csrf
from django.urls import reverse
from django import forms
from stats.forms import DocumentForm
from django.core.files.storage import FileSystemStorage
import worker.main as main_f


import pprint

from stats.models import analyz


def main_page(request):
    # if request.method == 'POST' and request.FILES['myfile']:
    #     myfile = request.FILES['myfile']
    #     fs = FileSystemStorage()
    #     filename = fs.save(myfile.name, myfile)
    #     uploaded_file_url = fs.url(filename)
    #     main_f.__main__(uploaded_file_url)
    #     return render(request, 'stats/main_page.html', {
    #         'uploaded_file_url': uploaded_file_url
    #     })
    # return render(request, 'stats/main_page.html')
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            f = form.save()
            result_url = f.filename()
            main_f.__main__(result_url)
            request.session['src_url'] = '/media/' + result_url
            request.session['log_url'] = '/media/' + result_url.replace('.', '_log.')
            request.session['res_url'] = '/media/' + result_url.replace('.', '_res.')
            request.session['out_url'] = '/media/' + result_url.replace('.', '_out.')
            # return redirect('/')
            f.addfiles()
            return redirect('stats/result.html')
    else:
        form = DocumentForm()
    return render(request, 'stats/main_page.html', {
        'form': form
    })


def result(request):
    return render(request, 'stats/result.html', {'src_url': request.session['src_url'],
                                                 'log_url': request.session['log_url'],
                                                 'res_url': request.session['res_url'],
                                                 'out_url': request.session['out_url']})


def get_db(request):
    test = analyz.objects.all()
    return