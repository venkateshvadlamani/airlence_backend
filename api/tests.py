# signup/tests.py
from django.test import TestCase
from django.contrib.auth.models import User

from signup.models import Signup


class SignupTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a User
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123')
        testuser1.save()

        # create a Signup
        test_signup = Signup.objects.create(
            author=testuser1, email='joker@gmail.com', message='some message')
        test_signup.save()

    def test_signup_content(self):
        signup = Signup.objects.get(id=1)
        expected_author = f'{signup.author}'
        expected_email = f'{signup.email}'
        expected_message = f'{signup.message}'
        self.assertEquals(expected_author, 'testuser1')
        self.assertEquals(expected_email, 'joker@gmail.com')
        self.assertEquals(expected_message, 'some message')
