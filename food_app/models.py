from django.db import models

# Create your models here.

# ORM 系统所提供的功能
# 模型(类) -> 数据库表格!
# 类名 -> 表名 一一对应
# 属性 -> 字段(类型+长度+约束) 一一对应
# 表名: 应用名字_模型名字


class Food(models.Model):
    name = models.CharField(max_length=60)
    count = models.IntegerField()
    price = models.FloatField()
    desc = models.TextField(max_length=800)
    publish_time = models.DateTimeField(auto_now_add=True)

