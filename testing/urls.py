from django.urls import path

from testing.views import test_view, index, \
    test_details, add_answer, UserAnswerView, \
    TestDetailsView, SignupView


urlpatterns = [
    path('test-view', test_view, name='test_view'),
    path('', index, name='index'),
    path('details/<int:id>', test_details, name='details'),
    path('add-answer/<int:id>', UserAnswerView.as_view(), name='add_answer'),
    path('signup', SignupView.as_view(), name='signup')
]
