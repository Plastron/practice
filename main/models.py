from django.db import models
from moviepy.editor import *
from google.colab import files

# Create your models here.

class TextInput(models.Model):
    text_input = models.CharField(max_length=100)

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')

