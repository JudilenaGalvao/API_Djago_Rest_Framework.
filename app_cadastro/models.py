from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=30,default='')
    price = models.FloatField(default='0')
    description = models.CharField(max_length=100,default='')
    categories = models.CharField(max_length=20,default='')
    