from django import forms
from django.db.models import fields

from users.models import Messages, Tcom, Texts, Uevals


class UevalFrom(forms.ModelForm):
    class Meta():
        model = Uevals

        fields = ['eval']

        labels = {
            'eval': '相手への評価'
        }
