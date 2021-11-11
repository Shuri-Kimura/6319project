from django.urls import path
from . import views


urlpatterns = [
    path('', views.NewcommodityView.as_view(), name='index'),
]