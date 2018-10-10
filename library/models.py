from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return "{} - {}".format(
            self.name, self.age
        )
