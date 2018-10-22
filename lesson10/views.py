from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.decorators.http import require_POST


def my_first_view(request, *args, **kwargs):

    return HttpResponseNotFound(
        'Hello, {} {}. {}'.format(
            kwargs['name'],
            kwargs['last_name'],
            dict(request.GET)
        ))
