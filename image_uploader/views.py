import base64

from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from image_uploader.forms import ImageUploadForm
from image_uploader.models import UserImage


def image_upload(request, *args, **kwargs):
    form = ImageUploadForm()
    if request.POST:
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'image_upload.html', {
        'errors': form.errors,
        'images': UserImage.objects.all()
    })


def test_email_view(request, *args, **kwargs):
    if request.POST:
        data = request.POST.dict()
        send_mail('', data['body'], 'test@gmail.com', [data['email']])
    return render(request, 'email.html')

