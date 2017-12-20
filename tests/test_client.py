"""Test the client model."""
from client import AvataxClient


def test_client_can_be_created(unauth_client):
    """Test that the client object can be created."""
    assert isinstance(unauth_client, AvataxClient)


def test_client_has_base_url_attribute(unauth_client):
    """Test the client model has attributes available."""
    assert unauth_client.base_url == 'https://sandbox-rest.avatax.com'


def test_client_has_app_name_attribute(unauth_client):
    """Test the client model has attributes available."""
    assert unauth_client.app_name == 'test app'


def test_client_has_app_version_attribute(unauth_client):
    """Test the client model has attributes available."""
    assert unauth_client.app_version == 'ver 0.0'


def test_client_has_machine_name_attribute(unauth_client):
    """Test the client model has attributes available."""
    assert unauth_client.machine_name == 'test machine'


def test_that_client_id_is_created(unauth_client):
    """Test that the client id is created and properly formatted."""
    assert unauth_client.client_id == 'test app;ver 0.0;python_sdk;17.6;test machine;'

