from django.shortcuts import render

# Create your views here.
def BlogHome(req):
    context = {
        'title':'Blogs',
        'subTitle':'Lots of blogs'
    }
    return render(req,'blog.html',context)

