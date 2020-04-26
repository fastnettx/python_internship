from django.shortcuts import render
from django.http import HttpResponse
import datetime


def index(request):
    return render(request, 'index.html')


def static(request):
    return HttpResponse('You should see static text!')


def dynamic(request, dynamic_url):
    return HttpResponse('Your entered URL - ' + dynamic_url)
