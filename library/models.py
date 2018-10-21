from django.contrib.postgres.fields import ArrayField, JSONField
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    authors = models.ManyToManyField(
        'library.Author',
        related_name='books',
        null=True
    )


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return "{} - {}".format(
            self.name, self.age
        )

import random


def random_1_1000():
    return random.randint(1, 1000)


class TestField(models.Model):
    char_field = models.CharField(max_length=50, null=True)
    float_field = models.FloatField(
        verbose_name='My float name',
        help_text='help text',
        primary_key=False,
        null=True,
        blank=True,
        default=1.0
    )
    boolean_field = models.BooleanField(default=False)
    big_int_field = models.BigIntegerField(
        unique=True,
        null=True
    )
    positive_field = models.PositiveIntegerField(
        db_index=True,
        null=True
    )
    small_int_field = models.SmallIntegerField(
        default=random_1_1000,
        null=True
    )
    positive_small_int_field = models.PositiveSmallIntegerField(
        null=True
    )
    text_field = models.TextField(
        null=True
    )
    datetime_field = models.DateTimeField(
        null=True
    )
    date_field = models.DateField(
        null=True
    )
    time_field = models.TimeField(
        null=True
    )
    null_boolean_field = models.NullBooleanField()
    slug_field = models.SlugField(
        null=True
    )
    array_field = ArrayField(models.IntegerField(), default=list)
    json_field = JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    file_field = models.FileField(null=True)
    image_field = models.ImageField(null=True)
    binary_field = models.BinaryField(null=True)

    class Meta:
        verbose_name = 'my class name'
        verbose_name_plural = 'my class names'
        # ordering = ('-create_at', 'char_field')
        index_together = (
            ('date_field', 'created_at'),
            ('updated_at', 'slug_field', 'array_field')
        )
        unique_together = (
            ('date_field', 'created_at'),
        )

# TestField.objects.filter(big_int_field__isnull=True)
# TestField.objects.filter(big_int_field__range=[1, 3])
# TestField.objects.filter()
#
#
# class User(models.Model):
#     username = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#
#     class Meta:
#         abstract = True
#
#
# class Employee(User):
#     clothes = models.TextField()
#
#
# class Manager(User):
#     salary = models.IntegerField()
#
#     def get_salary(self):
#         return self.salary
#
#
# class Boss(Manager):
#     def get_salary(self):
#         return self.salary * 10
#
#     class Meta:
#         proxy = True

