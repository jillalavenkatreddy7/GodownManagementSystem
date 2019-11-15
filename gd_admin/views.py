from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Employee,GoDown,Admin
from gd_login.models import Login,Inbox_Mails
from gd_vendor.models import VendorRegister


def admin_Logout(request):
    del request.session['username']
    return redirect('index')

def admin_Employee(request):
    qs = Employee.objects.all()
    return render(request, 'gd_admin/admin_employee.html', {'employee_data': qs})

def admin_Add_Employee(request):
    name = request.POST.get('name')
    designation = request.POST.get('designation')
    address = request.POST.get('address')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    username = request.POST.get('username')
    password = request.POST.get('password')

    Login(username=username,password=password,usertype=designation).save()
    Employee(name=name, designation=designation, address=address, email=email, contact=contact, username=username,password=password).save()

    qs = Employee.objects.all()
    return render(request, 'gd_admin/admin_employee.html', {'employee_data': qs,'message':'Employee Added'})

def view_Employee(request):
    username = request.POST.get('username')
    qs = Employee.objects.filter(username=username)
    return render(request, 'gd_admin/view_employee.html', {'employee_data': qs})

def update_Employee(request):
    username = request.POST.get('username')
    qs = Employee.objects.filter(username=username)
    return render(request, 'gd_admin/admin_update_employee.html', {'employee_data': qs})

def admin_Update_Employee(request):
    name = request.POST.get('name')
    designation = request.POST.get('designation')
    address = request.POST.get('address')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    username = request.POST.get('username')
    password = request.POST.get('password')

    Employee(name=name,designation=designation,address=address,email=email,contact=contact,username=username,password=password).save()

    qs = Employee.objects.all()
    return render(request, 'gd_admin/admin_employee.html', {'employee_data': qs})

def admin_Delete_Employee(request):
    username = request.POST.get('username')
    qs = Employee.objects.filter(username=username)

    Employee.objects.filter(username=username).delete()
    Login.objects.filter(username=username).delete()

    qs = Employee.objects.all()
    return render(request, 'gd_admin/admin_employee.html', {'employee_data': qs})

def admin_GoDown(request):
    qs = GoDown.objects.all()
    qs1 = Employee.objects.filter(designation='GoDown Manager')
    qs2 = Employee.objects.filter(designation='Inventory Manager')
    return render(request,'gd_admin/admin_godown.html',{'godown_data':qs,'gd_manager_name':qs1,'inventory_name':qs2})

def admin_Add_GoDown(request):
    godown_id = request.POST.get('godown_id')
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    godown_manager = request.POST.get('godown_manager')
    inventory_manager = request.POST.get('inventory_manager')

    if godown_manager == '--Select--' and inventory_manager == '--Select--':
        qs = GoDown.objects.all()
        qs1 = Employee.objects.filter(designation='GoDown Manager')
        qs2 = Employee.objects.filter(designation='Inventory Manager')

        return render(request, 'gd_admin/admin_godown.html',{'godown_data': qs, 'gd_manager_name': qs1, 'inventory_name': qs2,'msg': "Please Select Manager's"})

    elif godown_manager == '--Select--':
        qs = GoDown.objects.all()
        qs1 = Employee.objects.filter(designation='GoDown Manager')
        qs2 = Employee.objects.filter(designation='Inventory Manager')

        return render(request, 'gd_admin/admin_godown.html',{'godown_data': qs, 'gd_manager_name': qs1, 'inventory_name': qs2,'msg': 'Please Select GoDown Manager'})

    elif inventory_manager == '--Select--':
        qs = GoDown.objects.all()
        qs1 = Employee.objects.filter(designation='GoDown Manager')
        qs2 = Employee.objects.filter(designation='Inventory Manager')

        return render(request, 'gd_admin/admin_godown.html',{'godown_data': qs, 'gd_manager_name': qs1, 'inventory_name': qs2,'msg':'Please Select Inventory Manager'})
    else:
        GoDown(godown_id=godown_id,location=location,capacity=capacity,godown_manager=godown_manager,inventory_manager=inventory_manager).save()
        qs = GoDown.objects.all()
        qs1 = Employee.objects.filter(designation='GoDown Manager')
        qs2 = Employee.objects.filter(designation='Inventory Manager')

    return render(request,'gd_admin/admin_godown.html',{'godown_data':qs,'gd_manager_name':qs1,'inventory_name':qs2,'message':'GoDown Added'})

