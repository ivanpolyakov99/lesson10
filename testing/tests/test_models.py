from django import test

from testing.models import Test


class TestModels(test.TestCase):
    def test_model_test(self):
        test = Test.objects.create(
            name='Name1',
            level=1
        )
        self.assertEqual(str(test), "Name1")
        self.assertEqual(test.is_hard(), False)
        test.level = 6
        test.save()
        self.assertEqual(test.is_hard(), True)
