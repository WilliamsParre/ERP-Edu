from django.shortcuts import redirect
from django.contrib.auth.models import Group


def allowed_user(roles=[]):
    def decorator(view_fun):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                print(group)

            if group in roles:
                return view_fun(request, *args, **kwargs)
            else:
                return redirect('/user/')
        return wrapper_func
    return decorator
