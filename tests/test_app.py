import pytest

from src.app import create_app
from src.configs.testing import TestingConfig as Config


@pytest.fixture
def application():
    app = create_app(Config)

    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()


def test_hello():
    response = create_app().test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'
