from django.db import models

class Bill_Generation(models.Model):
    bill_id = models.AutoField(primary_key=True)
    vendor_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    bill_gen_date = models.DateField()
    amount = models.DecimalField(max_digits=20,decimal_places=2)
    status = models.CharField(max_length=30,default=False)