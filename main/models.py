from django.db import models
from moviepy.editor import *
from google.colab import files

# Create your models here.

class Video (models.Model):
    video = models.FileField(upload_to = "video/%y")
    def __str__(self):
        return self.caption



