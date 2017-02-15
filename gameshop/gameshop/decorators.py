from django.http import HttpResponse

def require_api_key(function):
    def wrap(request, *args, **kwargs):
        if request.META['HTTP_API_KEY'] != None:
            return function(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorized', status=401)
    return wrap
