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
from notifications.signals import notify
import json


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
    projects = employee.department_set.all()
    activitys = Activity.objects.filter(department_info = request.user.employee.department_info)
    information = {'employee':employee, 'projects':projects, 'activitys':activitys}
    return render(request, 'accounts/report.html', information)

@login_required(login_url='/')
@allowed_users(allowed_roles=['planning_dept', 'hod'])
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
    employees = Employee.objects.filter(department_info = request.user.employee.department_info)
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
    if request.method == 'POST':
        data = request.POST
        print(data['activity'])
        EmployeeObject = Employee.objects.get(employee_id=request.user.employee.employee_id)
        ProjectObject = Project.objects.get(project_id=data['project'])
        dep_info = DepInfo.objects.get(department_name=request.user.employee.department_info.department_name)
        act = Act.objects.get(name=data['activity'])
        activityObject = Activity.objects.get(name=act, department_info = dep_info)
        DepartmentObject = Department.objects.get(department_name=dep_info, project_assigned=ProjectObject )

        create_report = Report(employee=EmployeeObject,
                               project=ProjectObject,
                               activity=activityObject,
                               department_name=DepartmentObject,
                               everyday_hours=data['everyday_hours'],
                               hours_reported=data['hours_reported'],
                               week=data['week'],
                               year=data['year'],
                               complete=True)
        create_report.save()
        print(create_report)                    
    return render(request, 'accounts/success.html', status=200)

@login_required(login_url='/')
@csrf_exempt
def timesheetEntry_extended(request):
    if request.method == 'POST':
        data = request.POST
        print(data)
        EmployeeObject = Employee.objects.get(employee_id=request.user.employee.employee_id)
        ProjectObject = Project.objects.get(project_id=data['project'])
        dep_info = DepInfo.objects.get(department_name=request.user.employee.department_info.department_name)
        activityObject = Activity.objects.get(name=data['activity'], department_info = dep_info)
        DepartmentObject = Department.objects.get(department_name=dep_info, project_assigned=ProjectObject )
        reports = Report.objects.filter(employee=EmployeeObject, week=data['week'], year=data['year'])
        create_report = Report_extended(employee=EmployeeObject,
                               project=ProjectObject,
                               activity=activityObject,
                               department_name=DepartmentObject,
                               everyday_hours=data['everyday_hours'],
                               hours_reported=data['hours_reported'],
                               week=data['week'],
                               year=data['year'])
        create_report.save()
        for report in reports:
            report.extended_hours = True
            report.save()    
        print(create_report, "EXTENDED")
                    
    return render(request, 'accounts/success.html', status=200)

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

@login_required(login_url='/')
def newProject(request):
    form = ProjectForm()
    context = {'form': form}
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            project = Project.objects.last()
            notify.send(request.user, recipient=User.objects.all(), verb='created a project', level='info', action_object=project)
            return render(request, 'accounts/success.html')
    return render (request, 'accounts/newProject.html', context)

@login_required(login_url='/')
def department(request):
    employee = request.user.employee
    projects = Project.objects.filter(project_manager=employee, department_assigned=False)
    deps = DepInfo.objects.all()
    for dep in deps:
        dep.department_name = dep.department_name + ',' + (dep.department_name.replace(' ', '')).lower()
        dep.department_name = dep.department_name.split(",")   
    context = {'projects': projects, 'deps': deps}
    
    return render (request, 'accounts/department_assignment.html', context)

@login_required(login_url='/')
def viewTimesheet(request):
    reports = Report.objects.filter(employee__manager__employee_id=request.user.employee.employee_id)
    current_employee = ''
    current_week = ''
    employeeReports = []
    for i in range(0, reports.count()):
        if (reports[i].employee == current_employee and reports[i].week == current_week):
            continue
        else:
            current_employee = reports[i].employee
            current_week = reports[i].week
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

        return redirect("dep_assignment")
    return redirect("dep_assignment")

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
    reports_ext = Report_extended.objects.filter(employee=employee, week=week, year=year)
    report_info = reports[0]
    for report in reports:
        report.everyday_hours = report.everyday_hours.split(",")
    if reports_ext:
        for report in reports_ext:
            report.everyday_hours = report.everyday_hours.split(",")
        context = {'reports': reports, 'reports_ext': reports_ext, 'employee': employee, 'report_info': report_info}
    else:
        context = {'reports': reports, 'employee': employee, 'report_info': report_info}
    return render(request, 'accounts/approve_ts.html', context)
 
