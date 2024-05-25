from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Destination(models.Model):
    GET = "get"
    POST = "post"
    PUT = "put"
    METHOD_CHOICES = [
        (GET, 'get'),
        (POST, 'post'),
        (PUT, 'put')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinations')
    url = models.URLField()
    http_method = models.CharField(max_length=5, choices=METHOD_CHOICES, null=False, blank=False, default= POST)
    
    def __str__(self):
        return f"{self.url} ({self.http_method})"

class Header(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='headers')
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.key}: {self.value}"