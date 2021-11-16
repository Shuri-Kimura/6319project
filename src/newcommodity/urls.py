
from django.urls import path
from . import views

app_name = 'newcommodity'
urlpatterns = [
    path('', views.showCreateTextForm, name='index'),
    #ユーザ登録する処理を呼び出す
    path('add', views.addText, name='addText'),
]