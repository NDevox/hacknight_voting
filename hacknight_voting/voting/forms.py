from django import forms, Valida
from django.forms import ValidationError

from voting.models import HackNight


class optionForm(forms.Form):
    option = forms.CharField(label='option', max_length=255)


class VoteForm(forms.Form):
    def __init__(self, hacknight, *args, **kwargs):
        self.hacknight = HackNight.objects.get(pk=hacknight)
        super(VoteForm, self).__init__(*args, **kwargs)


class FirstVoteForm(VoteForm):
    options = forms.MultipleChoiceField()

    def clean(self, *args, **kwargs):
        cleaned_data = super(FirstVoteForm, self).clean(*args, **kwargs)
        if len(self.options) < 1:
            raise ValidationError('You need to pick an option')

        cleaned_data['hacknight'] = self.hacknight

        return cleaned_data


class SecondVoteForm(VoteForm):
    option = forms.ChoiceField()

    def clean(self, *args, **kwargs):
        cleaned_data = super(FirstVoteForm, self).clean(*args, **kwargs)
        if len(self.options) != 1:
            raise ValidationError('You must pick one option')

        cleaned_data['hacknight'] = self.hacknight

        return cleaned_data
