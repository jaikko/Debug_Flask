import pytest
from server import app as _app, clubs, competitions


@pytest.fixture
def client(app):
    """Get a test client for your Flask app"""
    return app.test_client()


@pytest.fixture
def app():
    """Yield your app with its context set up and ready"""

    with _app.app_context():
        yield _app

@pytest.fixture
def generate_variables():   
    clubs = [{
        "name": "Test",
        "email": "test@test.co",
        "points": "13"
    }]

    competitions = [{
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "15"
         },
        {
        "name": "Spring",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "14"
    }]
    return clubs, competitions
