from django.db import models

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length=32,help_text='Store name')
    location = models.CharField(max_length=64,help_text='location store')
    note = models.TextField()

    def __str__(self):
        return self.name
    
class Unit(models.Model):
    name = models.CharField(max_length=32,help_text='Unit name')
    code = models.CharField(max_length=4,help_text='Unit Code')
    note = models.TextField()

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=32,help_text='Brand name')
    note = models.TextField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=32,help_text='Category name')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=32,help_text='Product name')
    code = models.CharField(max_length=8,help_text='Product code')
    barcode = models.CharField(max_length=16,help_text='Product barcode')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    purchase_price = models.DecimalField(max_digits=9,decimal_places=2)
    sale_price = models.DecimalField(max_digits=9,decimal_places=2)
    purchase_unit = models.ForeignKey(Unit,on_delete=models.CASCADE,related_name='parchase_unit')
    sale_unit = models.ForeignKey(Unit,on_delete=models.CASCADE,related_name='sale_unit')
    note = models.TextField(max_length=64)
    #image = models.ImageField(upload_to="images/%y/%m/%d")
    