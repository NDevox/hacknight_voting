from django import forms
from django.forms import ValidationError

from voting.models import HackNight
from voting.models import Option


def get_current_hacknight():
    return HackNight.objects.latest('date')

class optionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['name', 'description']


def get_query():
    hacknight = get_current_hacknight()

    return hacknight.options.all()

def get_top_query():
    hacknight = get_current_hacknight()

    return hacknight.options.all().order_by('-first_vote')[:3]


class VoteForm(forms.Form):
    def __init__(self, hacknight, *args, **kwargs):
        self.hacknight = HackNight.objects.get(pk=hacknight)
        super(VoteForm, self).__init__(*args, **kwargs)

    def run_vote(self, option):

        option.first_vote += 1

        option.save()


class FirstVoteForm(VoteForm):
    options = forms.ModelMultipleChoiceField(queryset=get_query())

    def __init__(self, *args, **kwargs):
        super(FirstVoteForm, self).__init__(*args, **kwargs)


    def clean(self, *args, **kwargs):
        cleaned_data = super(FirstVoteForm, self).clean(*args, **kwargs)
        if len(cleaned_data['options']) < 1:
            raise ValidationError('You need to pick an option')

        cleaned_data['hacknight'] = self.hacknight

        return cleaned_data

    def run_votes(self, options):
        for option in options:
            self.run_vote(option)


class SecondVoteForm(VoteForm):
    option = forms.ModelChoiceField(queryset=get_top_query())

    def clean(self, *args, **kwargs):
        cleaned_data = super(SecondVoteForm, self).clean(*args, **kwargs)
        if len(cleaned_data['option']) != 1:
            raise ValidationError('You must pick one option')

        cleaned_data['hacknight'] = self.hacknight

        return cleaned_data

    def run_vote(self, option):

        option.second_vote += 1

        option.save()