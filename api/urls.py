from django.urls import path
from api import views

urlpatterns = [
    path('tests', views.TestListCreateAPI.as_view(), name='tests.list'),
    path('tests/<int:id>', views.TestDetailsAPI.as_view(), name='tests.details'),
]
