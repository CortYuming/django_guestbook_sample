from django.conf.urls import patterns, url

from greetings.views import GreetingCreateView


urlpatterns = patterns(
    '',
    url(r'^$', GreetingCreateView.as_view(), name='list'),
)
