"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path, include
import prova.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('you_are_in/', prova.views.you_are_in),
    path('sign_up/', prova.views.sign_up),
    path('logout/', prova.views.logout),
    path('', prova.views.hello_world),
    path('', include('django.contrib.auth.urls')),
]


urlpatterns += staticfiles_urlpatterns()

