from django.shortcuts import render
from django.http import HttpResponse


def showIndex(request):
    return render(request,"main.html")

def registeruser(request):
    #print("Hello")
    f_name = request.POST.get("fname")
    l_name = request.POST.get("lname")
    fullname = f_name+" "+l_name
    return HttpResponse(fullname)
