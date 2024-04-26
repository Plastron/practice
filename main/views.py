from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import forms


@csrf_exempt
def index(request):
    form_1 = forms.TextInputForm
    form_2 = forms.TextInputForm_2
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.TextInputForm(request.POST)
        return HttpResponse("<h4>Test text</h4>")
        """# check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            text = form.cleaned_data['text_input']
            processed_text = text.upper()
            # redirect to a new URL:
            return render(request, 'main/index.html', {'form': form})"""

    # if a GET (or any other method) we'll create a blank form

    return render(request, 'main/index.html', {'form_1': form_1, 'form_2': form_2})

@csrf_exempt
def test(request):
    return HttpResponse("<h4>Test text</h4>")