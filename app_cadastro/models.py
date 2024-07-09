from django.db import models
    
class Products(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,default='')
    price = models.FloatField(default='0')
    description = models.CharField(max_length=100,default='')
    categories = models.CharField(max_length=20,default='')
    