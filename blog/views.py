from django.shortcuts import render

def inicio(request):
    return render(request,"blog/blog.html")

# Create your views here.
