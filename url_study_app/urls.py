from django.urls import path
from url_study_app.views import *

# 子路由去掉总路由的前缀路径
urlpatterns = [

    # 固定路径路由, 不带动态参数设计方案
    path('', index, name='index'),
    path('a/', a),
    path('b/', b),
    path('a/b/c/', a_b_c),

    # 带动态参数的路由 handler_article(request, cid, id)
    # path('article/<cid>/<id>', handler_article),

    # 带类型约束的动态参数
    path('article/<int:id>', handler_article_int_id),
    path('article/<str:id>', handler_article_str_id),

    # 带有正则的路径设计
    # 以 detail 开头
    # import re_path

    # (?P<参数名字> 正则表达式)
    # re_path(r'^detail/(?P<category_name>......)/$',视图函数)

    #
    path('search/', handler_search),
]