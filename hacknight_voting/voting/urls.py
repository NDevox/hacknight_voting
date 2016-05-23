from django.conf.urls import url

from voting import views

urlpatterns = [
    url(r'^option/$', views.registerOption.as_view(), name='add_option'),
    url(r'^vote1/$', views.FirstVote.as_view(), name='first_vote'),
    url(r'^vote2/$', views.SecondVote.as_view(), name='second_vote'),
]