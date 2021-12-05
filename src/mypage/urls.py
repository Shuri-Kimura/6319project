from django.urls import path

from . import views

app_name = 'mypage'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.MypageView.as_view(), name='mypage'),
    path('<int:pk>/edit/', views.CommentUpdate.as_view(), name='edit'),
    path('<int:pk>/delete_list/', views.DeleteList.as_view(), name='delete_list'),
    path('<int:pk>/delete/', views.DeleteText.as_view(), name='delete'),
]