@login_required(login_url='/')   
def confirmTS(request, pk, week, year):
    employee = Employee.objects.get(employee_id=pk)
    if (request.user != employee.manager.user):
        return HttpResponse('Unauthorized', status=401)
    reports = Report.objects.filter(employee=employee, week=week, year=year)
    for report in reports:
        dep = Department.objects.get(department_name = employee.department_info, project_assigned=report.project)
        report.approved = True 
        dep.time_left = dep.time_left - report.hours_reported
        dep.save()
        report.save()
    return redirect('viewTS')

@login_required(login_url='/')   
def confirmTS_ext(request, pk, week, year):
    employee = Employee.objects.get(employee_id=pk)
    if (request.user != employee.manager.user):
        return HttpResponse('Unauthorized', status=401)
    reports = Report.objects.filter(employee=employee, week=week, year=year)
    reports_ext = Report_ext.objects.filter(employee=employee, week=week, year=year)
    for report in reports:
        dep = Department.objects.get(department_name = employee.department_info, project_assigned=report.project)
        report.approved = True 
        dep.time_left = dep.time_left - report.hours_reported
        dep.save()
        report.save()
    for report in reports_ext:
        dep = Department.objects.get(department_name = employee.department_info, project_assigned=report.project)
        report.approved = True 
        dep.time_left = dep.time_left - report.hours_reported
        dep.save()
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
    reports = Report.objects.filter(employee=request.user.employee)
    reports_ext = Report_extended.objects.filter(employee=request.user.employee)
    current_week = ''
    current_year = ''
    employeeReports = []
    for i in range(0, reports.count()):
        if (reports[i].week == current_week and reports[i].year == current_year ):
            continue
        else:
            current_week = reports[i].week
            current_year = reports[i].year
            employeeReports.append(reports[i])
    print(employeeReports)
    context = {'reports': employeeReports}
    
    return render(request, 'accounts/mytimesheets.html', context)

@csrf_exempt
@login_required(login_url='/')
@allowed_users(allowed_roles=['hod'])
def selectEmp(request):
    dep_info = DepInfo.objects.get(department_name=request.user.employee.department_info.department_name)
    project_deps = Department.objects.filter(department_name = dep_info, emp_assigned=False)
    employees_db = Employee.objects.filter(department_info = dep_info)
    if request.method == 'POST':
        data = request.POST
        employees = data['employees'].split(',')
        project = ''
        for dep in project_deps:
            if dep.project_assigned.project_id == int(data['project']):
                project = dep
        for employee in employees:
            employee = int(employee)
            for emp in employees_db:
                if emp.employee_id == employee:
                    project.assigned_to.add(emp)
        project.emp_assigned = True
        project.save()
        return render(request, 'accounts/success.html')

    context = {'projects': project_deps, 'employees': employees_db}
    return render(request, 'accounts/selectEmp.html', context)


@csrf_exempt
@login_required(login_url='/')
@allowed_users(allowed_roles=['hod'])
def extended_hours(request, pk):
    employee = Employee.objects.get(employee_id=pk)
    if request.user.employee.department_info != employee.department_info:
        return HttpResponse('Unauthorized', status=401)
    if employee.extended_hours:
        employee.extended_hours = False
        employee.save()
    else:
        employee.extended_hours = True
        employee.save()
    return redirect('view_employees')

@login_required(login_url='/')
def checkweek(request, week, year):
    employee = Employee.objects.get(employee_id=request.user.employee.employee_id)
    reports = Report.objects.filter(employee=employee, week=week, year=year)
    if reports:
        return HttpResponse('already_filled', status=200)
    else:
        return HttpResponse('no_content', status=200)

