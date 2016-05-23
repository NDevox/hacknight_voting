from django import forms
from django.forms import ValidationError

from voting.models import HackNight
from voting.models import Option

class optionForm(forms.Form):
    options = Option
    fields = "__all__"


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
