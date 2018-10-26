from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from testing.models import Test


def index_fbv(request, *args, **kwargs):
    return render(request, 'index.html', context={
        'view': 'FBV',
        'object_list': Test.objects.all()
    })


class IndexCBV(ListView):
    template_name = 'index.html'
    queryset = Test.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view'] = 'CBV'
        return context
