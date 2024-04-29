from django import forms
from . import models

class TextInputForm(forms.Form):
    text_input = forms.CharField(label='Enter text', max_length=100)

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = models.UploadedFile
        fields = ('file',)