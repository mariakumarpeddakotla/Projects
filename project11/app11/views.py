from django.shortcuts import render

def showIndex(request):
    if request.method == "POST":
        username = request.POST.get("name")
        password = request.POST.get("password")
        if username == "maria" and password == "kumar":
            return render(request,"index.html",{"message":"True"})
        else:
            return render(request,"index.html",{"message":"False"})
    else:
        return render(request,"index.html")
