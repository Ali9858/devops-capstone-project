"""Tests for deleting accounts."""


def test_delete_account(client, saved_account):
    response = client.delete(f"/accounts/{saved_account}")

    assert response.status_code == 204
    assert response.data == b""
    assert client.get(f"/accounts/{saved_account}").status_code == 404


def test_delete_missing_account_returns_404(client):
    response = client.delete("/accounts/999")

    assert response.status_code == 404
