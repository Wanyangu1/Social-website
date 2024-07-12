from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify
from urllib import request

from .models import Image

class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')

    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        
        # Extract the file extension from the URL
        extension = url.rsplit('.', 1)[-1].lower()
        
        # Check if the extension is in the list of valid extensions
        if extension not in valid_extensions:
            raise forms.ValidationError(
                'The given URL does not match valid image extensions.'
            )
        
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[-1].lower()
        image_name = f'{name}.{extension}'
        
        # Download image from the given URL
        response = request.urlopen(image_url)
        image.image.save(image_name, ContentFile(response.read()), save=False)
        
        if commit:
            image.save()
        
        return image
