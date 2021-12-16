from django.urls import path
from . import views

app_name ='search'
urlpatterns = [
    path('', views.index, name='index'),
    path('tlike/', views.TlikeView, name='tlike'),
    path('clike/', views.ClikeView, name='clike'),
]