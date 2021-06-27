from django.shortcuts import render
from app1.models import Register

def showregister(request):
    if request.method == 'POST':
        Fname = request.POST.get("fname")
        Lname = request.POST.get("lname")
        Uname = request.POST.get("uname")
        Pas = request.POST.get("pas")
        Rpas = request.POST.get("rpas")
        Age = request.POST.get("age")
        Register(fname = Fname,lname=Lname,uname=Uname,password=Pas,repass=Rpas,age=Age).save()
        return render(request,"login.html",{"message":"Sucess!Registration is Done"})
    else:
        return render(request,"register.html")
def showlogin(request):
    if request.method=='GET':
        return render(request,"login.html")
    else:
        un = request.POST.get('username')
        pas = request.POST.get('password')
        try:
            Register.objects.get(uname = un,password=pas)
            return render(request,'welcome.html')
        except Register.DoesNotExist:
            return render(request,'login.html',{"message":"Sorry!Invalid User"})