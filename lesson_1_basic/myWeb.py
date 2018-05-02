from wsgiref.simple_server import make_server
import time

def route():
    url_pattern = {
        ("/",index),
        ("/login",login),
        ("/regist",regist),
        ("/show_time",show_time)
    }
    return url_pattern

def index(req):
    f = open('index.html','rb')
    data = f.read()
    return data

def login(req):
    # print(req)
    print(req["QUERY_STRING"])

    f = open('login.html','rb')
    data = f.read()
    return data

def regist(req):
    f = open('regist.html','rb')
    data = f.read()
    return data

def show_time(req):
    times = time.ctime()
    # 第一种方法
    # return ('<h1>时间： [ %s ]</h1>' %str(times)).encode('gbk')

    # 第二种方法
    f = open('show_time.html','rb')
    data = f.read()
    data = data.decode('utf8')
    data = data.replace('{{time}}',str(times))
    return data.encode('utf8')

def application(environ,start_response):
    # print("========>",environ)
    start_response('200 OK',[('Content-Type','text/html')])

    path = environ["PATH_INFO"]
    # print("environ.get('PATH_INFO'):",environ.get("PATH_INFO"))
    # print("environ['PATH_INFO']:",environ["PATH_INFO"])

    print("path",path)

    func = None
    url_patterns = route()
    # print("url_patterns:",url_patterns)

    for item in url_patterns:
        print("item[0]", item[0])
        if item[0] == path:
            func = item[1]
            break
    if func:
        return [func(environ)]
    else:
        return [b'<h1>404 not found</h1>']

httpd = make_server('',8080,application)

print('Serving HTTP on port 8080...')
# 开始监听HTTP请求
httpd.serve_forever()