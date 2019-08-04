import pytest
import app


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    client = app.app.test_client()
    yield client


def test_index(client):
    response = client.get("/")
    assert b"Pi Simulation" in response.data
    assert b"Estimated Pi ~=" in response.data
