# -*- coding: utf-8 -*-
__author__ = 'zhiqi'
__date__ = '2018/9/12 10:10'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    # 判断账号密码是否为空
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误！'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误！'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)