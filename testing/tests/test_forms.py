from django import test
from django.contrib.auth.models import User

from testing.forms import MyForm, UserAnswerForm
from testing.models import Question, Test, Answer


class TestForms(test.TestCase):

    def setUp(self):
        self.test = Test.objects.create(name='Name')
        self.user = User.objects.create(username='user')
        self.question = Question.objects.create(
            name='question name',
            test=self.test,
            number=1
        )
        self.answer = Answer.objects.create(
            name='answer',
            question=self.question
        )

    def test_is_valid_my_form(self):
        form = MyForm(data={
            'email': 'test@gmail.com',
            'number': 123,
            'text': 'Some text'
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, {
            'email': 'test@gmail.com',
            'number': 123,
            'text': 'Sometext'
        })

    def test_is_not_valid_my_form(self):
        form = MyForm(data={
            'email': 'test@gmail.com',
            'number': -123,
            'text': 'Some text'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'number': ['Must be >= 0']
        })

    def test_user_answer_form(self):
        data = {
            'question_id': self.question.id,
            'answer_ids': [self.answer.id]
        }
        form = UserAnswerForm(
            user=self.user,
            data=data
        )
        self.assertTrue(form.is_valid())

        data['question_id'] = 2132
        form = UserAnswerForm(
            user=self.user,
            data=data
        )
        self.assertFalse(form.is_valid())
        # self.assertEqual(form.errors, {
        #     'question_id': ['Invalid question']
        # })
