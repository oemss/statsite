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
            form.save()
            myfile = request.FILES
            print("DSDSDSDDDDDDDDDDDDDDDDDDDDDDDDDD ")
            print(request.FILES.name)
            # main_f.__main__(str(myfile['upload']))
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'stats/main_page.html', {
        'form': form
    })
