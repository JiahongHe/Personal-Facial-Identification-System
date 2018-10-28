from django.test import TestCase
from requestHandler.models import User
from django.core.files import File
import mock

class UserTestCase(TestCase):
    def setUp(self):
        user1 = User()

    def userCreation(self):