from django.test import TestCase

# Create your tests here.


class DummyTestCase(TestCase):

    def test_something(self):
        self.assertEqual(1, 1)
    def test_something_else(self):
        self.assertEqual(0, 0)
