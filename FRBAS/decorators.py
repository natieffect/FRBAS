from django.shortcuts import redirect

def is_loged_in(function):
    def wrap(request, *args, **kwargs):
        if request.session.get('user_email',False):
            return redirect('employee:home')      
        else:
            return function(request, *args, **kwargs)
    return wrap

def is_loged_out(function):
    def wrap(request, *args, **kwargs):
        if request.session.get('user_email',False):
            return function(request, *args, **kwargs)       
        else:
             return redirect('employee:signIn')   
    return wrap