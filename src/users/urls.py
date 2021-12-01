from django.urls import path #関係ない

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.AccountRegistration.as_view(), name='registration'),
    #path('', views.Top.as_view(), name='top'),
    #path('login/', views.Login.as_view(), name='login'),
    #path('logout/', views.Logout.as_view(), name='logout'),
]