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
from gd_admin import views
from gd_admin.models import Admin
from gd_vendor.models import VendorRegister, Dispatcher, Payments

urlpatterns = [
    path('admin_home/', TemplateView.as_view(template_name='gd_admin/admin_home.html'), name='admin_home'),
    path('admin_vendor/',views.admin_Pending_Vendors,name='admin_pending_vendors'),
    path('admin_logout/',views.admin_Logout,name='admin_logout'),
    path('delete_vendor/', views.admin_Reject_Vendor,name='admin_reject_vendor'),
    path('accept_vendor/', views.admin_Accept_Vendor, name='admin_accept_vendor'),
    path('view_vendor/', views.view_Vendor, name='admin_view_pending_vendor'),
    path('admin_godown/', views.admin_GoDown, name='admin_godown'),
    path('admin_add_godown/', views.admin_Add_GoDown, name='admin_add_godown'),
    path('delete_godown/', views.delete_GoDown, name='admin_delete_godown'),
    path('update_godown/', views.update_GoDown, name='update_godown'),
    path('confirm_update_godown/', views.confirm_Update_GoDown, name='confirm_update_godown'),
    path('admin_employee/',views.admin_Employee,name='admin_employee'),
    path('admin_add_employee/',views.admin_Add_Employee,name='admin_add_employee'),
    path('admin_view_employee/',views.view_Employee,name='admin_view_employee'),
    path('update_employee/',views.update_Employee,name='update_employee'),
    path('admin_update_employee/',views.admin_Update_Employee,name='admin_update_employee'),
    path('admin_delete_employee/',views.admin_Delete_Employee,name='admin_delete_employee'),
    path('admin_reports_menu/',TemplateView.as_view(template_name='gd_admin/admin_reports_menu.html'),name='admin_reports_menu'),
    path('admin_mail_menu/', TemplateView.as_view(template_name='gd_admin/admin_mail_menu.html'),name='admin_mail_menu'),
    path('admin_compose_mail/', TemplateView.as_view(template_name='gd_admin/admin_compose_mail.html'),name='admin_compose_mail'),
    path('admin_inbox/',views.admin_Inbox,name='admin_inbox'),
    path('admin_delivery_reports/',ListView.as_view(template_name='gd_admin/admin_delivery_reports.html',model=Dispatcher),name='admin_delivery_reports'),
    path('admin_product_reports/',ListView.as_view(template_name='gd_admin/admin_product_reports.html',model=Dispatcher),name='admin_product_reports'),
    path('admin_payments_reports/',ListView.as_view(template_name='gd_admin/admin_payments_reports.html',model=Payments),name='admin_payments_reports'),
    path('admin_bill_reports/',ListView.as_view(model=Bill_Generation,template_name='gd_admin/admin_bill_reports.html'),name='admin_bill_reports'),
    path('admin_pending_bills/',ListView.as_view(model=Bill_Generation,template_name='gd_admin/admin_bill_reports.html',queryset=Bill_Generation.objects.filter(status='Pending')),name='admin_pending_bills'),
    path('admin_vendor_reports/',ListView.as_view(template_name='gd_admin/admin_vendor_reports.html',model=VendorRegister,queryset=VendorRegister.objects.filter(status='Active')),name='admin_vendor_reports'),
    path('admin_profile_menu/',TemplateView.as_view(template_name='gd_admin/admin_profile_menu.html'),name='admin_profile_menu'),
    path('admin_view_profile/',ListView.as_view(template_name='gd_admin/admin_view_profile.html',model=Admin),name='admin_view_profile'),
    path('admin_change_password/',TemplateView.as_view(template_name='gd_admin/admin_change_password.html'),name='admin_change_password'),
    path('change_password/',views.admin_Change_Password,name='change_password'),
    path('admin_delete_mail/',views.admin_Delete_Mail,name='admin_delete_mail')

]
