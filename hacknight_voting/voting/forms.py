from django import forms

class optionForm(forms.Form):
    option = forms.CharField(label='option', max_length=255)