from django.contrib import messages
from django.shortcuts import render, redirect

from gd_accountant.models import Bill_Generation
from gd_admin.models import GoDown, Employee
from gd_login.models import Inbox_Mails
from gd_vendor.models import VendorRegister, Space, Dispatcher, Payments


def save_Vendor(request):
    vendor_id = request.POST.get('vendor_id')
    vendor_name = request.POST.get('vendor_name')
    company_name = request.POST.get('company_name')
    company_address = request.POST.get('company_address')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')

    VendorRegister(vendor_id=vendor_id,vendor_name=vendor_name,company_name=company_name,company_address=company_address,contact_no=contact,email_id=email,username=username,password=password,status='Pending').save()
    return render(request,'gd_vendor/vendor_register.html',{'message':'Registered Successfully'})

def save_Space(request):
    vendor_id = request.POST.get('vendor_id')
    product_name = request.POST.get('product_name')
    product_capacity = request.POST.get('product_capacity')
    godown_id = request.POST.get('godown_id')

    Space(vendor_id=vendor_id,product_name=product_name,product_capacity=product_capacity,godown_id=godown_id).save()
    return render(request,'gd_vendor/vendor_request_for_space.html',{'message':"Saved Successfully"})


def vendor_request_for_space(request):
    qs = VendorRegister.objects.filter(status='Active')
    qs1 = GoDown.objects.all()
    return render(request,'gd_vendor/vendor_request_for_space.html',{'vendor_id':qs,'godown_id':qs1})

def vendor_request_for_dispatcher(request):
    qs = VendorRegister.objects.filter(status='Active')
    return render(request,'gd_vendor/vendor_request_for_dispatcher.html',{'vendor_id':qs})

def save_Dispatcher(request):
    vendor_id = request.POST.get('vendor_id')
    product_name = request.POST.get('product_name')
    product_capacity = request.POST.get('product_capacity')
    address = request.POST.get('address')
    customer_name = request.POST.get('customer_name')

    Dispatcher(vendor_id=vendor_id,product_name=product_name,product_capacity=product_capacity,address=address,customer_name=customer_name).save()
    return render(request,'gd_vendor/vendor_request_for_dispatcher.html',{'message':"Dispatched Successfully"})

def make_Payments(request):
    vendor_name = request.POST.get('vendor_name')
    bill_id = request.POST.get('bill_id')
    amount = request.POST.get('amount')
    payment_type = request.POST.get('paymant_type')
    number = request.POST.get('number')

    Payments(vendor_name=vendor_name,bill_id=bill_id,amount=amount,payment_type=payment_type,number=number).save()
    Bill_Generation.objects.filter(bill_id=bill_id).update(status="Paid")
    return render(request,'gd_vendor/vendor_make_payments.html',{'message':"Paid"})


def vendor_Logout(request):
    del request.session['username']
    return redirect('index')


def vendor_Inbox(request):
    name = request.session['username']
    qs = VendorRegister.objects.filter(username=name)
    email = qs[0].email_id
    qs1 = Inbox_Mails.objects.filter(to=email)
    return render(request,'gd_vendor/vendor_inbox.html',{'object_list':qs1})

def vendor_Delete_Mail(request):
    name = request.session['username']
    mail_id = request.POST.get('mail_id')
    print(name,mail_id)
    Inbox_Mails.objects.filter(mail_id=mail_id).delete()
    qs = VendorRegister.objects.filter(username=name)
    email = qs[0].email_id
    qs1 = Inbox_Mails.objects.filter(to=email)
    return render(request,'gd_vendor/vendor_inbox.html',{'object_list':qs1})


def vendor_View_Profile(request):
    name = request.session['username']
    qs = VendorRegister.objects.filter(username=name)
    print(qs[0].vendor_name,qs[0].company_name)
    return render(request, 'gd_vendor/vendor_view_profile.html', {'vendor_data': qs})
