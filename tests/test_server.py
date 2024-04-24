from fastapi.testclient import TestClient

from server import app

client = TestClient(app)


def test_read_main():
    response = client.get("/fetch_rate", params={"date_": "2024-04-20"})
    assert response.status_code == 200
    assert "eur" in response.json()
