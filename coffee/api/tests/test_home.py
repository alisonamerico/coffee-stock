from django.test import Client


def test_status_code(client: Client):
    resp = client.get('/api/')
    assert resp.status_code == 200

# def test_view_status_code(client: Client, user):
#     username = 'foo'
#     password = 'bar'
#     user.objects.create_user(username=username, password=password)
#     client.login(username=username, password=password)
#     resp = client.get('/myapi/api/')
#     assert resp.status_code == 200
