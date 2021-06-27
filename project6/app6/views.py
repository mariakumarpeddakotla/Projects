from django.shortcuts import render

def showIndex(request):
    student_info = {"data":
        [
            {"idno":101,"name":"maria","marks":[89,56,74,15,45,56]},
            {"idno": 102, "name": "kumar", "marks": [45, 45, 99, 55, 78, 50]},
            {"idno": 103, "name": "vijay", "marks": [81, 62, 55, 96, 30, 42]},
            {"idno": 104, "name": "raja", "marks": [86, 52, 70, 35, "A", 51]},
            {"idno": 105, "name": "revanth", "marks": [99, 36, 72, 66, 40, 33]},
        ]
    }
    #dict_data = {"data":student_info}

    return render(request,"main.html",student_info)
