from django.urls import path
from image_uploader.views import image_upload, test_email_view


urlpatterns = [
    path('image-upload/', image_upload, name='image_upload'),
    path('email/', test_email_view, name='email'),
]
