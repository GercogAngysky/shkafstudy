import types
from django.conf import settings
from django.views.generic import View
from django.shortcuts import redirect

def login_required(entity, redirect_url=settings.LOGIN_URL):
	def function_wraper(request, *args, **kwargs):
		user = request.user
		if user.is_authenticated:
			return entity(request, *args, **kwargs)
		return redirect(redirect_url) 

	def class_wraper(self, request, *args, **kwargs):
		user = request.user
		if user.is_authenticated:
			return super(self.__class__, self).dispatch(request, *args, **kwargs)
		return redirect(redirect_url)

	if isinstance(entity,  types.FunctionType):
		return function_wraper
	elif issubclass(entity, View):
		entity.dispatch = class_wraper
		return entity

