from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('accounts/', views.contact),
    path('users/', views.users),

]