from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    tasks = Tasks.objects.all()
    assigned_to = Tasks_Assignment.objects.all()
    return render(request, 'accounts/dashboard.html', {'tasks':tasks, "assigned_to":assigned_to})

def contact(request):
    return render(request, 'accounts/products.html')

def users(request):
    return render(request, 'accounts/customer.html')
# Create your views here.
