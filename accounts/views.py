from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    projects = Project.objects.all()
    department_time = Department.objects.all()
    return render(request, 'accounts/dashboard.html', {'projects':Project, "department":Department, "employee": Employee} )

def contact(request):
    return render(request, 'accounts/products.html')

def timesheet(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    dep_projects = Department.objects.all()
    projects = dep_projects.filter(department_name=employee.department_name)
    # dep_info = Department.objects.all()
    # projects = dep_info.manager_name
    information = {'employee':employee, 'projects':projects}
    return render(request, 'accounts/report.html', information)
# Create your views here.
