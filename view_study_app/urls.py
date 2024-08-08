from django.urls import path
from view_study_app.views import *

# 子路由去掉总路由的前缀路径
urlpatterns = [
    path('', index_func, name="index"),
    path('cookie', cookie_test),
    path('response', response_test),
    path('class_view/', SzView.as_view()),
]


