from django.shortcuts import render,HttpResponse,resolve_url
from app.models import *

# Create your views here.

def index(request):
    print("=======>",request)
    return render(request,'index.html',locals())


def addbook(request):

    """ 一对多添加 """
    # 方法1：直接对外键字段赋值
    # Book.objects.create(name='Linux',price=120,issue_date='2017-12-12',publish_id=2)

    # 方法2：将外键对象作为类的属性值
    # pub_obj = Publish.objects.filter(name='人民出版社')[0]
    # Book.objects.create(name='Django',price=50,issue_date='2018-01-01',publish=pub_obj)


    """ 多对多添加 """
    # 给指定book增加多个作者

    # 逐条添加
    # author_objs = Author.objects.get(id=1)
    # book_obj = Book.objects.get(id=3)
    # book_obj.author.add(author_objs)

    # 添加多条
    author_objs = Author.objects.filter(age=23)
    book_obj = Book.objects.get(id=3)
    # 【注意】此处多条对象前要加星号  *
    book_obj.author.add(*author_objs)


    return HttpResponse('<h1>添加成功</h1>')


def one_to_many(request):
    # 一对多查询：正向查找
    # 查询python这本书是哪个出版社出版的
    # 方法1：
    # book_obj = Book.objects.filter(name='Python')[0]
    # print(book_obj.name)
    # print(book_obj.price)
    # print("======>",book_obj.publish)
    # print(type(book_obj.publish))

    # 方法2
    # pub_obj = Publish.objects.filter(book__name='python')
    # print(pub_obj.values('name','city'))
    #
    print("------------------------------------------------------")

    # 多对一查询：反向查找
    # 查询人民出版社出版过那些书的名字和价格
    # 方法1：
    # pub_obj = Publish.objects.filter(name='人民出版社')[0]
    # pub_books = Book.objects.filter(publish=pub_obj)
    # print(">>>>>",pub_books)
    # print(pub_books.values('name','price'))

    # 方法2：
    # pub_obj = Publish.objects.filter(name='人民出版社')[0]
    # pub_books = pub_obj.book_set.all()
    # print(pub_books.values('name','price'))
    # print(type(pub_books))

    # 方法3：
    # pub_books = Book.objects.filter(publish__name='人民出版社')
    # print(pub_books.values('name','price'))

    return HttpResponse('查询成功')


def many_to_many(request):

    return HttpResponse('查询成功')




def update(request):pass
def delbook(request):pass
