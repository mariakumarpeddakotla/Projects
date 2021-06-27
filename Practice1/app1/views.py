from django.shortcuts import render

def showIndex(request):
    student_info = {"details":
           [{'student_id': 1, 'name': 'Jean Castro', 'class': 'V','marks':[36,75,26,94,99,70,38,55]},
            {'student_id': 2, 'name': 'Lula Powell', 'class': 'V','marks':[30,66,67,50,66,'A',99,58]},
            {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI','marks':[66,77,10,80,95,33,68,51]},
            {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI','marks':[65,55,72,98,9,71,39,30]},
            {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII','marks':[36,38,60,94,92,64,72,88]}]
    }
    return render(request,"main.html",student_info)
