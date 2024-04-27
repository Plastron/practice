from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import os

from moviepy.editor import *
from google.colab import files
from . import forms


@csrf_exempt
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form_1 = forms.TextInputForm(request.POST)
        # check whether it's valid:
        if form_1.is_valid():
            # process the data in form.cleaned_data as required
            text = form_1.cleaned_data['text_input']
            content_file = create_ticker_video(text)          
            video_path = os.path.join(settings.MEDIA_ROOT, 'ticker_video.mp4')
            # redirect to a new URL:
            return render(request, 'main/index_2.html', {'form_1': form_1, 'video_path': video_path })

    # if a GET (or any other method) we'll create a blank form
    form_1 = forms.TextInputForm

    return render(request, 'main/index.html', {'form_1': form_1})

@csrf_exempt
def test(request):
    return HttpResponse("<h4>Test text</h4>")

def create_ticker_video(text, duration = 3, w = 100, h = 100):

    # Create a TextClip with the provided text
    txt_clip = TextClip(text, fontsize=50, color='white', bg_color='black').set_duration(duration)


    # Create a black background clip with the specified dimensions and duration
    bg_clip = ColorClip(size=(w, h), color=(0,0,0)).set_duration(duration)

    # Store the width and height of the text clip for future calculations
    textclip_width, textclip_height = txt_clip.size

    # Define the Translate (Movement) Function
    def translate(t):
        # Start and end positions of the text
        start_pos = (w/2, h/2-textclip_height/2)
        end_pos = (w/2 - textclip_width, h/2-textclip_height/2)

        # Calculate x and y positions based on elapsed time and total duration
        x = int(start_pos[0] + t/duration * (end_pos[0] - start_pos[0]))
        y = int(start_pos[1] - t/duration * (end_pos[1] - start_pos[1]))

        return (x, y)

    # Apply the Translate (Movement) Effect to the Text Clip
    # The text will move based on the translate function's calculations
    txt_moving = txt_clip.set_position(translate)

    # Combine the background and moving text clips into one video
    video = CompositeVideoClip([bg_clip, txt_moving])
    # Create the ticker video

    # Write the video to a file
    #output_file = "ticker_video.mp4"
    #video.write_videofile(output_file, codec='libx264', fps=30)

    return video