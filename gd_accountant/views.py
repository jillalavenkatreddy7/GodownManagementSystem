from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView

from gd_accountant.models import Bill_Generation
from gd_admin.models import Employee
from gd_login.models import Inbox_Mails
from gd_vendor.models import VendorRegister

def accountant_logout(request):
    del request.session['username']
    return redirect('index')

def accountant_Bill_Generation(request):
    qs = VendorRegister.objects.filter(status='Active')
    return render(request, 'gd_accountant/accountant_bill_generation.html', {'vendor_data': qs})


def accountant_Generation_Bill(request):
    vendor_name = request.POST.get('vendor_name')
    product_name = request.POST.get('product_name')
    bill_gen_date = request.POST.get('bill_gen_date')
    amount = request.POST.get('amount')

    Bill_Generation(vendor_name=vendor_name, product_name=product_name, bill_gen_date=bill_gen_date,amount=amount,status='Pending').save()
    return redirect('accountant_bill_generated')


def accountant_Inbox(request):
    name = request.session['username']
    qs = Employee.objects.filter(username=name)
    email = qs[0].email
    qs1 = Inbox_Mails.objects.filter(to=email)
    return render(request,'gd_accountant/accountant_inbox.html',{'object_list':qs1})

def accountant_Delete_Mail(request):
    name = request.session['username']
    mail_id = request.POST.get('mail_id')
    print(name,mail_id)
    Inbox_Mails.objects.filter(mail_id=mail_id).delete()
    qs = Employee.objects.filter(username=name)
    email = qs[0].email
    qs1 = Inbox_Mails.objects.filter(to=email)
    return render(request,'gd_accountant/accountant_inbox.html',{'object_list':qs1})


def accountant_View_Profile(request):
    name = request.session['username']
    qs = Employee.objects.filter(username=name)
    return render(request, 'gd_accountant/accountant_view_profile.html', {'accountant_data': qs})
