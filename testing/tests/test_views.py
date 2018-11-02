from django import test
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

from testing.models import Test


class TestView(test.TestCase):
    def test_test_view(self):
        response = self.client.get(reverse('test_view'))
        self.assertTemplateUsed(response, 'child.html')
        self.assertEqual(response.context['count'], 1)

        test = Test.objects.create(name='name')
        response = self.client.get(
            reverse('test_view'),
            data={
                'count': 123
            }
        )
        self.assertEqual(response.context['count'], 123)
        self.assertEqual(
            list(response.context['tests']),
            [test, ]
        )

        response = self.client.get(
            reverse('test_view'),
            data={
                'parent': 'asdasd'
            }
        )
        self.assertTemplateUsed(response, 'index.html')

    def test_details(self):
        test = Test.objects.create(name='name')
        details = reverse('details', kwargs={'id': test.id})
        response = self.client.get(details)
        login_url = settings.LOGIN_URL
        self.assertRedirects(response, f'{login_url}?next={details}')

        User.objects.create_user(
            username='username',
            password='1'
        )
        is_success = self.client.login(username='username', password='2')
        self.assertFalse(is_success)

        is_success = self.client.login(username='username', password='1')
        self.assertTrue(is_success)

        response = self.client.get(details)
        self.assertTemplateUsed(response, 'detail.html')

        self.client.logout()
        response = self.client.get(details)
        self.assertEqual(response.status_code, 302)


