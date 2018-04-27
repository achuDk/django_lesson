from django.shortcuts import render,HttpResponse
import time


# Create your views here.

def show_time(request):
    times = time.ctime()
    # 第一种方式，直接返回字符串对象
    # return HttpResponse('Hello World!')

    # 第二种方式，返回templates目录下的html页面，使用locals()来转换变量，此方法不常用
    return render(request,'index.html',{"times":times})


def comment(request,page_num):
    return HttpResponse('comment page , %sth page' %page_num)


def article(request,year,month):
    return HttpResponse('<h1>%s年%s月</h1>' %(year,month))

def regist(request):
    print('request======>',request)
    user = request.GET.get('user')
    pwd = request.GET.get('pwd')
    # print('user:',user)
    # print('pwd:',pwd)
    if request.method == "POST":
        return HttpResponse("<h1 style='color: red;'>Regist Successful!</h1>")
    return render(request,'regist.html')