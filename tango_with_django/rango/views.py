from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world!")

def about(request):
    response = "Rango says Here is the about page <a href='/rango'>Index</a>"
    return HttpResponse(response)
