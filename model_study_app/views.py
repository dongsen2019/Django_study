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

    # sel_all = User.objects.all()
    # result = User.objects.filter(id__gt=2)
    # result = User.objects.filter(pk__gt=2)  # 等价于id__gt=2 主键表达式
    # result = User.objects.filter(pk=1)
    # result = User.objects.filter(pk_exact=1) # 等价于pk=1

    key_word = request.GET.get('kw', '')  # 字典的取值方法,取不到就取默认值''

    # 以什么字符开始的匹配
    # result = User.objects.filter(name__startswith=key_word)

    # 包含什么字符的匹配 区分大小写
    # result = User.objects.filter(name__contains=key_word)

    # 包含什么字符的匹配 不区分大小写
    # result = User.objects.filter(name__icontains=key_word)

    # lt:小于 gt:大于 lte:小于等于 gte:大于等于

    # in [1,3,5] range(18,35)
    # result = User.objects.filter(id__in=[2, 3])
    # result = User.objects.filter(id__range=(1, 3))

    # 日期相关
    import datetime
    # result = Course.objects.filter(publish_time__year=2024)

    # 利用datetime过滤月份为8的时间
    # result = Course.objects.filter(publish_time__range=(datetime.date(2024, 8, 1), datetime.date(2024, 8, 31)))

    # 正则表达式 __regex=r'^itlike[0-9]{3}$'

    # 是否为空 __isnull __isnotnull

    # 跨表查询
    # result = Course.objects.filter(category__name='首页')

    # 利用Q: Query 表达式多条件查询
    from django.db.models import Q
    result = Course.objects.filter(Q(cover__contains='m') & Q(price__exact=202.3))

    # F表达式 Field
    course = Course.objects.get(id=1)
    course.price = course.price + 1
    course.save()

    # 等同于以下两条sql 的执行
    # select price from Course where id = 4; 取到60
    # update Course set price = (60 + 1) where id 4;

    # 用一条sql实现的等价F表达式
    # update Course set price = price + 1 where id 4;
    from django.db.models import F
    course = Course.objects.get(id=4)
    course.price = F('price') + 1  # F表达式指取某个字段值
    course.save()

    to_jsn = list(result.values())
    return JsonResponse(to_jsn, safe=False)


def select_model_fk(request):
    # 正向查询
    course_list = Course.objects.all()
    content = {
        'course_list': course_list,
    }

    # 反向查询
    category = Category.objects.get(id=1)
    # 当模型引用外键时,在外键模型中自动创建 course_set 属性,且该属性=关联的模型表
    # 当然也可以引用外键的模型中,使用related_name修改上述的属性名称
    result = category.course_set.all().values()

    return JsonResponse(list(result), safe=False)


def agg_model(request):
    from django.db.models import Avg, Min, Max, Sum

    result = User.objects.all()
    count = result.count()

    avg_age = result.aggregate(Avg('age'))  # 聚合的字段数据 {'age__avg': 88}
    max_age = result.aggregate(Min('age'))
    min_age = result.aggregate(Max('age'))
    sum_age = result.aggregate(Sum('age'))

    return HttpResponse(f"结果测试: count: {count} max_age: {max_age} min_age: {min_age} avg_age: {avg_age} sum_age: {sum_age}")


def ann_model(request):
    # 注意记得引入专用的聚合函数
    from django.db.models import Count, Sum, F
    categories = Category.objects.all()
    categories = categories.annotate(Count('course_list')).values()

    # user = User.objects.all()
    # user = user.annotate(Sum('age')).values()

    return JsonResponse(list(categories), safe=False)


def model_notice(request):
    # orm 系统, 为了性能考虑, 实行机制:懒加载
    # 你真正用到这个结果集的时候, 才会真正的从数据库表格当中,来获取数据
    result = User.objects.all().order_by("-age")

    # 此时才会真正加载
    print(result)

    # 立即加载,  延迟加载的问题
    result = Course.objects.only("id", "name")

    for i in result:
        print(i.name,i.id)  # only立即加载到内存,其他字段如果不访问,不会加载到内存

    return JsonResponse(list(result.values()), safe=False)


