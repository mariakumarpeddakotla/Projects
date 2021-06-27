from django.shortcuts import render
from django.http import HttpResponse

def showIndex(request):
    return render(request,"main.html")

def user(request):
    f_name = request.POST.get('fname')
    l_name = request.POST.get('lname')
    fullname = f_name+" "+l_name
    number = request.POST.get('num')
    email = request.POST.get('mail')
    option = request.POST.get('op')
    Gender = request.POST.get('gen')
    return HttpResponse(email)

