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
from gd_accountant import views
from gd_accountant.models import Bill_Generation
from gd_admin.models import Employee
from gd_vendor.models import Payments

urlpatterns = [
    path('accountant_home/',TemplateView.as_view(template_name='gd_accountant/accountant_home.html'),name='accountant_home'),
    path('accountant_logout/',views.accountant_logout,name='accountant_logout'),
    path('accountant_reports_menu/',TemplateView.as_view(template_name='gd_accountant/accountant_reports_menu.html'),name='accountant_reports_menu'),
    path('accountant_bill_generation/',views.accountant_Bill_Generation,name='accountant_bill_generation'),
    path('accountant_generate_bill/',views.accountant_Generation_Bill,name='accountant_generate_bill'),
    path('accountant_bill_generated/',TemplateView.as_view(template_name='gd_accountant/accountant_bill_generated.html'),name='accountant_bill_generated'),
    path('accountant_mail_menu/',TemplateView.as_view(template_name='gd_accountant/accountant_mail_menu.html'),name='accountant_mail_menu'),
    path('accountant_compose_mail/',TemplateView.as_view(template_name='gd_accountant/accounatant_compose_mail.html'),name='accountant_compose_mail'),
    path('accountant_inbox/',views.accountant_Inbox,name='accountant_inbox'),
    path('accountant_view_bills/',ListView.as_view(model=Bill_Generation,template_name='gd_accountant/accountant_view_bills.html'),name='accountant_view_bills'),
    path('accountant_payments_reports/',ListView.as_view(template_name='gd_accountant/accountant_view_payments.html',model=Payments),name='accountant_payments_reports'),
    path('accountant_pending_bills/',ListView.as_view(model=Bill_Generation,template_name='gd_accountant/accountant_view_bills.html',queryset=Bill_Generation.objects.filter(status='Pending')),name='accountant_pending_bills'),
    path('accountant_delete_mail/',views.accountant_Delete_Mail,name='accountant_delete_mail'),
    path('accountant_view_profile/',views.accountant_View_Profile,name='accountant_view_profile'),


]
