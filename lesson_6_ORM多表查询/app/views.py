from django.shortcuts import render,HttpResponse
from app.models import *

# Create your views here.

def index(request):

    return render(request,'index.html',locals())


def addbook(request):


    return HttpResponse('<h1>添加成功</h1>')


def select(request):

    return render(request, 'index.html', locals())

def update(request):pass
def delbook(request):pass
