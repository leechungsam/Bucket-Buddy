"""chongzaban URL Configuration

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
from chongzaban import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('accounts/', include('allauth.urls')), # allauth
    path('buckets/', include('buckets.urls')), # bucketlist
    path('user/', include('user.urls')), # user
    path('room/', include('room.urls')), # 채팅방
    path('board/', include('board.urls')),#게시판
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
