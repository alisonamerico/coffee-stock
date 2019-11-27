import json


def test_status_code_not_authenticaded(client):
    """Authentication credentials were not provided."""
    response = client.get('/api/')
    assert response.status_code == 403


def test_content_http_403_forbidden(client):
    """Authentication credentials were not provided."""
    response = client.get('/api/')
    dct = extract_and_parse_json(response)
    assert dct == {"detail": "Authentication credentials were not provided."}


def test_status_code_get_method_not_allowed(client):
    """Method \"GET\" not allowed."""
    response = client.get('/rest-auth/login/')
    assert response.status_code == 405


def test_content_get_method_not_allowed(client):
    """Method \"GET\" not allowed."""
    response = client.get('/rest-auth/login/')
    dct = extract_and_parse_json(response)
    assert dct == {"detail": "Method \"GET\" not allowed."}


def extract_and_parse_json(response):
    s = response.content.decode(response.charset)
    dct = json.loads(s)
    return dct



