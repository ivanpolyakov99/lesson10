from django import template
from testing.models import UserAnswer

register = template.Library()


@register.filter('my_filter')
def my_filter(value, arg):
    return value.split(arg)


@register.simple_tag
def my_tag(a, b, c=None):
    return f"{a} {b} {c}"


@register.simple_tag
def check_question(user, question):
    user_answer = UserAnswer.objects.filter(
        user=user,
        question=question
    ).first()
    if not user_answer:
        return
    answers = user_answer.answer.filter(
    ).values_list('is_correct', flat=True)
    return all(answers)



# register.filter('my_filter', my_filter)
