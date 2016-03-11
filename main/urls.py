# -*- coding: utf-8 -*-
#from django.conf import settings
from django.conf.urls import include, url
#from django.conf.urls.i18n import i18n_patterns
from .views import MainView
urlpatterns = [
    url(r'$', MainView.as_view())
]
