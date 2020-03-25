from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

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

def create(request):
    return render(request, 'accounts/create.html')

def createEmployee(request):
    form = EmployeeForm()
    context = {'form': form}
    if request.method == 'POST':
        # print("PRINT DATA:", request.POST)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/create_employee.html', context)

def viewEmployees(request):
    employees = Employee.objects.all()
    data = {'employees': employees}
    return render(request, 'accounts/view_employees.html', data)
# Create your views here.
