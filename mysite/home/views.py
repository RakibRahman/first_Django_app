from django.shortcuts import render

# Create your views here.
def HomePage(req):
    context ={
        'name':'Rakib'
    }
    return render(req,'home.html',context)