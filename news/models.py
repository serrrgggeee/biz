# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from redactor.fields import RedactorField

class Spare(models.Model):
	name = models.CharField('Заголовок',  max_length=128)
	text_news = RedactorField( verbose_name='Описание')
	pub_date = models.DateTimeField('Срок размещения в днях')

	def __unicode__(self):
		return self.name
