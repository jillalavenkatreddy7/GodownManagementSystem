from django.db import models

class VendorRegister(models.Model):
    vendor_id = models.IntegerField(primary_key=True)
    vendor_name = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    company_address = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email_id = models.EmailField(max_length=100)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    status = models.CharField(max_length=30)

class Space(models.Model):
    space_id = models.AutoField(primary_key=True)
    vendor_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_capacity = models.DecimalField(max_digits=10,decimal_places=2)
    godown_id = models.IntegerField()

class Dispatcher(models.Model):
    Dispatcher_id = models.AutoField(primary_key=True)
    vendor_id = models.IntegerField()
    product_name = models.CharField(max_length=50)
    product_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField(max_length=300)
    customer_name = models.CharField(max_length=50)

class Payments(models.Model):
    payment_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=50)
    bill_id = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50,null=True)
    number = models.IntegerField()
