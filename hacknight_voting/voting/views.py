from django.shortcuts import render, redirect
from django.views.generic import View

import datetime

from voting.models import HackNight, Option
from voting.forms import optionForm, FirstVoteForm, SecondVoteForm


def get_current_hacknight():
    return HackNight.objects.latest('date')


class FirstVote(View):

    def get(self, request, *args, **kwargs):
        self.hacknight = get_current_hacknight()
        context = {'form': FirstVoteForm(self.hacknight.pk)}
        return render(request, 'vote1.html', context)

    def post(self, request, *args, **kwargs):
        self.hacknight = get_current_hacknight()
        form = FirstVoteForm(self.hacknight.pk, request.POST)

        if form.is_valid():
            form.run_votes(form.cleaned_data['options'])

        return redirect('voting:second_vote')


class SecondVote(View):
    def get(self, request, *args, **kwargs):
        self.hacknight = get_current_hacknight()
        context = {'form': SecondVoteForm(self.hacknight.pk)}
        return render(request, 'vote1.html', context)

    def post(self, request, *args, **kwargs):
        self.hacknight = get_current_hacknight()
        form = SecondVoteForm(self.hacknight.pk, request.POST)

        if form.is_valid():
            form.run_vote(form.cleaned_data['option'])

        return redirect('voting:winner')


class registerOption(View):

    def get(self, request, *args, **kwargs):

        try:
            hacknight = get_current_hacknight()

            if hacknight.date < datetime.date.today():
                hacknight = HackNight.objects.create(name='ANOTHER HACK NIGHT')
        except HackNight.DoesNotExist:
            hacknight = HackNight.objects.create(name='ANOTHER HACK NIGHT')

        form = optionForm()

        return render(request, 'register_option.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = optionForm(request.POST)
        if form.is_valid():
            option = Option.objects.create(**form.cleaned_data)
            x = get_current_hacknight()
            x.options.add(option)
            x.save()
        return render(request, 'register_option.html', {'form': form})


class Winner(View):
    def get(self, request, *args, **kwargs):
        hacknight = get_current_hacknight()

        winner = hacknight.options.all().order_by('-second_vote')[0]

        return render(request, 'winner.html', {'winner': winner})
