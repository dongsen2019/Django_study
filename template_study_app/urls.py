from django.urls import path
from template_study_app.views import *

# 子路由去掉总路由的前缀路径
urlpatterns = [
    path('', index, name="index"),

]


