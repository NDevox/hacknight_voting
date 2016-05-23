from django.conf.urls import url

from voting import views

urlpatterns = [
    url(r'^option/$', views.Options, name='add_option'),
    url(r'^vote1/$', views.FirstVote, name='first_vote'),
    url(r'^vote2/$', views.SecondVote, name='second_vote'),
]