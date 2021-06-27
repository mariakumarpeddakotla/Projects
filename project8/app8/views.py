from django.shortcuts import render

def showIndex(request):
    data = {"name":"maria","Salary":185000}
    return render(request,"main.html",data)
