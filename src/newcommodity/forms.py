
from django import forms
#モデルクラスを呼出
from users.models import Texts
from . import models




#フォームクラス作成
class TextForm(forms.ModelForm):

    class Meta():
        #①モデルクラスを指定
        model = Texts

        #②表示するモデルクラスのフィールドを定義
        fields = ('__all__')

        #③表示ラベルを定義
        labels = {'text_id':"教科書ID",
                  'user_id':"ユーザID",
                  'class_id':"教科ID",
                  'title':"商品名",
                'info':"商品情報",
                  'sold_flag':"soldフラグ",
                  'category':"カテゴリ",
                  'state':"商品状態",
                  'date':"出品日時",
                  'days':"お届け日数",
                  'image1':"画像１",
                  'image2':"画像2",
                 'image3':"画像3",
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
    