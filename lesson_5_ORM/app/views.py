from django.shortcuts import render,HttpResponse
from app.models import *

# Create your views here.

def index(request):

    return render(request,'index.html',locals())


def addbook(request):

    """ 第一种方法 ： 实例化 """
    # b1 = Book(name='Python基础',price=123,issue_date='2018-05-03',author='tom')
    # b1.save()

    """ 第二种方法 ： 调用类方法 """
    Book.objects.create(name='Linux基础',price=123,issue_date='2017-12-12',author='tom')

    return HttpResponse('<h1>添加成功</h1>')


def update(request):

    """ 第一种方法 """
    # b = Book.objects.get(name='Linux基础',author='tom')
    # b.author = 'alex'
    # b.save()

    """ 第二种方法 """
    Book.objects.filter(author='tom').update(price=99)

    return HttpResponse('<h1>修改成功</h1>')


def delbook(request):
    Book.objects.filter(author='tom',price=120).delete()

    return HttpResponse('<h1>删除成功</h1>')