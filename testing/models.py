from django.core.exceptions import ValidationError
from django.db import models

from django.conf import settings


# Create your models here.
class Test(models.Model):
    MIN_LEVEL = 1
    MAX_LEVEL = 10
    LEVELS = [(i, i) for i in range(MIN_LEVEL, MAX_LEVEL + 1, 1)]
    name = models.CharField(
        verbose_name='new name',
        max_length=255
    )
    level = models.PositiveSmallIntegerField(
        choices=LEVELS,
        default=MIN_LEVEL
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Test'


class Question(models.Model):
    name = models.CharField(max_length=255)
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions'
    )
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

    # def clean(self):
    #     correct_values = self.answers.all().values_list('is_correct', flat=True)
    #     if not any(correct_values):
    #         raise ValidationError('Please, provide any correct answer')
    #     super().clean()

    class Meta:
        unique_together = (
            ('number', 'test'),
        )
        ordering = ('test', 'number',)


class Answer(models.Model):
    name = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    score = models.PositiveSmallIntegerField(default=0)
    question = models.ForeignKey(
        Question,
        null=True,
        related_name='answers',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ManyToManyField(Answer)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    class Meta:
        unique_together = (
            ('question', 'user'),
        )

    def __str__(self):
        return f'{self.user}: {self.question} - {self.answer.all()}'
