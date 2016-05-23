from django import forms
from django.forms import ValidationError

from voting.models import HackNight
from voting.models import Option
from voting.views import get_current_hacknight

class optionForm(forms.Form):
    options = Option
    fields = "__all__"


def get_query(self):
    hacknight = get_current_hacknight()

    return hacknight.options.all()

def get_top_query(self):
    hacknight = get_current_hacknight()

    return hacknight.options.all().order_by('-first_vote')[:3]


class VoteForm(forms.Form):
    def __init__(self, hacknight, *args, **kwargs):
        self.hacknight = HackNight.objects.get(pk=hacknight)
        super(VoteForm, self).__init__(*args, **kwargs)

    def run_vote(self, option):

        option = Option.objects.get(pk=option)

        option.second_vote += 1

        option.save()


class FirstVoteForm(VoteForm):
    options = forms.ModelMultipleChoiceField(queryset=get_query)

    def __init__(self, *args, **kwargs):
        super(FirstVoteForm, self).__init__(*args, **kwargs)


    def clean(self, *args, **kwargs):
        cleaned_data = super(FirstVoteForm, self).clean(*args, **kwargs)
        if len(self.options) < 1:
            raise ValidationError('You need to pick an option')

        cleaned_data['hacknight'] = self.hacknight

        return cleaned_data

    def run_votes(self, options):
        for option in options:
            self.run_vote(option)


class SecondVoteForm(VoteForm):
    option = forms.ModelChoiceField(queryset=get_top_query)

    def clean(self, *args, **kwargs):
        cleaned_data = super(FirstVoteForm, self).clean(*args, **kwargs)
        if len(self.options) != 1:
            raise ValidationError('You must pick one option')

        cleaned_data['hacknight'] = self.hacknight

        return cleaned_data