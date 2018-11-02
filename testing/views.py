from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import FormView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate

from testing.models import Test, Answer, UserAnswer
from testing.forms import MyModelForm, UserAnswerForm, UserCreateForm


# Create your views here.


def test_view(request, *args, **kwargs):
    parent = request.GET.get('parent', '')
    block_count = int(request.GET.get('count') or 1)
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


@login_required
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


class TestDetailsView(DetailView):
    template_name = 'detail.html'

    def get_object(self, queryset=None):
        return Test.objects.get(id=self.kwargs['id'])


@require_POST
@login_required
def add_answer(request, *args, **kwargs):
    question_id = kwargs['id']
    answer_ids = request.POST.getlist(str(question_id))

    form = UserAnswerForm(
        user=request.user,
        data={
            'question_id': question_id,
            'answer_ids': answer_ids
        }
    )
    if form.is_valid():
        form.save()
        return redirect(reverse('details', kwargs={'id': 3}))
    else:
        return HttpResponse('', status=400)


class UserAnswerView(FormView):
    form_class = UserAnswerForm

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        question_id = self.kwargs['id']
        answer_ids = self.request.POST.getlist(str(question_id))
        return {
            'user': self.request.user,
            'data': {
                'question_id': question_id,
                'answer_ids': answer_ids
            }
        }

    def form_valid(self, form):
        form.save()
        return redirect(reverse('details', kwargs={
            'id': form.question.test.id
        }))

    def form_invalid(self, form):
        return redirect(reverse('details', kwargs={
            'id': form.question.test.id
        }))


class SignupView(FormView):
    form_class = UserCreateForm
    template_name = 'signup.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        user = authenticate(
            request=self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        login(self.request, user)
        return super().form_valid(form)
