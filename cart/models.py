from django.db import models
from shop.models import *

# Create your models here.
class cartlist(models.Model):
     cart_id=models.CharField(max_length=250,unique=True)
     date_added=models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
         return self.cart_id

class items(models.Model):
    cart_product=models.ForeignKey(products, on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    item_quandity=models.IntegerField()
    
    def __str__ (self):
        return self.cart_product
    