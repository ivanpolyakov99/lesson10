from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='user_images')
    image_base64 = models.TextField(null=True)

