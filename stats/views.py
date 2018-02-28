import os
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.urls import reverse
from django import forms
from stats.forms import DocumentForm
from django.core.files.storage import FileSystemStorage
import worker.main as main_f
import pprint
from stats.models import analyz


def main_page(request):
    # s = request.session()
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
            request.session['src_url'] = os.sep + 'media' + os.sep + result_url
            request.session['log_url'] = os.sep + 'media' + os.sep + result_url.replace('.', '_log.')
            request.session['res_url'] = os.sep + 'media' + os.sep + result_url.replace('.', '_res.')
            request.session['out_url'] = os.sep + 'media' + os.sep + result_url.replace('.', '_out.')
            # return redirect('/')
            # print(analyz.object.all())
            f.addfiles()
            return redirect('stats/result.html')
    else:
        form = DocumentForm()
    return render(request, 'stats/main_page.html', {
        'form': form
    })


def result(request):
    if "src_url" in request.session:
        src_ulr = request.session['src_url']
        log_url = request.session['log_url']
        res_url = request.session['res_url']
        out_url = request.session['out_url']
        del request.session['src_url']
        del request.session['log_url']
        del request.session['res_url']
        del request.session['out_url']
        return render(request, 'stats/result.html', {'src_url': src_ulr,
                                                     'log_url': log_url,
                                                     'res_url': res_url,
                                                     'out_url': out_url})
    else:
        return render(request, 'stats/result.html')


def get_db(request):
    test = analyz.objects.all()
    return