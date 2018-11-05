import traceback

from django.utils.deprecation import MiddlewareMixin

from logger.models import ApplicationError


class ApplicationErrorMiddleware(MiddlewareMixin):
    # def __init__(self, get_response):
    #     super().__init__(get_response)
    #     print('ERRORMIDDLEWARE')
    #     self.get_response = get_response

    # def __call__(self, request):
    #     return self.get_response(request)
    def process_exception(self, request, exception):
        ApplicationError.objects.create(
            message=str(exception),
            class_name=exception.__class__.__name__,
            url=request.build_absolute_uri(),
            method=request.method,
            data=request.GET or request.POST,
            traceback=traceback.format_exc()
        )