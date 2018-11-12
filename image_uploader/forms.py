import base64

from django import forms

from image_uploader.models import UserImage


class ImageUploadForm(forms.ModelForm):

    class Meta:
        model = UserImage
        fields = ('name',)

    def generate_base64_image(self):
        image = self.files['image']
        return 'data:{content_type};base64,{data}'.format(
            content_type=image.content_type,
            data=base64.b64encode(image.file.read()).decode()
        )

    def save(self, commit=True):
        object_of_user_image = super().save(commit=False)
        object_of_user_image.base64_image = self.generate_base64_image()
        if commit:
            object_of_user_image.save()
        return object_of_user_image
