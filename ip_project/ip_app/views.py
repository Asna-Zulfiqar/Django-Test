from django.shortcuts import render , HttpResponse
from .decorators import  ip_decorator

def local(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        user_ip = user_ip.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')
    print(user_ip)
    if user_ip == '127.0.0.1':
        return HttpResponse('Page accesible by Local Ip')
    else:
        return HttpResponse('Access Denied: Local Ip')
    
def live(request):
    user_ip = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip:
        user_ip = user_ip.split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')
    print(user_ip)
    if user_ip != '127.0.0.1':
        return HttpResponse('Page accesible by Live Ip')
    else:
        return HttpResponse('Access Denied: Live Ip')
    
def local_page(request):
    return HttpResponse('Page accesible by Local Ip')

def live_page(request):
    return HttpResponse('Page accesible by Live Ip')

@ip_decorator
def local_page_view(request):
    return HttpResponse('Page accesible by Local Ip')

@ip_decorator
def live_page_view(request):
    return HttpResponse('Page accesible by Live Ip')



