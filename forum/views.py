from django.shortcuts import render
from django.http import HttpResponse


def home1(request):
    return HttpResponse('<h2>тут тоже</h2>')


def home2(request):
    return HttpResponse('<h2>Класно получилось</h2>')

