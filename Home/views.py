from django.shortcuts import render
from django.http import HttpResponse
from . models import Post
# Create your views here.

def index(request):
    contex={
        'posts': Post.objects.all()
        }
    
    return render(request,'Home/home.html',contex)

def profile(request):

    return render(request,'Home/profile.html')



