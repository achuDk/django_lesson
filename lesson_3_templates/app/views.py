from django.shortcuts import render
import time,datetime
# Create your views here.


class Animal():
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

def show_time(request):
    time = datetime.datetime.now()
    list = ['a',1,{"name":"alex"}]
    dict = {"name":"yuan","age":21}
    obj = Animal('tom','male')
    filter_test = 'hello world !'
    tag_a = '<a href=''>click</a>'
    return render(request,'show_time.html',locals())


def index(request):
    list = ['alex','yuan','egon']
    dict = {"name": "yuan", "age": 21}
    return render(request,'index.html',locals())

def login(request):

    return render(request,'login.html',locals())