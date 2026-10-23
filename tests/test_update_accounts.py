"""Tests for updating accounts."""


def test_update_account(client, saved_account, account_data):
    updated = dict(account_data, name="Ada Byron", phone_number="555-0199")

    response = client.put(f"/accounts/{saved_account}", json=updated)

    assert response.status_code == 200
    assert response.get_json()["name"] == "Ada Byron"
    assert response.get_json()["phone_number"] == "555-0199"


def test_update_missing_account_returns_404(client, account_data):
    response = client.put("/accounts/999", json=account_data)

    assert response.status_code == 404


def test_update_account_rejects_invalid_date(client, saved_account, account_data):
    account_data["date_joined"] = "invalid"

    response = client.put(f"/accounts/{saved_account}", json=account_data)

    assert response.status_code == 400
