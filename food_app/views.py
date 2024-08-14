from django.shortcuts import render, reverse
from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from food_app.models import Food

# Create your views here.

# 每一个视图, 暂且理解为, 形式上就是一个函数
# 在设计函数的时候, 必须要接收一个参数; 当 django 调用这个函数时, 所传递的 请求对象


# 接收一个请求对象, 通过处理, 最后, 返回一个响应对象(包含响应的具体内容)

# 插入数据
def index(request):
    # 在这里, 可以做各种业务!
    # 做完之后, 一定要写一个返回; 这个返回, 最后, 就是由django框架,响应给客户端的内容
    # temp = 1 + 2 + 3
    # return HttpResponse("响应给客户端的具体内容{temp}:".format(temp=temp))

    # 模拟模型的使用: 新建模型,使用模型给数据库的表插入数据
    import random
    food = Food(name='小鸡炖蘑菇', count=random.randint(30, 100), price=random.uniform(30, 100), desc='做起来很费劲')

    food.save()

    return HttpResponse(f'数据创建完成')


def add_food(request):
    return render(request, 'add_food.html')


def save_food(request):
    if request.method == "POST":
        print(request.POST)
        food_name = request.POST.get("food_name")
        count = request.POST.get("count")
        price = request.POST.get("price")
        desc = request.POST.get("desc")

        food = Food(name=food_name, count=count, price=price, desc=desc)
        food.save()
        return HttpResponseRedirect(reverse("food:food_list"))


# 查询数据
def food_list(request):
    # data = [
    #     {"id": 1, 'title': "红烧大鹅", "price": 36},
    #     {"id": 2, 'title': "红烧大鸭", "price": 28},
    #     {"id": 3, 'title': "红烧鸡翅", "price": 18}
    # ]

    # return JsonResponse(data, safe=False)

    # 使用模型: 用模型查询获取数据库的表数据
    # foods = Food.objects.all().values()
    #
    # return JsonResponse(data=list(foods), safe=False)

    # 模拟使用: 模板T, 网页()
    foods = Food.objects.all().values()
    return render(request, 'food_app/food_list.html', context={'title': "这是ds编写的", 'food_list': foods})
    # 这里没有IDE提示: 原因: 我们仅仅在settings 告知django的查找路径
    # IDE 不知道, 所以没有提示! 运行时, 不会报错!
    # 顺便告诉IDE, 哪里才是模板根路径


# 筛选数据
def food_detail(request, id):
    # data = [1, 2, 3, id]
    # food = Food.objects.filter(id=id).values()
    # return JsonResponse(data=list(food)[0], safe=False)

    food = Food.objects.filter(id=id).values()
    print(food)
    return render(request, "food_detail.html", context={'title': "这是ds编写的", 'food': list(food)[0]})



