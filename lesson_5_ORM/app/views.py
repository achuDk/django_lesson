from django.shortcuts import render,HttpResponse
from app.models import *

# Create your views here.

def index(request):

    return render(request,'index.html',locals())


def addbook(request):

    """ 第一种方法 ： 实例化 """
    b1 = Book(name='Python基础',price=123,issue_date='2018-05-03',author='tom')
    b1.save()

    """ 第二种方法 ： 调用类方法 """
    # Book.objects.create(name='Linux基础',price=123,issue_date='2017-12-12',author='tom')

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


def select(request):
    """ 1. 查询的结果为多条记录组成的集合 """
    # 显示所有
    book_list = Book.objects.all()

    # 显示指定筛选条件的结果
    # book_list = Book.objects.filter(author='alex')

    # 显示结果中的前3条
    # book_list = Book.objects.all()[:3]

    # 倒序
    # book_list = Book.objects.all()[::-1]

    print(type(book_list),book_list)
    print(book_list[0])

    """ 2. 查询的结果为一条记录，否则报错 """
    ret = Book.objects.get(id=1)

    print("ret:",ret)

    """ 关联查询 """
    res1 = Book.objects.filter(author='yuan').values('id','name','price')
    print("res1:",res1)
    print(res1[0]['name'])

    res2 = Book.objects.exclude(author='yuan').values_list('id','name','price')
    print('res2:',res2)


    """ 3. 条件查询 """
    # book_list = Book.objects.filter(name__icontains='n')

    # book_list = Book.objects.filter(issue_date__gt='2018-05-01')



    return render(request,'index.html',locals())