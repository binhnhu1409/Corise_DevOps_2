import pytest
from quote_gen.app import app


@pytest.fixture 
def test_client():
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client
            
def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200

def test_health_page(test_client):
    response = test_client.get("/health")
    assert response.status_code == 200
    assert "healthy" in str(response.data)

def test_quote_page(test_client):
    response = test_client.get("/quote")
    assert response.status_code == 200