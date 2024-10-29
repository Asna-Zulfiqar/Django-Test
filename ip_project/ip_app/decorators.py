from functools import wraps
from django.http import HttpResponse

def ip_decorator(function):
    @wraps(function)
    def wrap(request , *args , **kwargs):
        user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip:
            user_ip = user_ip.split(',')[0]
        else:
            user_ip = request.META.get('REMOTE_ADDR')
        if user_ip == '127.0.0.1':
            return function(request , *args , **kwargs)
        elif user_ip != '127.0.0.1':
            return function(request , *args , **kwargs)
        else:
            return HttpResponse("Access Denied")
    return wrap

