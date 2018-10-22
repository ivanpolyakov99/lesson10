from django.urls import path

from testing.views import test_view, index, test_details


urlpatterns = [
    path('test-view', test_view),
    path('', index),
    path('details/<int:id>', test_details, name='details'),
]
