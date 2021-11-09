from django.urls import path

from . import views

app_name = 'mypage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.MypageView.as_view(), name='mypage'),
    path('edit/', views.edit, name='edit'),
]
