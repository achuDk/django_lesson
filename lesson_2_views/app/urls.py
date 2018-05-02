from django.urls import path,re_path
from myWeb import views

urlpatterns = [
    re_path(r'article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})', views.article),

    re_path(r'^comment/page-(?P<page_num>\d{2})', views.comment),
    # 使用 url 别名
    re_path(r'regist', views.regist, name="req"),
]
