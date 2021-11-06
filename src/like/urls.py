from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'like'
urlpatterns = [
    #path('', views.LikeListView.as_view(), name='like'),
    path('', views.LikeListView.as_view(), name='like'),
    path('likely/', views.LikelyListView.as_view(), name='likely'),
]