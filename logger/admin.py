from django.contrib import admin

# Register your models here.
from logger.models import ApplicationError

admin.site.register(ApplicationError)
