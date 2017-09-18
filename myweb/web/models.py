# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Category(models.Model):
    order_number = models.IntegerField()
    category_name = models.CharField(max_length=200)
    # 好物推荐
    # 教学栏
    # 黑科技
    # 新事物
    # 怀旧向
    # 工具集

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name


class User(models.Model):
    username = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    public_date = models.DateTimeField()
    content = models.CharField(max_length=2000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    collect = models.IntegerField()  # 收藏
    like = models.IntegerField()  # 点赞

    def __str__(self):
        return self.title


