from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    phone = models.CharField(min_length=1000000000, max_length=9999999999)

    class Meta:
        db_table = 'Account'