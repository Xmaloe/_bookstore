import pytest
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_with_token():
    user = User.objects.create_user(username="testuser", password="testpass")
    token, _ = Token.objects.get_or_create(user=user)
    return user, token

@pytest.fixture
def api_url():
    return "/bookstore/v1/product/"

def test_access_without_token(api_client, api_url):
    response = api_client.get(api_url)
    assert response.status_code == status.HTTP_200_OK

def test_access_with_token(api_client, user_with_token, api_url):
    _, token = user_with_token
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    response = api_client.get(api_url)
    assert response.status_code == status.HTTP_200_OK
