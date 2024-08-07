from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return HttpResponse("url学习的首页!")


def a(request):
    return HttpResponse("url路由页面-----a")


def b(request):
    return HttpResponse("url路由页面-----b")


def a_b_c(request):
    return HttpResponse("url路由页面-----c")


# def handler_article(request, cid, id):
#     return HttpResponse(f"url路由页面---{cid}--{id}")


def handler_article_int_id(request, id):
    return HttpResponse(f"url路由页面---int--{id}")


def handler_article_str_id(request, id):
    return HttpResponse(f"url路由页面---str--{id}")

def handler_search(request):
    # v_a = request.GET.get('a')
    # v_aa = request.GET.getlist('a')
    # print(v_a, v_aa)
    # return HttpResponse(f'参数值为{v_a},{v_aa}')

    # 模拟重定向

    # 重新确定定位的方向(硬编码)
    # return HttpResponseRedirect('/url_study/')

    # 反向解析编码
    return HttpResponseRedirect(reverse('food:index'))
