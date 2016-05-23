from django import forms

from voting.models import HackNight

class optionForm(forms.Form):
    option = forms.CharField(label='option', max_length=255)


class VoteForm(forms.Form):
    def __init__(self, hacknight, *args, **kwargs):
        self.hacknight = HackNight.objects.get(pk=hacknight)
        super(VoteForm, self).__init__(*args, **kwargs)


class SecondVoteForm(VoteForm):
    options = forms.MultipleChoiceField()


class SecondVoteForm(VoteForm):
    option = forms.ChoiceField()