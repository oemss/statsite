from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
# Create your views here.
from django.template.context_processors import csrf
from django.urls import reverse
from django import forms
from .forms import UploadFileForm
from stats.forms import DocumentForm
from django.core.files.storage import FileSystemStorage
import worker.main as main_f

def main_page(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        main_f.__main__(uploaded_file_url)
        return render(request, 'stats/main_page.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'stats/main_page.html')


def handle_uploaded_file(f):
    with open('media/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
