from django.shortcuts import render, reverse
from django.shortcuts import HttpResponse
from model_study_app.models import *
from django.http import JsonResponse

# Create your views here.



def index(request):
    return HttpResponse("模型学习-首页")


def add_model(request):
    # ------数据库的增------

    # home_category = Category.objects.get(id=1)
    # print(home_category)
    #
    # category = Category(name='模型添加测试', parent=home_category)

    # 外键引用的模型字段,在数据库中的字段名为 模型字段名 + _id
    # category = Category(name='模型添加测试2', parent_id=2)
    # category.save()

    # # 使用类方法进行创建
    # Category.objects.create(name='模型添加测试-类方法创建', parent_id=3)

    # ------数据库的新增修改------
    # category = Category(id=4, name='关于我们-修改')
    # category.save()

    return HttpResponse("添加模型测试")


def delete_model(request):

    # ------数据库的删------
    # c8 = Category.objects.get(id=8)
    #
    # c8.delete()

    # ------数据库的批量删------
    # gt: greater then
    # lt: less then
    # e: equal
    # gte
    # lte
    # in
    c_gt_4 = Category.objects.filter(id__gt=5)
    print(c_gt_4)

    result = c_gt_4.delete()
    print(result)  # (4, {'model_study_app.Category': 4}) 删除操作的返,总数,哪个模型删除的个数

    return HttpResponse("删除模型数据测试")


def update_model(request):
    update_data = Category.objects.get(id=4)
    update_data.name = '关于我们-更新'
    update_data.parent_id = 2

    update_data.save()

    # 批量更新 Person.objects.filter(age gte=18).update(score=0)
    return HttpResponse("更新模型数据测试")


def select_model(request):
    # 如果在数据库中的字段是路径,需要在HTML模板的语法中添加.url后缀,
    # 这样系统会自动加上服务器地址的前缀
    context = {
        'user': User.objects.all()
        # 'user': User.objects.filter(age__gte=29)
        # 'user': User.objects.exclude(age__gte=29)
        # 'user': User.objects.all()[1:3] 切片操作
        # 'user': User.objects.get(id=4) get方法,筛选的键要保证唯一
        # User.objects.all().count() --select count(1)
    }

    print(User.objects.all().count())
    return render(request, 'model_study_app/select.html', context=context)


def select_model_json(request):
    # 如果在数据库中的字段是路径,需要在HTML模板的语法中添加.url后缀,
    # 这样系统会自动加上服务器地址的前缀
    sel_all = User.objects.all()
    to_jsn = list(sel_all.values())

    return JsonResponse(to_jsn, safe=False)
