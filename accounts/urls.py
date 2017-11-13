from django.conf.urls import url
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    #       회원가입하는 주소
    url(r'^signup/$', views.signup, name="signup"),

    #       로그인하는 주소
    url(r'^login/$', auth_views.login, name="login",
        kwargs = {'template_name' : 'accounts/login_form.html',
                  'authentication_form' : LoginForm
                  }),

    #       로그아웃하는 주소
    url(r'^logout/$', auth_views.logout, name="logout"),

    #       프로필을 보여주면서 수정까지 할 수 있게한다.
    url(r'^profile/$', views.ProfileView.as_view(), name="profile"),

]
