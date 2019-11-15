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
from django.urls import path
from django.views.generic import TemplateView, ListView

from gd_inventory import views
from gd_vendor.models import Dispatcher

urlpatterns = [
    path('inventory_home/',TemplateView.as_view(template_name='gd_inventory/inventory_home.html'),name='inventory_home'),
    path('inventory_logout/',views.inventory_Logout,name='inventory_logout'),
    path('inventory_product_reports/',ListView.as_view(template_name='gd_inventory/inventory_product_reports.html',model=Dispatcher),name='inventory_product_reports'),
    path('inventory_mail_menu/',TemplateView.as_view(template_name='gd_inventory/inventory_mail_menu.html'),name='inventory_mail_menu'),
    path('inventory_compose_mail/',TemplateView.as_view(template_name='gd_inventory/inventory_compose_mail.html'),name='inventory_compose_mail'),
    path('inventory_inbox/',views.inventory_Inbox,name='inventory_inbox'),
    path('inventory_delete_mail/',views.inventory_Delete_Mail,name='inventory_delete_mail'),
    path('inventory_view_profile/',views.inventory_View_Profile,name='inventory_view_profile'),


]
