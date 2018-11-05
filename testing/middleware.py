import time
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings


def my_first_middleware(get_response):
    def middleware(request):
        # process_request
        response = get_response(request)
        # process_response
        return response
    return middleware


class MySimpleClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # process_request
        response = self.get_response(request)
        # process_response
        return response


class MyFirstClassMiddleware:
    def __init__(self, get_response):
        print('INIT MIDDLEWARE')
        self.get_response = get_response
        if not settings.DEBUG:
            raise MiddlewareNotUsed

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        now = time.time()
        # print(now - start)
        # print(now - self.start_view)
        return response

    def process_view(self, request, view_func, args, kwargs):
        print('VIEW')
        self.start_view = time.time()
