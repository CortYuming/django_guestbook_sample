from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from greetings.models import Greeting


class GreetingCreateView(CreateView):
    model = Greeting
    success_url = reverse_lazy('greetings:list')
    template_name = 'greetings/greetings.html'

    def get_context_data(self, **kwargs):
        greetings = Greeting.objects.order_by('-date_created')
        kwargs['greetings'] = greetings
        return kwargs
