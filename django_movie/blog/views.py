from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def posts_list(reguest):
    return HttpResponse("<h1>Hello world</h1>")