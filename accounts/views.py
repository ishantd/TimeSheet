from django.shortcuts import render, redirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import User, Group
from django.forms import inlineformset_factory
from django.http import QueryDict


@login_required(login_url='/')
def home(request):
    projects = Project.objects.all()
    department_time = Department.objects.all()
    return render(request, 'accounts/dashboard.html', {'projects':Project, "department":Department, "employee": Employee} )

@login_required(login_url='/')
def contact(request):
    return render(request, 'accounts/products.html')

@login_required(login_url='/')
def timesheet(request):
    employee = Employee.objects.get(employee_id=request.user.employee.employee_id)
    dep_projects = Department.objects.all()
    projects = dep_projects.filter(department_name=request.user.employee.department_name)
    information = {'employee':employee, 'projects':projects}
    return render(request, 'accounts/report.html', information)

@login_required(login_url='/')
@allowed_users(allowed_roles=['planning_dept'])
def create(request):
    return render(request, 'accounts/create.html')

@login_required(login_url='/')
def createEmployee(request):
    context = {'form': SignupForm}
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.employee.employee_id = form.cleaned_data.get('employee_id')
            user.employee.name = form.cleaned_data.get('name')
            user.employee.phone = form.cleaned_data.get('phone')
            user.employee.email = form.cleaned_data.get('email')
            user.employee.date_created = datetime.now()
            user.employee.department_name = form.cleaned_data.get('department_name')
            user.employee.manager = Employee.objects.get(employee_id =form.cleaned_data.get('manager'))
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('dashboard')
        else:
            print("FORM DATA NOT VALID")      
            # user.employee.employee_id = form.cleaned_data.get('employee_id')
    return render(request, 'accounts/create_employee.html', context)

@login_required(login_url='/')
def viewEmployees(request):
    employees = Employee.objects.all()
    data = {'employees': employees}
    return render(request, 'accounts/view_employees.html', data)

@login_required(login_url='/')
def updateEmployee(request, pk):
    employee = Employee.objects.get(employee_id=pk)
    context = {}
    return render(request, 'accounts/create_employee.html', context)

@login_required(login_url='/')
@csrf_exempt
def timesheetEntry(request):
    # form = ReportForm()
    ProjectObject = ''
    if request.method == 'POST':
        data = request.POST
        print(data['project'])
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
                    
    return HttpResponse("YESY")

@unauthenticated_user
def Login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
            
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or password is incorrect.')
            
    return render(request, 'accounts/login.html', context)
            
    context = {}
    return render (request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def newProject(request):
    form = ProjectForm()
    context = {'form': form}
    
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            print("SUCCESS")
        else:
            print("ERROR")
    return render (request, 'accounts/newProject.html', context)

def department(request):
    employee = request.user.employee
    projects = Project.objects.filter(project_manager=employee)
    deps = DepInfo.objects.all()
    for dep in deps:
        dep.department_name = dep.department_name + ',' + (dep.department_name.replace(' ', '')).lower()
        dep.department_name = dep.department_name.split(",")
    
    print(deps)
    # print(projects)   
    context = {'projects': projects, 'deps': deps}
    
    
    return render (request, 'accounts/department_assignment.html', context)

def viewTimesheet(request):
    reports = Report.objects.filter(employee__manager__employee_id=request.user.employee.employee_id)
    current_employee = ''
    employeeReports = []
    for i in range(0, reports.count()):
        if (reports[i].employee == current_employee):
            continue
        else:
            current_employee = reports[i].employee
            employeeReports.append(reports[i])
    context = {'reports': employeeReports}
    
    return render(request, 'accounts/view_ts.html', context)


@login_required(login_url='/')
@csrf_exempt
def department_assignment(request):
    if request.method == 'POST':
        data = request.POST
        ProjectObject = Project.objects.get(project_id=data['project_assigned'])
        depObject = DepInfo.objects.get(department_name=data['department_name'])
        print("DEBUG", depObject, data['department_name'])
        assign_dep = Department(
            department_name=depObject,
            project_assigned=ProjectObject,
            time_allocated=data['time_allocated'],
            time_left=data['time_left']
        )
        
        assign_dep.save()
        print("Department wise time saved!")
        
        
    return redirect("dep_assignment", status=200)

@login_required(login_url='/')
@csrf_exempt
def bool_department(request):
    if request.method == 'POST':
        data = request.POST
        ProjectObject = Project.objects.get(project_id=data['project'])
        ProjectObject.department_assigned = True
        ProjectObject.save()        
        print("Bool object in project department changed!")
    return HttpResponse('BoolChanged', status=200)

@login_required(login_url='/')
def approveTimesheet(request, pk, week, year):
    employee = Employee.objects.get(employee_id=pk)
    if (request.user != employee.manager.user):
        return render(request, 'accounts/error.html', status=401)
    reports = Report.objects.filter(employee=employee, week=week, year=year)
    report_info = reports[0]
    for report in reports:
        report.everyday_hours = report.everyday_hours.split(",") 
    context = {'reports': reports, 'employee': employee, 'report_info': report_info}
    return render(request, 'accounts/approve_ts.html', context)
 
@login_required(login_url='/')   
def confirmTS(request, pk, week, year):
    employee = Employee.objects.get(employee_id=pk)
    if (request.user != employee.manager.user):
        return HttpResponse('Unauthorized', status=401)
    reports = Report.objects.filter(employee=employee, week=week, year=year)
    for report in reports:
        report.approved = True
        report.save()
    return redirect('viewTS')

@login_required(login_url='/')   
def rejectTS(request, pk, week, year):
    employee = Employee.objects.get(employee_id=pk)
    if (request.user != employee.manager.user):
        return HttpResponse('Unauthorized', status=401)
    reports = Report.objects.filter(employee=employee, week=week, year=year)
    for report in reports:
        report.rejected = True
        report.approved = False
        report.save()
    return redirect('viewTS')

@login_required(login_url='/')
def mytimesheets(request):
    
    context = {}
    
    return render(request, 'mytimesheets.html', context)

@login_required(login_url='/')
@allowed_users(allowed_roles=['hod'])
def selectEmp(request):

    context = {}


    return render(request, 'accounts/selectEmp', context)



