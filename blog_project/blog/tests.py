from django.test import TestCase
from django.contrib.auth.models import User
import pytest

# Create your tests here.
@pytest.mark.django_db
def test_home_view(client):
    print("Testing view for home page...")
    response = client.get(path='/')
    assert response.status_code == 200

def test_login_view(client):
    response = client.get(path='/accounts/login/')
    assert response.status_code == 200
    assert 'Login' in str(response.content)
    assert 'registration/login.html' in response.template_name

@pytest.mark.django_db
def test_sigup_authentication(client):
    user  = User.objects.create_user('testuser','test@example.com', 'django123')
    client.login(username = user.username, password = 'django123')

    response = client.get(path ='/register/', follow  = True)
    assert response.status_code == 200
    assert 'Register' in str(response.content)

