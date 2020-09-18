import json

from ngr.main import handler


def test_handler(caplog):
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
