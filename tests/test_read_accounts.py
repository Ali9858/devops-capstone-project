"""Tests for reading accounts and checking service health."""


def test_read_account(client, account_data, saved_account):
    response = client.get(f"/accounts/{saved_account}")

    assert response.status_code == 200
    assert response.get_json()["email"] == account_data["email"]


def test_read_missing_account_returns_404(client):
    response = client.get("/accounts/999")

    assert response.status_code == 404


def test_health_endpoint_sets_security_headers(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "OK"}
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
