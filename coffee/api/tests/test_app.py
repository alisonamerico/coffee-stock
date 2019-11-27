from coffee.api.apps import ApiConfig


def test_apps():
    assert ApiConfig.name == 'api'
