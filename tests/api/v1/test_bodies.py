from fastapi.testclient import TestClient


def test_get_bodies(client: TestClient) -> None:
    response = client.get('/bodies/')
    assert response.status_code == 200
    resp_json = response.json()
    assert len(resp_json['data']) == 14


def test_get_body(client: TestClient) -> None:
    response = client.get('/bodies/MANMAN')
    assert response.status_code == 200
    data = response.json()['data']
    assert len(data) == 1
    assert data[0]['name'] == 'MANMAN'


def test_get_planets(client: TestClient) -> None:
    response = client.get('/bodies/planets')
    assert response.status_code == 200
    data = response.json()['data']
    for planet in data:
        assert planet['isPlanet']
