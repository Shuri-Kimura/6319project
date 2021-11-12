from django.urls import path
#from .views import IndexView
from . import views

app_name = 'textpage'
urlpatterns = [
  #path('', IndexView.as_view())
 path('', views.TextpageListView.as_view(), name='textpage'),
]


#from django.urls import path
#from . import views
#from .views import IndexView


#urlpatterns = [
 #   path('', IndexView.as_view()),
    #path('', views.index, name='index'),
#]