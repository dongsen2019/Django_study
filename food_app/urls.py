from django.urls import path

from food_app.views import index
from food_app.views import food_list
from food_app.views import food_detail

app_name = "food"

# 子路由去掉总路由的前缀路径
urlpatterns = [
    path('', index, name="index"),
    path('list/', food_list, name="food_list"),
    path('detail/<int:id>', food_detail, name="food_detail"),
]