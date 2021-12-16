from django import forms
from django.db.models import fields

from users.models import Messages, Tcom, Texts, Uevals


class TcomForm2(forms.ModelForm):
    class Meta():
        model = Tcom

        fields = ['comments']

        labels = {
            'comments': 'コメント'
        }


class TcomForm(forms.ModelForm):

    class Meta():
        # ①モデルクラスを指定
        model = Tcom

        # ②表示するモデルクラスのフィールドを定義
        fields = ['comments', 'exhibitor_or_all']

        # ③表示ラベルを定義
        labels = {
            'comments': "コメント",
            'exhibitor_or_all': '出品者にのみコメントする'
        }

        """
        #②表示するモデルクラスのフィールドを定義
        fields = ('class_id','title','info','category','state','days','image1','image2','image3')

        #③表示ラベルを定義
        labels = {'class_id':"教科ID",
                  'title':"商品名",
                  'info':"商品情報",
                  'category':"カテゴリ",
                  'state':"商品状態",
                  'days':"お届け日数",
                  'image1':"画像１",
                  'image2':"画像2",
                 'image3':"画像3",
        }
        """


class MessageForm(forms.ModelForm):
    class Meta():
        model = Messages
        fields = []

        labels = {}


class TextForm(forms.ModelForm):
    class Meta():
        model = Texts
        fields = [
            'info',
            'category',
            'state',
            'days'
        ]

        labels = {
            'info': '商品情報',
            'category': 'カテゴリー',
            'state': '商品状態',
            'days': 'お渡しまでの日数'
        }


class UevalFrom(forms.ModelForm):
    class Meta():
        model = Uevals

        fields = ['eval']

        labels = {
            'eval': '相手への評価'
        }
