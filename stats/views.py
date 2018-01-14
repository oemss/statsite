from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
# Create your views here.
from django.template.context_processors import csrf
from django.urls import reverse
from django import forms
from .forms import UploadFileForm


def main_page(request):
    return render(request, 'stats/main_page.html', {})


def handle_uploaded_file(f):
    with open('media/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def submit(request):
    # Если метод POST
    if request.method == 'POST':
        # Заполняем форму полученными данными
        form = UploadFileForm(request.POST, request.FILES)
        # Если данные валидны
        print("asdasdas")
        print(form.errors)
        if form.is_valid():
            # обрабатываем файл
            print("dsad")
            handle_uploaded_file(request.FILES)
            # перенаправляем на другую страницу
            return HttpResponseRedirect('admin')
    # Если другой метод (обычно GET)
    else:
        form = UploadFileForm()
    # Выводим форму загрузки
    return redirect('/')

