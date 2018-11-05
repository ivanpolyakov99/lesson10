from django import test
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse

from testing.models import Test
from unittest import mock


class TestView(test.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(
            username='username',
            password='1'
        )
        cls.test = Test.objects.create(name='name')

    @classmethod
    def tearDownClass(cls):
        pass

    def test_test_view(self):
        response = self.client.get(reverse('test_view'))
        self.assertTemplateUsed(response, 'child.html')
        self.assertEqual(response.context['count'], 1)

        response = self.client.get(
            reverse('test_view'),
            data={
                'count': 123
            }
        )
        self.assertEqual(response.context['count'], 123)
        self.assertEqual(
            list(response.context['tests']),
            [self.test, ]
        )

        response = self.client.get(
            reverse('test_view'),
            data={
                'parent': 'asdasd'
            }
        )
        self.assertTemplateUsed(response, 'index.html')

    def test_details(self):
        details = reverse('details', kwargs={'id': self.test.id})
        response = self.client.get(details)
        login_url = settings.LOGIN_URL
        self.assertRedirects(response, f'{login_url}?next={details}')

        is_success = self.client.login(username='username', password='2')
        self.assertFalse(is_success)

        is_success = self.client.login(username='username', password='1')
        self.assertTrue(is_success)

        response = self.client.get(details)
        self.assertTemplateUsed(response, 'detail.html')

        self.client.logout()
        response = self.client.get(details)
        self.assertEqual(response.status_code, 302)

    def test_details_post(self):
        is_success = self.client.login(
            username='username',
            password='1'
        )
        self.assertTrue(is_success)

        self.client.post(
            path=reverse('details', kwargs={'id': self.test.id}),
            data={'key': 'value'}
        )

        tests_old = list(Test.objects.all().values_list('id', flat=True))
        tests_old_count = len(tests_old)
        self.client.post(
            path=reverse('details', kwargs={'id': self.test.id}),
            data={
                'name': 'New test',
                'level': 5
            }
        )
        tests_new = Test.objects.all()
        tests_new_count = len(tests_new)
        self.assertEqual(tests_new_count - 1, tests_old_count)

        new_test = Test.objects.exclude(id__in=tests_old).first()
        self.assertEqual(new_test.name, 'New test')
        self.assertEqual(new_test.level, 5)

        # with mock.patch('testing.view.test_details') as mocked_view:
        #     mocked_view.side_effect = Exception('My exception')
        #     self.client.post(
        #         path=reverse('details', kwargs={'id': self.test.id}),
        #         data={
        #             'name': 'New test',
        #             'level': 5
        #         }
        #     )


