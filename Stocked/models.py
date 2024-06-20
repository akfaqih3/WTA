from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=64)
    note = models.TextField()

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=4)
    note = models.TextField()

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=32)
    note = models.TextField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=32)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=8)
    barcode = models.CharField(max_length=16)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=9,decimal_places=2)
    sale_price = models.DecimalField(max_digits=9,decimal_places=2)
    purchase_unit = models.ForeignKey(Unit,on_delete=models.CASCADE,related_name='parchase_unit')
    sale_unit = models.ForeignKey(Unit,on_delete=models.CASCADE,related_name='sale_unit')
    note = models.TextField(max_length=64)
    image = models.ImageField(upload_to="pro_images/%y/%m/%d",default='pro_images/default.png',blank=True)
    