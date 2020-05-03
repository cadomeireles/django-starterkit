from django.contrib.auth.models import User
from django.test import Client, TestCase


class DashboardTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_redirect_to_dashboard_after_login(self):
        user = User.objects.create_user(
            email='tester@email.com', username='tester')
        user.set_password('Tes#es12_')
        user.save()

        post_data = {
            'login': 'tester@email.com', 'password': 'Tes#es12_'
        }

        response = self.client.post('/accounts/login/', post_data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/dashboard')
