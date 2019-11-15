from django.contrib import messages
from django.shortcuts import render, redirect
from gd_admin.models import Employee
from gd_login.models import Inbox_Mails

def manager_Inbox(request):
    name = request.session['username']
    qs = Employee.objects.filter(username=name)
    email = qs[0].email
    qs1 = Inbox_Mails.objects.filter(to=email)
    return render(request,'gd_manager/manager_inbox.html',{'object_list':qs1})

def manager_Logout(request):
    del request.session['username']
    return redirect('index')

def manager_Delete_Mail(request):
    name = request.session['username']
    mail_id = request.POST.get('mail_id')
    print(name,mail_id)
    Inbox_Mails.objects.filter(mail_id=mail_id).delete()
    qs = Employee.objects.filter(username=name)
    email = qs[0].email
    qs1 = Inbox_Mails.objects.filter(to=email)
    return render(request,'gd_manager/manager_inbox.html',{'object_list':qs1})


def manager_View_Profile(request):
    name = request.session['username']
    qs = Employee.objects.filter(username=name)
    return render(request, 'gd_manager/manager_view_profile.html', {'namager_data': qs})
