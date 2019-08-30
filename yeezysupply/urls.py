"""yeezysupply URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from bypass import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('bypass/', views.bypass_list, name='bypass'),
    path('monitor/', views.shop_monitor, name='monitor'),
    path('makeBypass/', views.button_bypass, name='makeBypass'),
    path('addBot/', views.add_bot, name='addBot'),
    path('massURL/', views.mass_urls, name='massURL'),
    path('delBot/', views.del_bot, name='delBot'),
    path('fog/', views.fog, name='fog'),
    path('atc/', views.atc, name='atc'),
    path('checkAutoBp/', views.check_auto_bp, name='checkAutoBp'),
    path('ysautobp/', views.ys_autobp, name='ysautobp'),
    path('proxy/', views.proxy, name='proxy'),
]
