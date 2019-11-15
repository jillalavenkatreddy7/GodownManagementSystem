from django.contrib import messages
from django.shortcuts import render, redirect

from gd_admin.models import Employee
from gd_login.models import Login, Inbox_Mails


def login_Check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    usertype = request.POST.get('usertype')

    qs = Login.objects.filter(username=username,password=password,usertype=usertype)
    if qs:
        if usertype == 'Administrator':
            request.session['username'] = username
            return redirect('admin_home')

        elif usertype == 'GoDown Manager':
            request.session['status'] = True
            request.session['username'] = username
            return redirect('godown_manager_home')

        elif usertype == 'Vendor':
            request.session['username'] = username
            # return HttpResponse('Vendor Page')
            return redirect('vendor_home')

        elif usertype == 'Inventory Manager':
            request.session['username'] = username
            # return HttpResponse('Inventory Manager Page')
            return redirect('inventory_home')

        else:
            request.session['status'] = True
            request.session['username'] = username
            # return HttpResponse('Accountant Page')
            return redirect('accountant_home')

    else:
        messages.error(request,"Invalid Details")
        return redirect('login')


def send_Mail(request):
    frm = request.POST.get('frm')
    to = request.POST.get('to')
    subject = request.POST.get('subject')
    body = request.POST.get('body')
    type = request.POST.get('type')

    Inbox_Mails(frm=frm, to=to, subject=subject, body=body).save()
    messages.error(request, 'Mail Sent')

    if type == "Administrator":
        return redirect('admin_compose_mail')

    elif type == "GoDown Manager":
        return redirect('manager_compose_mail')

    elif type == 'Inventory Manager':
        return redirect('inventory_compose_mail')

    elif type == 'Accountant':
        return redirect('accountant_compose_mail')

    else:
        return redirect('vendor_compose_mail')

