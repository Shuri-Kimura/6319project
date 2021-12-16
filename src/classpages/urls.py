from django.urls import path

from . import views
app_name = 'classpages'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.Classpage, name='class'),
    path('<int:pk>/Ceval/', views.addceval, name='ceval'),
    path('create/', views.createclass, name='create'),
]