def update_GoDown(request):
    godown_id = request.POST.get('godown_id')
    qs = GoDown.objects.filter(godown_id=godown_id)
    qs1 = Employee.objects.filter(designation='GoDown Manager')
    qs2 = Employee.objects.filter(designation='Inventory Manager')
    return render(request,'gd_admin/update_godown.html',{'update_godown_data':qs,'gd_manager_name':qs1,'inventory_name':qs2})

def confirm_Update_GoDown(request):
    godown_id = request.POST.get('godown_id')
    location = request.POST.get('location')
    capacity = request.POST.get('capacity')
    godown_manager = request.POST.get('godown_manager')
    inventory_manager = request.POST.get('inventory_manager')

    GoDown(godown_id=godown_id, location=location, capacity=capacity, godown_manager=godown_manager,inventory_manager=inventory_manager).save()
    qs = GoDown.objects.all()
    qs1 = Employee.objects.filter(designation='GoDown Manager')
    qs2 = Employee.objects.filter(designation='Inventory Manager')
    return render(request, 'gd_admin/admin_godown.html', {'godown_data': qs,'gd_manager_name':qs1,'inventory_name':qs2})

def delete_GoDown(request):
    godown_id = request.POST.get('godown_id')
    GoDown.objects.filter(godown_id=godown_id).delete()
    qs = GoDown.objects.all()
    qs1 = Employee.objects.filter(designation='GoDown Manager')
    qs2 = Employee.objects.filter(designation='Inventory Manager')
    return render(request, 'gd_admin/admin_godown.html', {'godown_data': qs,'gd_manager_name':qs1,'inventory_name':qs2})


def admin_Pending_Vendors(request):
    qs = VendorRegister.objects.filter(status='Pending')
    return render(request,'gd_admin/admin_pending_vendors.html',{'object_list':qs})

def view_Vendor(request):
    vendor_id = request.POST.get('vendor_id')
    qs = VendorRegister.objects.filter(vendor_id=vendor_id)
    return render(request,'gd_admin/admin_view_pending_vendor.html',{'vendor_data':qs})

def admin_Accept_Vendor(request):
    vendor_id = request.POST.get('vendor_id')
    vendor_name = request.POST.get('vendor_name')
    company_name = request.POST.get('company_name')
    company_address = request.POST.get('company_address')
    contact = request.POST.get('contact')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password = request.POST.get('password')

    Login(username=username,password=password,usertype='Vendor').save()
    VendorRegister.objects.filter(vendor_id=vendor_id).update(status='Active')
    qs = VendorRegister.objects.filter(status='Pending')
    return render(request, 'gd_admin/admin_pending_vendors.html', {'object_list': qs})


def admin_Reject_Vendor(request):
    vendor_id = request.POST.get('vendor_id')
    VendorRegister.objects.filter(vendor_id=vendor_id).delete()
    qs = VendorRegister.objects.filter(status='Pending')
    return render(request, 'gd_admin/admin_pending_vendors.html', {'object_list': qs})


def admin_Inbox(request):
    name = request.session['username']
    email = 'admin@gmail.com'
    qs1 = Inbox_Mails.objects.filter(to=email)
    return render(request,'gd_admin/admin_inbox.html',{'object_list':qs1})


def admin_Change_Password(request):
    old_password = request.POST.get('old_password')
    new_password = request.POST.get('new_password')
    comfirm_password = request.POST.get('confirm_password')

    qs = Admin.objects.filter(password=old_password)
    if qs:
        if new_password == comfirm_password:
            Login.objects.filter(username='admin').update(password=new_password)
            Admin.objects.filter(username='admin').update(password=new_password)
            return redirect('admin_view_profile')
        else:
            messages.error(request,"New Password and Confirm Password are didn't match")
            return redirect('admin_change_password')
    else:
        messages.error(request, "Entered Wrong Password")
        return redirect('admin_change_password')

def admin_Delete_Mail(request):
    name = request.session['username']
    mail_id = request.POST.get('mail_id')
    Inbox_Mails.objects.filter(mail_id=mail_id).delete()
    qs = Inbox_Mails.objects.filter(to='admin@gmail.com')
    return render(request,'gd_admin/admin_inbox.html',{'object_list':qs})

