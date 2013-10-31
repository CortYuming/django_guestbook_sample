from django.conf.urls import patterns, url

from greetings.views import GreetingCreateView


urlpatterns = patterns(
    '',
    # url(r'^$', GreetingListView.as_view(), name='list'),
    url(r'^$', GreetingCreateView.as_view(), name='list'),
    # url(r'^new$', GreetingCreateView.as_view(), name='new'),
)
