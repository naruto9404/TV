"""Mehram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path,include

admin.site.site_header = "THE OTAKU'S STORE Admin"
admin.site.index_title = "THE OTAKU'S STORE Admin Portal"
admin.site.site_title = "Welcome To THE OTAKU'S STORE "


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('home.urls'))
    

    #herewe included a path which tells us that if with the link 
    #name we do not write admin and keep it blank then please send the user to the rrr.urls 
    #and we need to do it in the project urls not in the app urls.
]
