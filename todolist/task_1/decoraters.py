import functools
from django.shortcuts import redirect

def signin_required(view_func, redirect_url="display"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return view_func(request,*args, **kwargs)
        return redirect(redirect_url)
    return wrapper