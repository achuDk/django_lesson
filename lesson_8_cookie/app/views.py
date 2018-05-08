from django.shortcuts import render,redirect
import datetime
# Create your views here.

def login(request):
    print("COOKIE",request.COOKIES)
    print("session",request.session)
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "yuan" and pwd == "123":
            ret = redirect('/index/')
            # 过期时间为3天
            # ret.set_cookie("user",user,max_age=172800,expires=datetime.datetime.utcnow()+datetime.datetime.timedelta(days=3))

            request.session['if_login'] = True
            request.session['user'] = user
            request.session.set_expiry(172800)
            return ret
    return render(request,'login.html')


def index(request):
    # ret = request.COOKIES.get("user",None)

    ret = request.session.get("user", None)

    print("ret3", ret)
    if request.session.get("if_login",None) and ret:
    # if ret:
        user = ret
        return render(request,'index.html',locals())
    else:
        return redirect('/login/')