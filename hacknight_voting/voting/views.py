from django.shortcuts import render, redirect
from django.views.generic import View


class FirstVote(View):

    def get(self, request, *args, **kwargs):
        options = self.hacknight.options.all()
        context = {'options': options}
        return render(request, 'vote1.html', context)

    def post(self, request, *args, **kwargs):
        form  = self.FORM

        if form.is_valid():
            form.run_votes()

        return redirect('voting:second_vote')