from django.test import TestCase
from mysite.core.models import Profile
# Create your tests here.


class ProfileModelTest(TestCase):

    @classmethod
    def test_response_login(self):
        from django.test.client import Client
        c = Client()
        response = c.post('/login/', {'username': 'q', 'password': 'q'})
        assert response.status_code == 200

    def test_response_logout(self):
        from django.test.client import Client
        c = Client()
        response = c.post('/logout/')
        assert response.status_code == 302

    def test_response_signup(self):
        from django.test.client import Client
        c = Client()
        response = c.post('/signup/')
        assert response.status_code == 200




