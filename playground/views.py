from django.shortcuts import render
from django.http import HttpResponse


def empty_parameter(request):
    return render(request, 'index.html')

def say_hello(request):
    return HttpResponse("imekubaliiiiii")
