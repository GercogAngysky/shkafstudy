from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from .models import Employee

class EmployeeLogin(LoginView):
	model = Employee
	template_name='registration/login.html'
	# redirect_field_name = reverse_lazy('home')

class EmployeeLogout(LogoutView):
	model = Employee
	template_name='registration/logged_out.html'
	# redirect_field_name = reverse_lazy('home')
