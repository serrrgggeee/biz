# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Category, Technic, Photo, Producer

class PhotoAdmin(admin.StackedInline):
    model = Photo
    extra = 5

class SpareAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['name']}),
        ('Категория товара', {'fields':['category']}),
        ('Производитель', {'fields':['producer']}),
        ('Описание', {'fields':['description']}),
        ('Количество', {'fields':['count']}),
        ('Цена товара', {'fields':['price']}),
        ('Показывать на сайте', {'fields':['shou']}),
        ('Спец предложение(сортируются в начало)', {'fields':['first_order']}),
        ('Срок размещение', {'fields':['pub_date']}),
    ]
    inlines = [PhotoAdmin]

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Producer)
admin.site.register(Technic, SpareAdmin)