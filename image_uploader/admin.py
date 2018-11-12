from django.contrib import admin

# Register your models here.
from image_uploader.models import UserImage

admin.site.register(UserImage)
