import pytest
from service_api.app import create_app


@pytest.yield_fixture
def app():
    app = create_app()
    yield app

@pytest.fixture
def test_client(loop, app, sanic_client):
    return loop.run_until_complete(sanic_client(app))
