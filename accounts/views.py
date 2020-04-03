from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
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
        print("PRINT DATA:", request.POST)
        form = EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'accounts/create_employee.html', context)

def viewEmployees(request):
    employees = Employee.objects.all()
    data = {'employees': employees}
    return render(request, 'accounts/view_employees.html', data)

def updateEmployee(request, pk):
    employee = Employee.objects.get(employee_id=pk)
    form = EmployeeForm(instance=employee)
    context = {'form': form}
    return render(request, 'accounts/create_employee.html', context)


@csrf_exempt
def timesheetEntry(request):
    # form = ReportForm()
    ProjectObject = ''
    if request.method == 'POST':
        data = request.POST
        EmployeeObject = Employee.objects.get(employee_id=data['employee'])
        ProjectObject = Project.objects.get(project_id=data['project']) 
        DepartmentObject = Department.objects.get(department_name=data['department_name'])

        create_report = Report(employee=EmployeeObject,
                               project=ProjectObject,
                               activity=data['activity'],
                               department_name=DepartmentObject,
                               everyday_hours=data['everyday_hours'],
                               hours_reported=data['hours_reported'],
                               week=data['week'],
                               year=data['year'])
        create_report.save()
        
        if (data['project']!='0'):
            total_time = DepartmentObject.time_left
            DepartmentObject.time_left = total_time - int(data['hours_reported'])
            DepartmentObject.save()
            
    return HttpResponse("YESY")
# Create your views here.
