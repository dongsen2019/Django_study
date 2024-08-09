from django.urls import path
from model_study_app.views import *

# 子路由去掉总路由的前缀路径
urlpatterns = [
    # 固定路径路由, 不带动态参数设计方案
    path('', index, name='index'),
    path('add/', add_model),
    path('delete/', delete_model),
    path('update/', update_model),
    path('select/', select_model),
    path('select_jsn', select_model_json)
]