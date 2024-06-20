from django.db import models

# Create your models here.

class Account(models.Model):
    accountType =(
        ('customer','customer'),
        ('supplier','supplier')
    )

    name = models.CharField(max_length=32)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=16)
    note = models.CharField(max_length=64,blank=True,null=True)
    type = models.CharField(max_length=16,choices=accountType)

    def __str__(self) -> str:
        return self.name