from django.http import HttpResponse
from django.shortcuts import redirect, render

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                groups = request.user.groups.all()

            for group in groups:
                if group.name in allowed_roles:
                    return view_func(request, *args, **kwargs)

            return render(request, 'accounts/error2.html', status=401)
        return wrapper
    return decorator