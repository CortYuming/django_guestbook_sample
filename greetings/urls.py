from django.conf.urls import patterns, url

from greetings.views import GreetingListView, GreetingCreateView, GreetingUpdateView


urlpatterns = patterns(
    '',
    url(r'^$', GreetingListView.as_view(), name='list'),
    url(r'^new$', GreetingCreateView.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)$', GreetingUpdateView.as_view(), name='edit'),
)
