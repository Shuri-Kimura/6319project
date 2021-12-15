from django.urls import path
from django.conf.urls import url
from . import views
from users.models import Tfavos, Cfavos, Classes, Texts, Tcom

app_name = 'textpage'
urlpatterns = [
    #path('', IndexView.as_view())
    #path('', views.TextpageView.as_view(), name='textpage'),
    path('<int:pk>/', views.TextpageView.as_view(), name='textpage'),
    path('<int:pk>/AddCom/', views.addCom, name='addCom'),
    path('<int:pk>/TransActionList/',
         views.TransActionList, name='TransActionList'),
    path('<int:text_pk>/UserEvalutate/<int:user_pk>',
         views.UserEvaluate, name='Evaluate'),
    path('<int:text_pk>/TransAction/<int:user_pk>',
         views.TransAction, name='TransAction'),
]


#from django.urls import path
#from . import views
#from .views import IndexView


# urlpatterns = [
#   path('', IndexView.as_view()),
#path('', views.index, name='index'),
# ]
