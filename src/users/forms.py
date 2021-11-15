from django import forms
from django.contrib.auth.models import User
from .models import Account

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','student_number','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'学籍番号':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('last_name','first_name',)
        labels = {'last_name':"苗字",'first_name':"名前",}