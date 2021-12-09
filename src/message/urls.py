from django.urls import path

from . import views

app_name = 'message'
urlpatterns = [
    path('<int:pk>/', views.MessageList.as_view(), name='message'),
    path('detail/<int:pk>/', views.MessageDetail.as_view(), name='detail'),
]
