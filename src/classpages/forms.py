from django import forms

from users.models import Ccom,Cevals,Classes

class CcomForm(forms.ModelForm):

    class Meta():
        model = Ccom
        fields = ["comments"]

        labels = {'comments': "コメント",
        }

class CevalForm(forms.ModelForm):
    class Meta():
        model = Cevals
        fields = ["rikai","raku"]

        labels = {
            'rikai': "理解度",
            'raku': "楽単",
        }

class CreateForm(forms.ModelForm):
    class Meta():
        model = Classes
        fields = '__all__'

        labels = {
            'class_id':"授業番号",
            'title':"授業名",
            'teacher':"教授名",
            'faculty':"学部",
            'department':"学科",
            'credit':"単位",
            'method_eval':"評価方法",
            'classform':"授業形式",
            'contents':"授業概要",
        }