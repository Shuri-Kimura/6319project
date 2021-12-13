"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', include('search.urls')),
    path('newcommodity/', include('newcommodity.urls')),
    path('like/', include('like.urls')),
    path('mypage/',include('mypage.urls')),
    path('textpage/',include('textpage.urls')),
    path('',include('users.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('classpages/',include('classpages.urls')),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), name='password_change'), # 追加
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('message/',include('message.urls')),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)