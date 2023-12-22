from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField()
    qyt=models.IntegerField()
    prd_code=models.CharField(max_length=50,unique=True)