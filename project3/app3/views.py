from django.http import HttpResponse

def mark(request):
    message='''
        <html>
        <body style="background:black">
                <h1 style="color:White">Welcome to Django</h1>
        </body>
        </html>
'''
    return HttpResponse(message)
