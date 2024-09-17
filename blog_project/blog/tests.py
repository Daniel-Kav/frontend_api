from django.test import TestCase
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
    assert ''