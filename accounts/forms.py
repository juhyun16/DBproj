#-*- coding:utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import MinLengthValidator
from .form_validators import phone_validator

class LoginForm(AuthenticationForm):
    pass


class SignupForm(UserCreationForm):
    username=forms.CharField(label='로그인에 사용할 아이디', validators=[MinLengthValidator(5), ],
                             help_text='특수문자 및 공백 입력 불가입니다. 최소 5자 이상 입력해주세요.',
                             widget=forms.TextInput(attrs={'pattern':'[a-zA-Z0-9]+'}))

    #password=forms.CharField(label='비밀번호', widget=forms.PasswordInput(),
     #                        help_text='비밀번호는 최소 8자 이상 이어야 합니다. 비밀번호는 전부 숫자로 이루어질 수 없습니다.')


    phone_number=forms.CharField(max_length=15, label='휴대전화 번호',
                                 help_text='필수입력요 사항입니다. Hyphen은 자동삽입됩니다.',
                                 validators=[phone_validator, ])

    lname=forms.CharField(max_length=20, label='last name',
                          help_text='성을 입력해주세요')

    fname=forms.CharField(max_length=20, label='first name',
                          help_text='이름을 입력해주세요')


    class Meta(UserCreationForm.Meta):
        fields=UserCreationForm.Meta.fields


    #       validators로 값의 유효성을 먼저 검사하고,
    #       clean_xxx 멤버함수로 무결성을 검사한다.(ex. 휴대전화번호 중복 검사)
    def clean_phone_number(self):
        pass


    #       save 함수의 역할.
    #       DB table의 record를 하나 생성하고 생성된 record를 반환한다.
    #       이 때 속성값들은 가공된 데이터 즉 form의 cleaned_data를 사용하도록 한다.
    def save(self, commit=True):
        user=super().save()
        print(user.id)
        return user




