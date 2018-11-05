from django.contrib.postgres.fields import JSONField
from django.db import models


class ApplicationError(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    class_name = models.CharField(max_length=64)
    url = models.URLField(max_length=500)
    method = models.CharField(max_length=10, null=True)
    data = JSONField(default=dict)
    traceback = models.TextField()