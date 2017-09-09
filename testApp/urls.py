#!/usr/bin/env python3
# coding=utf-8
# __author__ = 'admin'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^index/$",views.index),
    url(r"^home/$",views.Ovcom),
    url('^lin/$',views.lin),
]
