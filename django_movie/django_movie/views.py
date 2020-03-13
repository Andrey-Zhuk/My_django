from django.http import HttpResponse

def hello(reguest):
    return HttpResponse("<h1>Hello world</h1>")