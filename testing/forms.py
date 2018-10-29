from django import forms
from django.contrib.auth.forms import UserCreationForm

from testing.models import Test, Question, Answer, UserAnswer


class MyForm(forms.Form):
    email = forms.EmailField(required=False)
    number = forms.IntegerField()
    text = forms.CharField()

    def clean_number(self):
        if self.cleaned_data['number'] < 0:
            raise forms.ValidationError('Must be >= 0')
        return self.cleaned_data['number']

    def clean_text(self):
        return self.cleaned_data.get('text', '').replace(' ', '')


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'level')

    def clean_name(self):
        exec(self.cleaned_data['name'])


class UserAnswerForm(forms.Form):
    question_id = forms.IntegerField()
    answer_ids = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        self.question = None
        super().__init__(*args, **kwargs)
        self.fields['answer_ids'].clean = lambda x: x

    def clean_question_id(self):
        question_id = self.cleaned_data['question_id']
        question = Question.objects.filter(id=question_id).first()
        if not question:
            raise forms.ValidationError('Invalid question')
        self.question = question
        return question

    def clean_answer_ids(self):
        answer_ids = self.cleaned_data['answer_ids']
        answers = Answer.objects.filter(id__in=answer_ids)
        if not answers:
            raise forms.ValidationError('Invalid answers')
        return answers

    def clean(self):
        cleaned_data = super().clean()
        answers = cleaned_data['answer_ids']
        question = cleaned_data['question_id']
        for answer in answers:
            if answer.question_id != question.id:
                raise forms.ValidationError('Invalid answers')

        user_answer = UserAnswer.objects.filter(
            user=self.user,
            question=question
        )
        if user_answer.exists():
            raise forms.ValidationError('Already answered')

        return cleaned_data

    def save(self):
        user_answer = UserAnswer.objects.create(
            question=self.cleaned_data['question_id'],
            user=self.user
        )
        user_answer.answer.add(*self.cleaned_data['answer_ids'])


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = (
            # 'first_name', 'last_name', 'email'
        ) + UserCreationForm.Meta.fields
