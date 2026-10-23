"""Tests for creating accounts."""


def test_create_account(client, account_data):
    response = client.post("/accounts", json=account_data)

    assert response.status_code == 201
    assert response.get_json()["name"] == account_data["name"]
    assert response.get_json()["date_joined"] == "2024-01-02"
    assert response.headers["Location"].endswith("/accounts/1")


def test_create_account_requires_fields(client):
    response = client.post("/accounts", json={"name": "Ada"})

    assert response.status_code == 400


def test_create_account_rejects_invalid_date(client, account_data):
    account_data["date_joined"] = "not-a-date"

    response = client.post("/accounts", json=account_data)

    assert response.status_code == 400


def test_create_account_rejects_non_object_json(client):
    response = client.post("/accounts", json=["not", "an", "object"])

    assert response.status_code == 400


def test_create_account_requires_json_content_type(client, account_data):
    response = client.post(
        "/accounts", data="name=Ada", content_type="application/x-www-form-urlencoded"
    )

    assert response.status_code == 415
