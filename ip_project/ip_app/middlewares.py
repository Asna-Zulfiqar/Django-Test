from django.http import HttpResponse

class CustomIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
    
        if request.META['REMOTE_ADDR'] == '127.0.0.1':
            return self.get_response(request)
        elif request.META['REMOTE_ADDR'] != '127.0.0.1':
            return self.get_response(request)
        else:
            return HttpResponse("Access denied.")