from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'textpage'
urlpatterns = [
  #path('', IndexView.as_view())
 path('', views.TextpageView.as_view(), name='textpage'),
]


#from django.urls import path
#from . import views
#from .views import IndexView


#urlpatterns = [
 #   path('', IndexView.as_view()),
    #path('', views.index, name='index'),
#]