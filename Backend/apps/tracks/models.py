from django.db import models
from django.contrib.auth.models import User
from stores.models import Transaction
# Create your models here.

class Status(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)

