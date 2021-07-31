"""pandaBackend URL Configuration

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
from django.urls import path, re_path
# 2021.7.23
from api_test import views



urlpatterns = [
    path('admin/', admin.site.urls),
# 2021.7.23
    path('test/', views.Hello.as_view()),
    # 2021.7.30
    path('videos/', views.VideoList.as_view()),
    #2021.7.31
    # re_path('video/', views.VideoDetail.as_view())
    re_path(r'^video1/(?P<name>\w+)/', views.VideoDetail2.as_view())
]
