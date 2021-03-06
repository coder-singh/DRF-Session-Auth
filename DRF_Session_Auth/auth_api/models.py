from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    phone = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'Account'