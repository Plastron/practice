from django import forms

class TextInputForm(forms.Form):
    text_input = forms.CharField(label='Enter text', max_length=100)

class TextInputForm_2(forms.Form):
    text_input_2 = forms.CharField(label='Enter text 2', max_length=100)