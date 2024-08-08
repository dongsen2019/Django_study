from django.urls import path
from model_study_app.views import *

# 子路由去掉总路由的前缀路径
urlpatterns = [
    # 固定路径路由, 不带动态参数设计方案
    path('', index, name='index'),

]