from django import forms

from users.models import Ccom
class CcomForm(forms.ModelForm):

    class Meta():
        model = Ccom
        fields = ["comments"]

        labels = {'comments': "コメント",
        }
