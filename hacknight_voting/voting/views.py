from django.shortcuts import render, redirect
from django.views.generic import View

from voting.models import HackNight
from voting.forms import optionForm, FirstVoteForm, SecondVoteForm


def get_current_hacknight():
    return Hack

class FirstVote(View):

    def get(self, request, *args, **kwargs):
        options = self.hacknight.options.all()
        context = {'options': options}
        return render(request, 'vote1.html', context)

    def post(self, request, *args, **kwargs):
        form  = FirstVoteForm(request.POST)

        if form.is_valid():
            form.run_votes()

        return redirect('voting:second_vote')


class SecondVote(View):
    def get(self, request, *args, **kwargs):
        options = self.hacknight.options.all()
        context = {'options': options}
        return render(request, 'vote1.html', context)

    def post(self, request, *args, **kwargs):
        form = SecondVoteForm(request.POST)

        if form.is_valid():
            form.run_votes()

        return redirect('voting:second_vote')


class registerOption(View):

    def set_option(self, request):

        if request.method == 'POST':

            form = optionForm(request.POST)

            if form.is_valid():
               print('cool')

        else:
           form = optionForm()

        return render(request, 'register_option.html', {'form': form})
