from django.urls import path

from food_app.views import *


app_name = "food"

# 子路由去掉总路由的前缀路径
urlpatterns = [
    path('', index, name="index"),

    path('add_page/', add_food, name="add_food"),
    path('save_data/', save_food, name="save_food"),

    path('list/', food_list, name="food_list"),
    path('detail/<int:id>', food_detail, name="food_detail"),
]