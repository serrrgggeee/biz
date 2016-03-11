# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django import forms
from filer.fields.image import FilerImageField
from redactor.fields import RedactorField

class Category(models.Model):
	name = models.CharField('Группа товара', max_length=64)
	def __unicode__(self):
		return self.name

class Producer(models.Model):
	name = models.CharField('Производитель', max_length=64)
	def __unicode__(self):
		return self.name


class Technic(models.Model):
	name = models.CharField('Название техники',  max_length=128)
	category = models.ForeignKey(Category, related_name="spare_technic", verbose_name='Категория')
	producer = models.ForeignKey(Producer, related_name="spare_technic_producer", verbose_name='Производитель')
	description = RedactorField( verbose_name='Описание')
	count = models.BigIntegerField('Количество едениц')
	price = models.DecimalField('Стоимость единицы, руб.', max_digits=10, decimal_places=2)
	shou = models.BooleanField(default=True,  verbose_name='Отображать на сайте')
	first_order = models.BooleanField(default=False,  verbose_name='Первые в списке')
	pub_date = models.DateTimeField('Срок размещения в днях')

	def __unicode__(self):
		return self.name

class Photo(models.Model):
	name = models.CharField('Название фотографии', max_length=64)
	photo_technic = FilerImageField(
        blank=True,
		related_name="photo_technic",
        help_text=u'Optional. Please supply a photo of this main member.',
        null=True,
        on_delete=models.SET_NULL,  # Important
		verbose_name='Фотография'
    )
	spare = models.ForeignKey(Technic, related_name="spare_technic", verbose_name='Группа')
	def __unicode__(self):
		return self.name
