from http.client import HTTPResponse
from django.shortcuts import redirect, HttpResponse


# def allowed_user(roles=[]):
#     def decorator(view_fun):
#         def wrapper_func(request, *args, **kwargs):

#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#                 print(group)
#             if group == roles:
#                 return view_fun(request, *args, **kwargs)
#             else:
#                 # return redirect('/user/')
#                 return HttpResponse('You are not authorised to access this page')
#         return wrapper_func
#     return decorator

def allowed_user(roles=[]):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):

			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			if group in roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func
	return decorator
