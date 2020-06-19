from django.db import models
from django.contrib.auth.models import User

class Custemor(models.Model):
    user=models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=25, null=True)
    phno=models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.name
        
class Product(models.Model):
    name=models.CharField(max_length=200, null=True)
    price=models.DecimalField(max_digits=7, decimal_places=2)
    image=models.ImageField(null=True, blank=True)
    
    slot=models.PositiveIntegerField(unique=True, null=True)
    stock=models.PositiveIntegerField(null=True)
    desc=models.CharField(max_length=200, blank=True)
    netwt=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=""
        return url
        
class Order(models.Model):
    custemor=models.ForeignKey(Custemor, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
        
class OrderItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order=models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField(default=0, null=True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
        
class CoinDispenser(models.Model):
    value=models.IntegerField(default=0)
    count=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    added=models.IntegerField(default=0)
    deleted=models.IntegerField(default=0)
    date_added=models.DateTimeField(auto_now_add=True)