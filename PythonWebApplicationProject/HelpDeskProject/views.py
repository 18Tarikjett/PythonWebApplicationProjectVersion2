from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import posts


# Create your views here.

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'home/home_page.html', context)

def about(request):
    context = {
        'posts': posts
    }
    return render(request,'home/about_page.html',context)






