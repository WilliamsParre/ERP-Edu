from http.client import HTTPResponse
from django.shortcuts import redirect, HttpResponse


def allowed_user(roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('<h1 style="color:red;text-align:center;">You are not authorized to view this page</h1>')
        return wrapper_func
    return decorator
