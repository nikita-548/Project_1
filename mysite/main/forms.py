from django.forms import ClearableFileInput
from django import forms
from .models import UploadFiles
class FileModelForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = ['music_file']
        widgets = {
            'music_file': ClearableFileInput(attrs={'multiple': True}),
        }