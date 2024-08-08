from django.shortcuts import render, reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpResponseNotFound
from django.views.generic.base import View

# Create your views here.


# request: 请求对象
# 客户端, 发送给我们服务器, 请求报文的包装(对象)
def index_func(request):
    print(type(request))
    print(f"请求方法: {request.method}")
    print(f"资源路径: {request.path}")
    print(f"请求头: {request.headers}")
    print(f"GET传递的参数: {request.GET}")
    print(f'POST:{request.POST}')
    print(f'COOKIE: {request.COOKIES}')

    # client = request.headers.get("User-Agent")
    # if client.startswith("python"):
    #     return HttpResponse("gun")
    # else:
    #     return HttpResponse("ok")

    print(request.method, request.POST)
    if request.method == "GET":
        # GET 处理业务
        pass
    elif request.method == "POST":
        # POST 处理业务
        pass

    return HttpResponse("参数测试!")


def cookie_test(request):
    # 浏览器发送请求,携带过来的cookie值
    print(request.COOKIES)
    print(request.method)

    count = int(request.COOKIES.get("count")) + 1

    # 希望把cookie设置给浏览器
    response = HttpResponse(f"cookie测试, 不同用户,页面的访问次数:{count}")
    response.set_cookie("count", str(count))
    return response


def response_test(request):
    # response = HttpResponse("普通的字符串")
    response = HttpResponse("<h1>H1标题</h1>")  # 返回一个HTML片段

    # 不渲染为HTML文本
    # response.headers.__setitem__('Content-Type', 'text/plain; charset=utf-8')

    food1 = {
        'id': 1,
        'name': '大鹅'
    }

    food2 = {
        'id': 2,
        'name': '小鸡'
    }

    import json
    response = HttpResponse(json.dumps(food1))

    # 直接转JSON
    response = JsonResponse(food1)

    # 当传入的类型不是字段的序列化,关闭safe安全模式
    food_list = [food1, food2]
    response = JsonResponse(food_list, safe=False)

    # 重定向场景
    r_to = reverse("index")
    print(r_to)  # /view_study/
    response = HttpResponseRedirect(r_to)

    # 404 return HttpResponseNotFound

    return response

# 基于类的视图, 收到不同类型的请求会返回相应的response
# !!! URL的对应函数要写SzView.as_view()调用一下
class SzView(View):
    def get(self, request):
        return HttpResponse("处理 get请求 业务逻辑")

    def post(self, request):
        return HttpResponse("处理 post请求 业务逻辑")

    def head(self, request):
        return HttpResponse("处理 head请求 业务逻辑")
