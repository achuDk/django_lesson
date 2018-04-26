from wsgiref.simple_server import make_server


def route():
    url_pattern = {
        ("/",index),
        ("/login",login),
        ("/regist",regist),
    }
    return url_pattern

def index(req):
    f = open('index.html','rb')
    data = f.read()
    return data

def login(req):
    f = open('login.html','rb')
    data = f.read()
    return data

def regist(req):
    f = open('regist.html','rb')
    data = f.read()
    return data

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