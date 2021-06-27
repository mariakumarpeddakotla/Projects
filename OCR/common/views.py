from django.shortcuts import render
from common.utlies import sendTextMessage
from random import randint
from student.models import Student_RegistrationModel
from django.shortcuts import redirect

def showCommonPage(request):
    return render(request,"common/index.html")

def StudentPage(request):
    return render(request,'common/student.html')

def StudentRegister(request):
    if request.method=='POST':
        name = request.POST.get('std_name')
        contact = request.POST.get('std_cnt')
        email = request.POST.get('std_email')
        password = request.POST.get('std_pswd')

        otp = randint(100000,999999)

        message = "You registerd to sathya and the otp is"+str(otp)

        if sendTextMessage(message,contact):
            Student_RegistrationModel(name=name,contact=contact,email=email,password=password,otp=otp).save()
        else:
            pass
        return redirect('std_otp')
    else:
        StudentPage(request)

def openStudentOtp(request):
    return render(request,'common/otp.html')