@login_required(login_url='/')
def success(request):

    return render(request, 'accounts/success.html')



@login_required(login_url='/')
@allowed_users(allowed_roles=['planning_dept'])
def create_activity(request):
    form = ActivityForm()
    acts = Act.objects.all()
    context = {'form': form, 'acts': acts}

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            act = Act.objects.last()
            notify.send(request.user, recipient=User.objects.all(), verb='created an activity', level='info', action_object=act)
        return redirect('create_activity')
            

    return render(request, 'accounts/create_activity.html', context)
    
@login_required(login_url='/')
@allowed_users(allowed_roles=['planning_dept'])
def delete_activity(request, pk):
    act = Act.objects.get(id=pk)
    act.delete()
    return redirect('create_activity')


@login_required(login_url='/')
def viewprojects(request): 
    projects = Project.objects.exclude(name='Holiday/Leave')
    context = {'projects': projects}

    return render(request, 'accounts/viewprojects.html', context)

@login_required(login_url='/')
def project(request, pk):
    project = Project.objects.get(project_id=pk)

    context = {'project': project}

    return render(request, 'accounts/project.html', context)

@login_required(login_url='/')
def dept_wise(request, pk):
    project = Project.objects.get(project_id=pk)
    depts = Department.objects.filter(project_assigned=project)
    labels = []
    time_all = []
    time = []
    for dept in depts:
        name = dept.department_name.department_name
        t1 = dept.time_allocated
        t2 = dept.time_left

        time_all.append(t2)
        time.append(t1-t2) 
        labels.append(name)
    x = {
        "department_names": labels,
        "time_allocated": time_all,
        "time_reported": time
    }

    data = json.dumps(x)

    return HttpResponse(data, status=200)

@login_required(login_url='/')
def act_wise(request, pk):
    labels = []
    time = []
    acts = Activity.objects.filter(department_info=request.user.employee.department_info)
    
    dep = Department.objects.get(department_name=request.user.employee.department_info, project_assigned=pk)

    reports = Report.objects.filter(project=pk, department_name=dep)
    
    for act in acts:
        name = act.name.name
        labels.append(name)
        act_sum = 0
        for report in reports:
            if report.activity == act:
                act_sum = act_sum + report.hours_reported
        time.append(act_sum)

    x = {
        "activity_names": labels,
        "activity_time": time
    }

    data = json.dumps(x)

    return HttpResponse(data, status=200)

@login_required(login_url='/')
@allowed_users(allowed_roles=['hod'])
def projectEmployee(request, pk):
    project = Project.objects.get(project_id=pk)
    dep = Department.objects.get(department_name =request.user.employee.department_info, project_assigned=project)
    assigned_employees = dep.assigned_to.all()
    employees = Employee.objects.filter(department_info = request.user.employee.department_info).exclude(employee_id__in=assigned_employees)
    context = {'employees': employees, 'assigned_employees': assigned_employees}
    if request.method == "POST":
        data = request.POST
        selected = data.getlist('employee')
        assigned = []
        final = []
        for ax in assigned_employees:
            assigned.append(ax.employee_id) 
        selected = [int(i) for i in selected]
        to_add = (set(selected).difference(assigned))
        to_delete = (set(assigned).difference(selected))
        if to_add:
            for emp in to_add:
                dep.assigned_to.add(emp)
            dep.save()

        if to_delete:
            for emp in to_delete:
                dep.assigned_to.remove(emp)
            dep.save()
        return render(request, 'accounts/success.html')

        
    return render(request, 'accounts/projectEmployees.html', context)

@login_required(login_url='/')
def notifications_view(request):
    notifications = request.user.notifications.unread()   
    context = {'notifications': notifications}

    return render(request, 'accounts/notifications.html', context)

@login_required(login_url='/')
def reports_index(request):
    context = {}

    return render(request, 'accounts/reports/index.html', context)

@login_required(login_url='/')
def create_notification(request):

    return HttpResponse("success", status=200)

@login_required(login_url='/')
def projects_all(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'accounts/reports/projects/all.html', context)