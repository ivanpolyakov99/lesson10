from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from testing.models import Test
from testing.forms import MyModelForm

# Create your views here.


def test_view(request, *args, **kwargs):
    parent = request.GET.get('parent', '')
    block_count = request.GET.get('count') or 1
    if parent:
        template = 'index.html'
    else:
        template = 'child.html'
    return render(
        request,
        template,
        context={
            "tests": Test.objects.all(),
            "count": block_count
        }
    )


def index(request, *args, **kwargs):
    return render(
        request,
        'tests.html',
        context={
            "tests": Test.objects.all(),
        }
    )


def test_details(request, *args, **kwargs):
    _id = kwargs['id']
    test = get_object_or_404(Test, id=_id)
    form = MyModelForm()
    if request.POST:
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()
    return render(
        request,
        'detail.html',
        context={
            "test": test,
            "form": form
        }
    )