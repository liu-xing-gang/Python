# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# 新增元组用于设置消息类型枚举项
KIND_CHOICES = (
    ('Python技术', 'Python技术2'),
    ('数据库技术', '数据库技术2'),
    ('经济学', '经济学2'),
    ('文体资讯', '文体资讯2'),
    ('个人心情', '个人心情2'),
    ('其它', '其它2')
)

# Create your models here.
class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20, default='匿名')
    
    # 修改kind定义，加入choices参数
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])

#     
class UserProfile(User):
    cname = models.CharField("中文名称", max_length=30)

# 
class UserProfileAdmin(admin.ModelAdmin):
    # 定义admin总览里每行的显示信息
    list_display = ('cname', 'username', 'email')
    # 定义搜索框以哪些字段可以搜索
    search_fields = ('cname', 'username')

