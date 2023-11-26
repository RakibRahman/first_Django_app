from django.shortcuts import render

# Create your views here.
def BlogHome(req):
    return render(req,'blog.html')

def BlogPost(req):
    return render(req,'base.html')