from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def home(request):
    peoples = [
    {'name':'sahil nayak', 'age': 18},
    {'name':'Ritika gupta', 'age': 19},
    {'name':'Arpeeta mahapatra', 'age': 18}
    ]
    
    return render(request , "index.html", context= {'people': peoples})

    


