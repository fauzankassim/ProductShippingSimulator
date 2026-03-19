from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer.username + " purchased " + self.product.title + " at " + self.created_at
