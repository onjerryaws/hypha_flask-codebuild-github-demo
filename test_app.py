import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    rv = client.get('/')
    assert rv.data == b"Hello from AWS CodeBuild via GitHub! \xf0\x9f\x9a\x80"

def test_health_route(client):
    rv = client.get('/health')
    assert rv.status_code == 200
    assert rv.json == {"status": "OK"}
