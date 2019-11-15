from django.contrib import messages
from django.shortcuts import render, redirect

from gd_admin.models import Employee
from gd_login.models import Inbox_Mails


def inventory_Logout(request):
    del request.session['username']
    return redirect('index')


def inventory_Inbox(request):
    name = request.session['username']
    qs = Employee.objects.filter(username=name)
    email = qs[0].email
    qs1 = Inbox_Mails.objects.filter(to=email)
    return render(request,'gd_inventory/inventory_inbox.html',{'object_list':qs1})

def inventory_Delete_Mail(request):
    name = request.session['username']
    mail_id = request.POST.get('mail_id')
    print(name,mail_id)
    Inbox_Mails.objects.filter(mail_id=mail_id).delete()
    qs = Employee.objects.filter(username=name)
    email = qs[0].email
    qs1 = Inbox_Mails.objects.filter(to=email)
    return render(request,'gd_inventory/inventory_inbox.html',{'object_list':qs1})


def inventory_View_Profile(request):
    name = request.session['username']
    qs = Employee.objects.filter(username=name)
    return render(request, 'gd_inventory/inventory_view_profile.html', {'inventory_data': qs})
