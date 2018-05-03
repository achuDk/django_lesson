from django.shortcuts import render,HttpResponse,redirect
import time


# Create your views here.

def show_time(request):
    times = time.ctime()
    name = "yuan"
    # 第一种方式，直接返回字符串对象
    # return HttpResponse('Hello World!')

    # 第二种方式，返回templates目录下的html页面，
    # return render(request,'index.html',{"times":times,"name":name})

    # 使用locals()来转换变量，无需每个变量逐一声明
    return render(request,'index.html',locals())


def comment(request,page_num):
    return HttpResponse('comment page , %sth page' %page_num)


def article(request,year,month):
    return HttpResponse('<h1>%s年%s月</h1>' %(year,month))

def regist(request):
    print('request======>',request)
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    print('user:',user)
    print('pwd:',pwd)
    # 路径相关方法或属性
    print('path:',request.path)
    # 当url中包含其他参数时，也会一起显示出来，如： /myweb/regist?user=1&pwd=2
    print('get_full_path:',request.get_full_path())

    if user == "yuan" and pwd == "123":
        # return HttpResponse("<h1 style='color: red;'>Hello  %s  <br>Regist Successful!</h1>" %user)
        return redirect('/show_time')
    return render(request,'regist.html')
