from django.shortcuts import render

# Create your views here.
def showlogin(request):
    return render(request,"main.html")

def showforgot(request):
    if request.method == 'GET':
        return render(request,"forgot.html")
    else:
        return render(request,"create.html")