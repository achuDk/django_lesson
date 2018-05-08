from django.shortcuts import render,redirect

# Create your views here.

def login(request):
    print("COOKIE",request.COOKIES)
    print("session",request.session)
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "yuan" and pwd == "123":
            ret = redirect('/index/')
            # ret.set_cookie("user",user)

            request.session['if_login'] = True
            request.session['user'] = user

            return ret
    return render(request,'login.html')


def index(request):
    # ret = request.COOKIES.get("user",None)

    if request.session.get("if_login",None):
        ret = request.session.get("user",None)
        print("ret3",ret)
        if ret:
            user = ret
            return render(request,'index.html',locals())
    else:
        return redirect('/login/')