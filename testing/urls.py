from django.urls import path

from testing.views import test_view, index, test_details, add_answer, UserAnswerView, TestDetailsView


urlpatterns = [
    path('test-view', test_view),
    path('', index, name='index'),
    path('details/<int:id>', TestDetailsView.as_view(), name='details'),
    path('add-answer/<int:id>', UserAnswerView.as_view(), name='add_answer'),
]
