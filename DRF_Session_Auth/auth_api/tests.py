from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from auth_api.models import Account

class Registration_API_Test(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        Account should be created
        """
        url = reverse('auth_api:register')
        data = {
            "username": "simple",
            "email": "simplea@gmail.com",
            "name": "simple",
            "phone": 9898989899,
            "password": "abcd1#",
            "password2": "abcd1#"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'simple')

    
    def test_existing_account(self):
        """
        Test case for existing user check
        Account shouldn't be created
        """
        url = reverse('auth_api:register')
        account = Account(username='simple', email='simple@gmail.com', 
                            name='simple', phone=999999999)
        account.save()
        data = {
            "username": "simple",
            "email": "simplea@gmail.com",
            "name": "simple",
            "phone": 9898989899,
            "password": "abcd1#",
            "password2": "abcd1#"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)


    def test_missing_field(self):
        """
        Ensure that we get 400 bad request if any field is missing
        Accoutn shouldn't be created
        """
        url = reverse('auth_api:register')
        data = {
            "username": "simple",
            "email": "simplea@gmail.com",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Account.objects.count(), 0)

        
    def test_password_regex(self):
        """
        Ensure that password contain 1 number, 1 character, special character -_#
        Account shouldn't be created
        """
        url = reverse('auth_api:register')
        data = {
            "username": "simple",
            "email": "simplea@gmail.com",
            "name": "simple",
            "phone": 9898989899,
            "password": "abcd1",
            "password2": "abcd1"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Account.objects.count(), 0)

class Login_API_Test(APITestCase):
    def test_login(self):
        """
        Ensure we can log in
        """
        url = reverse('auth_api:login')
        account = Account(username='test')
        account.set_password('test1#')
        account.save()
        data = {
            "username": "test",
            "password": "test1#"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
    def test_login_wrong_creds(self):
        """
        Ensure we get 400 if we provide wrong credentials
        """
        url = reverse('auth_api:login')
        account = Account(username='test')
        account.set_password('test1#')
        account.save()
        data = {
            "username": "test",
            "password": "test1#67"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)