from django.http import HttpResponse

def index(request):
    return HttpResponse("¯\_( ͡❛ ͜ʖ ͡❛)_/¯")

def about(request):
    return HttpResponse("┏( ͡❛ ͜ʖ ͡❛)┛")

