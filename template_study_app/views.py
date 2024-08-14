from django.shortcuts import render, HttpResponse
from model_study_app.models import *

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return f'{self.name}跑起来'


# Create your views here.
def index(request):
    # key变量名不能使用-这种特殊意义字符
    context = {
        'data': "  社会我顺哥,人狠话不多  abc ",
        'dict_ps': {'name': 'sz', 'age': 18},
        'person': Person('ds', 34),
        'pets': ["小花", "小红"],
        'category': Category.objects.filter(parent__isnull=True),
        'score': 100,
    }
    return render(request, 'template_app/index.html', context= context)