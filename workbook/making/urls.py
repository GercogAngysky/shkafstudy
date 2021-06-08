from django.urls import path
from . import views


urlpatterns = [
	path('employee/login', views.EmployeeLogin.as_view(), name = 'login'),
	path('employee/logout', views.EmployeeLogout.as_view(), name = 'logout'),
]