import os
import tempfile
import pytest

from app import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Use a temporary DB path for the app
    db_path = str(tmp_path / "test.db")
    monkeypatch.setenv("DB_PATH", db_path)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Emily" in rv.data or b"Projects" in rv.data
