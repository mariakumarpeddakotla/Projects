from django.shortcuts import render
from django.http import HttpResponse

def show(request):
    message = "Working"
    return HttpResponse(message)

