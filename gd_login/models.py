from django.db import models

class Login(models.Model):
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=30)
    usertype = models.CharField(max_length=30)

class Inbox_Mails(models.Model):
    mail_id = models.AutoField(primary_key=True)
    frm = models.CharField(max_length=30)
    to = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    body = models.TextField(max_length=200)
