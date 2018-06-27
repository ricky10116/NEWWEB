"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app1 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index.html$', views.index),  
    url(r'page1.html$', views.page1),
    url(r'12345$', views.Addtext),
    
]
# http://127.0.0.1:8000/index.html
# http://127.0.0.1:8000/index/page1.html