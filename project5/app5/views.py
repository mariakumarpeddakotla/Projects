from django.shortcuts import render

def showIndex(request):
    details = {"name":"Maria Kumar","age":22,"village":"Phirangipuram"}
    return render(request,"main.html",details)
