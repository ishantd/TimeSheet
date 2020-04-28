from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.home, name='dashboard'),
    path('accounts/', views.contact),
    path('timesheet/', views.timesheet, name='report'),
    path('create/', views.create),
    path('create_employee/', views.createEmployee, name="create_employee"),
    path('view_employees/', views.viewEmployees, name='view_employees'),
    path('update_employee/<str:pk>/', views.updateEmployee, name='update_employee'),
    path('timesheetEntry/', views.timesheetEntry),
    path('', views.Login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('new_project/', views.newProject, name='new_project'),
    path('assign_time/', views.department, name='department'),
    path('view_ts/', views.viewTimesheet, name='viewTS'),
    path('department_assignment/', views.department_assignment, name='dep_assignment'),
    path('bool_change/',  views.bool_department),
    path('approve_ts/<str:pk>/<str:week>/<str:year>/', views.approveTimesheet, name='approveTS'),
    path('confirm_ts/<str:pk>/<str:week>/<str:year>/', views.confirmTS, name='confirmTS'),
    path('reject_ts/<str:pk>/<str:week>/<str:year>/', views.rejectTS, name='rejectTS'),
    path('selectEmp/', views.selectEmp, name='selectEmployee')
]