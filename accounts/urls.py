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
    path('timesheetEntry_extended/', views.timesheetEntry_extended),
    path('', views.Login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('new_project/', views.newProject, name='new_project'),
    path('assign_time/', views.department, name='department'),
    path('view_ts/', views.viewTimesheet, name='viewTS'),
    path('department_assignment/', views.department_assignment, name='dep_assignment'),
    path('bool_change/',  views.bool_department),
    path('mytimesheets/', views.mytimesheets, name='mytimesheet'),
    path('approve_ts/<str:pk>/<str:week>/<str:year>/', views.approveTimesheet, name='approveTS'),
    path('confirm_ts/<str:pk>/<str:week>/<str:year>/', views.confirmTS, name='confirmTS'),
    path('confirm_ts_ext/<str:pk>/<str:week>/<str:year>/', views.confirmTS_ext, name='confirmTS_ext'),
    path('reject_ts/<str:pk>/<str:week>/<str:year>/', views.rejectTS, name='rejectTS'),
    path('selectEmp/', views.selectEmp, name='selectEmployee'),
    path('extendedhours/<str:pk>/', views.extended_hours, name='extended'),
    path('checkweek/<str:week>/<str:year>/', views.checkweek),
    path('success/', views.success, name='success'),
    path('create_activity/', views.create_activity, name='create_activity'),
    path('delete_activity/<str:pk>/', views.delete_activity, name='delete_activity'),
    path('viewprojects/', views.viewprojects, name='viewprojects'),
    path('project/<str:pk>/', views.project, name='project'),
    path('dept_wise/<str:pk>/', views.dept_wise, name='deptwise'),
    path('act_wise/<str:pk>/', views.act_wise, name='actwise'),
    path('project_employee/<str:pk>/', views.projectEmployee, name='project_employee'),
    path('profile/notifications/', views.notifications_view, name='notifications')
]