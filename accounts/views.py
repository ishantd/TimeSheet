from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home Page')

def contact(request):
    return HttpResponse('Contact Page')

def users(request):
    return HttpResponse('Customer Page')
# Create your views here.
