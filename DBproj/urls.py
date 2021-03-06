# -*- coding: utf-8 -*-

"""DBproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from .views import HomeView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),         admin 페이지를 사용할 수 없음.

    #       root url '/'에 대한 처리
    url(r'^$', HomeView.as_view(), name='home'),

    # super admin, admin 로그인 기능 구현 앱.
    url(r'^accounts/', include('accounts.urls')),

]
