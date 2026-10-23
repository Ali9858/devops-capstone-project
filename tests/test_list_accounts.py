"""Tests for listing accounts."""


def test_list_accounts_empty(client):
    response = client.get("/accounts")

    assert response.status_code == 200
    assert response.get_json() == []


def test_list_accounts_returns_all_records(client, account_data):
    client.post("/accounts", json=account_data)
    second = dict(account_data, email="grace@example.com", name="Grace Hopper")
    client.post("/accounts", json=second)

    response = client.get("/accounts")

    assert response.status_code == 200
    assert [account["name"] for account in response.get_json()] == [
        "Ada Lovelace",
        "Grace Hopper",
    ]
