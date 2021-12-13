from django.urls import path

from . import views
app_name = 'classpages'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.Classpage.as_view(), name='class'),
    path('<int:pk>/Ccom/', views.addccom, name='ccom'),
    path('create/', views.createclass, name='create'),
]