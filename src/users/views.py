from django.shortcuts import render
from django.views.generic import TemplateView # テンプレートタグ
from .forms import AccountForm # ユーザーアカウントフォーム
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Users

def index(request):
    return render(request, 'users/index.html')

class  AccountRegistration(TemplateView):

    def __init__(self):
        self.params = {
        "AccountCreate":False,
        "account_form": AccountForm(),
        }

    # Get処理
    def get(self,request):
        self.params["account_form"] = AccountForm()
        self.params["AccountCreate"] = False
        return render(request,'users/register.html',context=self.params)

    # Post処理
    def post(self,request):
        self.params["account_form"] = AccountForm(data=request.POST)

        # フォーム入力の有効検証
        if self.params["account_form"].is_valid():
            # アカウント情報をDB保存
            #account = self.params["account_form"].save()
            account = Users(username=self.params["account_form"]["username"],student_number=self.params["account_form"]["student_number"],email=self.params["account_form"]["email"])
            # パスワードをハッシュ化
            account.set_password(self.params["account_form"]["password"])
            #account.set_password(account.password)
            # ハッシュ化パスワード更新
            account.save()
            #account.save()

            # 下記追加情報
            # 下記操作のため、コミットなし

            # 画像アップロード有無検証
            # if 'account_image' in request.FILES:
            #     add_account.account_image = request.FILES['account_image']

            # モデル保存
            #add_account.save()

            # アカウント作成情報更新
            self.params["AccountCreate"] = True

        else:
            # フォームが有効でない場合
            print(self.params["account_form"].errors)

        return render(request,'users/register.html',context=self.params)