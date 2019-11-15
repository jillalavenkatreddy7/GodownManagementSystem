"""GoDown_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='gd_home/index.html'), name='index'),
    path('login/', TemplateView.as_view(template_name='gd_home/login.html'), name='login'),
    path('aboutus/', TemplateView.as_view(template_name='gd_home/about_us.html'), name='about_us'),
    path('contact_us/', TemplateView.as_view(template_name='gd_home/contact_us.html'), name='contact_us'),

    path('gd_admin/',include('gd_admin.urls')),
    path('gd_login/',include('gd_login.urls')),
    path('gd_vendor/',include('gd_vendor.urls')),
    path('gd_manager/',include('gd_manager.urls')),
    path('gd_inventory/',include('gd_inventory.urls')),
    path('gd_accountant/',include('gd_accountant.urls')),

]
