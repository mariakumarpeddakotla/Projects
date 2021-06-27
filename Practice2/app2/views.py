from django.shortcuts import render

def showIndex(request):
    tab = {"info":
                [{"company":"Alfreds Futterkiste","contact":"Maria","country":"USA"},
                 {"company": "Berglunds snabbköp", "contact": "Kumar", "country": "Canada"},
                 {"company":"Centro comercial Moctezuma","contact":"Vijay","country":"Germany"},
                 {"company":"Ernst Handel","contact":"Anand","country":"Australia"},
                 {"company": "Island Trading", "contact": "Raja", "country": "Japan"},
                 {"company": "Königlich Essen", "contact": "Revanth", "country": "UK"},
                 {"company": "Laughing Bacchus Winecellars", "contact": "Mahi", "country": "Italy"},
                 {"company": "Magazzini Alimentari Riuniti", "contact": "Lohith", "country": "Swedden"}]
    }
    return render(request,"main.html",tab)