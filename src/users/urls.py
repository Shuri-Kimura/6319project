from django.urls import path #関係ない
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.AccountRegistration.as_view(), name='registration'),
]