from django.contrib.auth.models import BaseUserManager
from uuid import uuid4

class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, token, password, **extra_fields):
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            token=token,
            website=extra_fields.pop('website', None),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password,token=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not token:
            token = str(uuid4())
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, token, password, **extra_fields)