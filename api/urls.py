from django.urls import path
from rest_framework.authtoken import views as auth_views
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

# urlpatterns = [
#     path('tests', views.TestListCreateAPI.as_view(), name='tests.list'),
#     path('tests/<int:id>', views.TestDetailsAPI.as_view(), name='tests.details'),
# ]

router.register(r'tests', views.TestViewSet)
urlpatterns = router.urls
urlpatterns += [
    path('api-token-auth', auth_views.obtain_auth_token)
]
