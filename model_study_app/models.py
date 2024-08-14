from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Category(models.Model):
    # id 不用手动添加,会自动生成
    name = models.CharField("分类名称", max_length=20)

    # 描述多级分类
    # 直接手动设计数据库表格的时候, 表结构: 额外的一个字段, parent_id 指明 父分类的 id

    # 关联的目标字段, 一定是主键id
    # 构建 Category.parent_id in 模型 .id
    # 如果是自关联, 那么这个模型, 可以直接, 写'self'
    # null: 数据库表结构当中, 字段值, 能否为null
    # blank: admin 管理系统当中,编辑/新增模型的时候, 做一个必填验证
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='category_list')


class Course(models.Model):
    name = models.CharField("课程名称", max_length=50)
    cover = models.ImageField("课程封面", upload_to='course')
    price = models.FloatField("课程价格")
    is_show = models.BooleanField("是否上架", default=False)
    publish_time = models.DateTimeField("发布时间", auto_now_add=True)  # 一旦我们指明了此字段是自动填充
    # 注意: amdin 系统里面,编辑/增加时 不要显示publish_time这个字段

    detail = models.TextField("课程详情")

    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="所属分类", related_name='course_list')

    # amdin系统操作变更数据时,显示的数据集名称,默认为数组[索引号]
    def __str__(self):
        return f'课程名称: {self.name}'

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name + "管理"


class User(models.Model):
    name = models.CharField("用户姓名", max_length=20)
    sex = models.CharField("用户性别", max_length=50, choices=(('male', '男'), ('female', '女'), ('secret', '保密')), default='secret')
    age = models.IntegerField("用户年龄", validators=[
        MinValueValidator(1),
        MaxValueValidator(200)
    ], help_text="1 到 200")
    email = models.EmailField("用户邮箱")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name + "管理"


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="用户")
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="课程")
    content = models.TextField("评论内容")
