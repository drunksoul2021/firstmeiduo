from django.db import models

# Create your models here.

# 1.define model by myself
# secret need cpty
#class User(models.Model):
#    username = models.CharField(max_length=20,unique=True)
#    password = models.CharField(max_length=20)
#    mobile = models.CharField(max_length=11,unique=True)

# 2.django give us user model
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    mobile = models.CharField(max_length=11,unique=True)

    class Meta:
        db_table = 'tb_users'
        verbose_name = 'user admin'
        verbose_name_plural = verbose_name