from django.shortcuts import render
from django.http import HttpResponse
from app14.models import Registration

def showMainPage(request):
    return render(request, "main.html")


def showRegisterPage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        loc = request.POST.get("location")
        password = request.POST.get("password")

        Registration(name=name,contact=contact,email=email,location=loc,password=password).save()
        return render(request,"register.html",{"message":"Sucess! Registration is Done"})
    else:
        return render(request,"register.html")

def showLoginPage(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        em = request.POST.get('email')
        pas = request.POST.get('password')

        try:
            stu_obj = Registration.objects.get(email=em,password=pas)
            return render(request,'welcome.html')
        except Registration.DoesNotExist:
            return render(request,'login.html',{"error_message":"Invalid User"})
