from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('accounts/', views.contact),
    path('timesheet/<str:emp_id>/', views.timesheet),

]