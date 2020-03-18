from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    projects = Project.objects.all()
    department_time = Department.objects.all()
    return render(request, 'accounts/dashboard.html', {'projects':Project, "department":Department, "employee": Employee} )

def contact(request):
    return render(request, 'accounts/products.html')

def users(request):
    return render(request, 'accounts/customer.html')
# Create your views here.
