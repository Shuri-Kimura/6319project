from django.urls import path
#from . import views
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    #path('', views.index, name='index'),
]