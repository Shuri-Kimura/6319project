from django import forms

from users.models import Messages, Tcom, Texts


class TcomForm(forms.ModelForm):

    class Meta():
        # ①モデルクラスを指定
        model = Tcom

        # ②表示するモデルクラスのフィールドを定義
        fields = ["comments"]

        # ③表示ラベルを定義
        labels = {'comments': "コメント",
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
        fields = []

        labels = {}
