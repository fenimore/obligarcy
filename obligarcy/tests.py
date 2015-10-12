from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Contract, Submission
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your tests here.

# Test Index
class IndexViewTest(TestCase):
    def test_index_view_with_no_user(self):
        """
        If no user is active, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('obligarcy:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No users are available.")

    def test_index_view_with_a_user(self):
        """
        Questions with a user in the past should be displayed on the
        index page.
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )
# Test Register
# Test Login
# Test Logout
# Test Profile
# Test New Contract
# Test New Submission