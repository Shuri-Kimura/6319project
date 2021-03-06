from django import forms
from django.contrib.auth.models import User
from .models import Users

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = Users
        # フィールド指定
        fields = ('username','student_number','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'stuent_number':"学籍番号",'email':"メールアドレス"}
