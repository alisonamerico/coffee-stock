import json


# import pytest
# from django.contrib.auth.models import User
# from django.contrib.gis.geos import factory
# from pytest_django.fixtures import client
# from rest_framework.authtoken.models import Token
# from rest_framework import status
# from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
# from django.urls import reverse


# class UserRegistrationAPIViewTestCase(APITestCase, client):
#     url = client.get("/rest-auth/login/")
#
#     def test_invalid_password(self):
#         """
#         Test to verify that a post call with invalid passwords
#         """
#         user_data = {
#             "username": "testuser",
#             "email": "test@testuser.com",
#             "password": "password",
#             "confirm_password": "INVALID_PASSWORD"
#         }
#         response = self.client.post(self.url, user_data)
#         self.assertEqual(400, response.status_code)
#
#     def test_user_registration(self):
#         """
#         Test to verify that a post call with user valid data
#         """
#         user_data = {
#             "username": "testuser",
#             "email": "test@testuser.com",
#             "password": "123123",
#         }
#         response = self.client.post(self.url, user_data)
#         self.assertEqual(201, response.status_code)
#         self.assertTrue("token" in json.loads(response.content))


def test_status_code_not_authenticaded(client):
    """Authentication credentials were not provided."""
    response = client.get('/api/')
    assert response.status_code == 403


def test_content_http_403_forbidden(client):
    """Authentication credentials were not provided."""
    response = client.get('/api/')
    dct = extract_and_parse_json(response)
    assert dct == {"detail": "Authentication credentials were not provided."}


def test_status_code_get_method_not_allowed(client):
    """Method \"GET\" not allowed."""
    response = client.get('/rest-auth/login/')
    assert response.status_code == 405


def test_content_get_method_not_allowed(client):
    """Method \"GET\" not allowed."""
    response = client.get('/rest-auth/login/')
    dct = extract_and_parse_json(response)
    assert dct == {"detail": "Method \"GET\" not allowed."}


def extract_and_parse_json(response):
    s = response.content.decode(response.charset)
    dct = json.loads(s)
    return dct


# def test_user_autentication():
# #     # client = APIClient()
# #     # client.login(
#     '/rest-auth/login/', {'username': 'coffe', 'email': 'email@email.com', 'password': 'test@123'}, format='json'
# #     # )
# #     client = APIClient()
# #     client.login(username='coffe', email='coffee@coffee.com', password='HotCoffee@123')
#
# # Using the standard RequestFactory API to create a form POST request
#     factory = APIRequestFactory()
#     request = factory.post(
#         '/rest-auth/login/', {'username': 'coffee', 'email': 'email@email.com', 'password': 'test@123'}, format='json'
#     )
#
#
# def test_force_authenticate():
#     user = User.objects.get(username='olivia')
#     request = factory.get('/rest-auth/login/')
#     force_authenticate(request, user=user, token=user.auth_token)


# class UserLoginAPIViewTestCase(APITestCase):
#     url = reverse("/rest-auth/login/")
#
#     def setUp(self):
#         self.username = "john"
#         self.email = "john@snow.com"
#         self.password = "you_know_nothing"
#         self.user = User.objects.create_user(self.username, self.email, self.password)
#
#     def test_authentication_without_password(self):
#         response = self.client.post(self.url, {"username": "snowman"})
#         self.assertEqual(400, response.status_code)
#
#     def test_authentication_with_wrong_password(self):
#         response = self.client.post(self.url, {"username": self.username, "password": "I_know"})
#         self.assertEqual(400, response.status_code)
#
#     def test_authentication_with_valid_data(self):
#         response = self.client.post(self.url, {"username": self.username, "password": self.password})
#         self.assertEqual(200, response.status_code)
#         self.assertTrue("auth_token" in json.loads(response.content))
