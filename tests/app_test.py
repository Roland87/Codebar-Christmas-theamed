from app import app
import pytest

def test_home_page():
    client = app.test_client()
    response = client.get('/')
    assert b'Codebar Christmas' in response.data
    assert b'Season\'s Greetings!' in response.data

def test_invalid_route():
    client = app.test_client()
    response = client.get('/invalid-route')
    assert response.status_code == 404