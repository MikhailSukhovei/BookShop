from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return HttpResponse("<h4>Страница контактов и связей</h4>")

def catalog(request):
    return HttpResponse("<h4>Страница каталога</h4>")