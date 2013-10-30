from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from greetings.models import Greeting


class GreetingListView(ListView):
    model = Greeting
    context_object_name = 'greetings'
    template_name = 'greeting_list.html'


class GreetingCreateView(CreateView):
    model = Greeting
    success_url = reverse_lazy('greetings:list')


class GreetingUpdateView(UpdateView):
    model = Greeting
    success_url = reverse_lazy('greetings:list')
    template_name = 'greeting_form.html'
