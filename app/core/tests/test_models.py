"""
Docstring for app.core.tests.test_models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        """
        Docstring for test_create_user_with_email_successful
        
        :param self: Description
        """
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))