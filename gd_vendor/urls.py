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
from gd_vendor import views
from gd_vendor.models import VendorRegister, Space, Dispatcher

urlpatterns = [
        path('vendor_register/',TemplateView.as_view(template_name='gd_vendor/vendor_register.html'),name='vendor_register'),
        path('save_vendor/',views.save_Vendor,name='save_vendor'),
        path('vendor_home/',TemplateView.as_view(template_name='gd_vendor/vendor_home.html'),name='vendor_home'),
        path('vendor_request_for_menu/', TemplateView.as_view(template_name='gd_vendor/vendor_request_for_menu.html'),name='vendor_request_for_menu'),
        path('vendor_request_for_space/',views.vendor_request_for_space,name='vendor_request_for_space'),
        path('save_space/',views.save_Space,name='save_space'),
        path('vendor_request_for_dispatcher/', views.vendor_request_for_dispatcher,name='vendor_request_for_dispatcher'),
        path('save_dispatcher/',views.save_Dispatcher,name='save_dispatcher'),
        path('vendor_payments_menu/',TemplateView.as_view(template_name='gd_vendor/vendor_payments_menu.html'),name='vendor_payments_menu'),
        path('vendor_reports_menu/',TemplateView.as_view(template_name='gd_vendor/vendor_reports_menu.html'),name='vendor_reports_menu'),
        path('vendor_bill_reports/',ListView.as_view(template_name='gd_vendor/vendor_bill_reports.html',model=Bill_Generation),name='vendor_bill_reports'),
        path('vendor_make_payments/',ListView.as_view(template_name='gd_vendor/vendor_make_payments.html',model=Bill_Generation),name='vendor_make_payments'),
        path('make_payments/',views.make_Payments,name='make_payments'),
        path('vendor_reports_menu/',TemplateView.as_view(template_name='gd_vendor/vendor_reports_menu.html'),name='vendor_reports_menu'),
        path('vendor_space_reports/',ListView.as_view(template_name='gd_vendor/vendor_space_reports.html',model=Space),name='vendor_space_reports'),
        path('vendor_dispatcher_reports/',ListView.as_view(template_name='gd_vendor/vendor_dispatcher_reports.html',model=Dispatcher),name='vendor_dispatcher_reports'),
        path('',views.vendor_Logout,name='vendor_logout'),
        path('vendor_mail_menu/',TemplateView.as_view(template_name='gd_vendor/vendor_email_menu.html'),name='vendor_mail_menu'),
        path('vendor_compose_mail/',TemplateView.as_view(template_name='gd_vendor/vendor_compose_mail.html'),name='vendor_compose_mail'),
        path('vendor_inbox/', views.vendor_Inbox, name='vendor_inbox'),
        path('vendor_delete_mail/',views.vendor_Delete_Mail,name='vendor_delete_mail'),
        path('vendor_view_profile/',views.vendor_View_Profile,name='vendor_view_profile'),

]
