from django.test import TestCase, Client
from django.urls import reverse, resolve
from .forms import registrationForm

class TestRegistration(TestCase):
    # test the registration of the project
    def setUp(self):
        self.client = Client()
    
    def test_view_registrationPage(self):
        response_success = self.client.get(reverse('registrationPage'))
        response_failure1 = self.client.get('invalidURL')
        response_failure2 = self.client.get(reverse('register'))
        self.assertEqual(resolve(reverse('registrationPage')).view_name, 'registrationPage')
        self.assertEqual(response_success.status_code, 200)
        self.assertNotEqual(response_failure1.status_code, 200)
        self.assertNotEqual(response_failure2.status_code, 200)
        self.assertIsInstance(response_success.context['form'], registrationForm)

    def test_view_register(self):

        # view register is only for receiving the form, so it should not accept any GET request.
        # and it only accept post request from the exact page view registrationPage served, so it should alsp 
        # deny any post request made outside view registrationPage.

        response_failure1 = self.client.get(reverse('register')) 
        response_failure2 = self.client.post(registrationForm()) 
        self.assertNotAlmostEqual(response_failure1.status_code, 200)
        self.assertNotAlmostEqual(response_failure2.status_code, 200)
    
        

