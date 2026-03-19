from django.db import models
from django.contrib.auth.models import User
from apps.stores.models import Transaction
# Create your models here.

class Status(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

class Track(models.Model):
    transaction_id = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    courier_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)