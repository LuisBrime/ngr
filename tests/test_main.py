import json

from fastapi.testclient import TestClient

from ngr.main import handler


def test_handler(caplog) -> None:
    event = dict(
        path='/bodies/',
        httpMethod='GET',
        requestContext={},
        multiValueQueryStringParameters=None,
    )
    response = handler(event, None)

    assert '## EVENT' in caplog.text
    assert str(event) in caplog.text
    assert '## RESPONSE' in caplog.text
    assert str(response) in caplog.text

    json_resp = json.loads(response['body'])
    assert len(json_resp['data']) == 14


def test_health_check(client: TestClient) -> None:
    response = client.get('/')
    assert response.status_code == 200
    resp_json = response.json()
    assert resp_json['message'] == 'Hello there!'
