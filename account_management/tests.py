from django.test import TestCase
from .email_send import random_str
from views import LoginForm


# Create your tests here.
class RandomStrTest(TestCase):

    def test_normal_input(self):
        test_string = random_str(12)
        self.assertEqual(len(test_string), 12,
                         f"The length of the string {test_string} is not correct")
        self.assertTrue(test_string.isalnum(), f"The string {test_string} contains illegal chars.")

    def test_default_input(self):
        test_string = random_str()
        self.assertEqual(len(test_string), 8,
                         f"The length of the string {test_string} is not correct")
        self.assertTrue(test_string.isalnum(),
                         f"The string {test_string} contains illegal chars.")

    def test_illegal_input(self):
        with self.assertRaises(TypeError, msg="Good"):
            string = random_str('a')

class LoginFormTest(TestCase):
    def setUp(self):
        self.login_form = LoginForm()
