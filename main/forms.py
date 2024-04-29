from django import forms
from . import models

class TextInputForm(forms.ModelForm):
    class Meta:
        model = models.TextInput
        fields = ['text_input']