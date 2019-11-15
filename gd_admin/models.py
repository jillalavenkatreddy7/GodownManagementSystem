from django.db import models

class Vendor_Register(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    address = models.TextField(max_length=400)
    email = models.EmailField()
    contact = models.IntegerField()
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=50)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    address = models.TextField(max_length=400)
    email = models.EmailField()
    contact = models.IntegerField()
    username = models.CharField(max_length=30,primary_key=True)
    password = models.CharField(max_length=50)

class GoDown(models.Model):
    godown_id = models.IntegerField(primary_key=True)
    location = models.CharField(max_length=30)
    capacity = models.IntegerField()
    godown_manager = models.CharField(max_length=50)
    inventory_manager = models.CharField(max_length=50)

class Admin(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=30)
    address = models.TextField(max_length=400)
    email = models.EmailField()
    contact = models.IntegerField()
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=50)

