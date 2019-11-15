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

from gd_accountant.models import Bill_Generation
from gd_manager import views
from gd_vendor.models import Dispatcher, Space, Payments, VendorRegister

urlpatterns = [
    path('godowm_manager_home/', TemplateView.as_view(template_name='gd_manager/godown_manager_home.html'), name='godown_manager_home'),
    path('manager_logout/',views.manager_Logout,name='manager_logout'),
    path('godown_reports/',TemplateView.as_view(template_name='gd_manager/manager_reports_menu.html'),name='manager_reports_menu'),
    path('manager_email_menu/',TemplateView.as_view(template_name='gd_manager/manager_email_menu.html'),name='manager_email_menu'),
    path('manager_compose_mail/',TemplateView.as_view(template_name='gd_manager/manager_compose_mail.html'),name='manager_compose_mail'),
    path('manager_inbox/',views.manager_Inbox,name='manager_inbox'),
    path('manager_bill_reports/',ListView.as_view(model=Bill_Generation,template_name='gd_manager/manager_bill_reports.html'),name='manager_bill_reports'),
    path('manager_pending_bills/',ListView.as_view(model=Bill_Generation,template_name='gd_manager/manager_bill_reports.html',queryset=Bill_Generation.objects.filter(status='Pending')),name='manager_pending_bills'),
    path('manager_delivery_reports/',ListView.as_view(template_name='gd_manager/manager_deliver_reports.html',model=Dispatcher),name='manager_delivery_reports'),
    path('manager_product_reports/',ListView.as_view(template_name='gd_manager/manager_product_reports.html',model=Space),name='manager_product_reports'),
    path('manager_payments_reports/',ListView.as_view(template_name='gd_manager/manager_payments_reports.html',model=Payments),name='manager_payments_reports'),
    path('manager_vendor_reports/',ListView.as_view(template_name='gd_manager/manager_vendor_reports.html',model=VendorRegister,queryset=VendorRegister.objects.filter(status='Active')),name='manager_vendor_reports'),
    path('manager_delete_mail/',views.manager_Delete_Mail,name='manager_delete_mail'),
    path('manager_view_profile/',views.manager_View_Profile,name='manager_view_profile'),

]
