# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from .views import smyt
urlpatterns = [
    url(r'$', smyt),
]
