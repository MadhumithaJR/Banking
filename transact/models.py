# Create your models here.
from django.db import models


class Customer(models.Model):
    custID = models.IntegerField()
    custName = models.CharField(max_length=100)
    custBalance = models.IntegerField()
    custEmail = models.EmailField(max_length=100)

class TransactionDetail(models.Model):
    fromCust = models.CharField(max_length=100)
    toCust = models.CharField(max_length=100)
    payment = models.IntegerField()
