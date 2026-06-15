from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),

    path('register/', views.register_view, name='register'),

    path(
        'hr-dashboard/',
        views.hr_dashboard,
        name='hr_dashboard'
    ),

    path(
        'manager-dashboard/',
        views.manager_dashboard,
        name='manager_dashboard'
    ),

    path(
        'employee-dashboard/',
        views.employee_dashboard,
        name='employee_dashboard'
    ),
    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),
]