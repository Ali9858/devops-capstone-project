"""Pytest fixtures for isolated service tests."""

import os

import pytest

# Keep unit tests independent of a separately running PostgreSQL container.
os.environ["DATABASE_URI"] = "sqlite:///:memory:"

from service import app  # noqa: E402
from service.models import db  # noqa: E402


@pytest.fixture
def client():
    """Provide a Flask test client with a clean database for each test."""
    with app.app_context():
        db.drop_all()
        db.create_all()
    with app.test_client() as test_client:
        yield test_client
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def account_data():
    """Return a valid Account request body."""
    return {
        "name": "Ada Lovelace",
        "email": "ada@example.com",
        "address": "1 Analytical Engine Way",
        "phone_number": "555-0101",
        "date_joined": "2024-01-02",
    }


@pytest.fixture
def saved_account(client, account_data):
    """Create an account and return its ID."""
    response = client.post("/accounts", json=account_data)
    assert response.status_code == 201
    return response.get_json()["id"]
