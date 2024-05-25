from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.hashers import make_password
from uuid import uuid4
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    id      = models.UUIDField(primary_key=True,default=uuid4,editable=False,unique=True)
    name    = models.CharField(max_length=25, blank=False)
    token = models.CharField(max_length=64, unique=True)
    website = models.URLField(max_length=255,blank=True)
    password = models.CharField(max_length=128, null=False)
    is_staff = models.BooleanField(default=False) 
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    objects = CustomUserManager()

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save(update_fields=['password'])

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    def __str__(self):
        return self.email
    