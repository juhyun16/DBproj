# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views


urlpatterns = [
    #       로그인하는 주소
    url(r'^login/$', views.login, name="login"),

]
