from django import forms

from .models import NewImage

class UploadForm(forms.ModelForm):
    class Meta:
        model = NewImage
        fields = '__all__'