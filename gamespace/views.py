from django.http import HttpResponse
from django.shortcuts import render
from . import views


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    # return HttpResponse('about.html')
    return render(request, 'about.html')
