from django.http import HttpResponse


def my_first_view(request, *args, **kwargs):
    return HttpResponse('Hello world!')
