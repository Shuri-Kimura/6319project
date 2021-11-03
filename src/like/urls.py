from django.urls import path
from . import views


app_name = 'like'
urlpatterns = [
    path('', views.like, name='like'),
    path('likely/', views.likely, name='likely'),
]