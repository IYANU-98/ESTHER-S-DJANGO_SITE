from django.http import HttpResponse

def hello_world_view(request):
    return HttpResponse("Hello World! This is controlled by my new 'home' app.")
