"""Test the client model."""
import pytest
from sandbox_client import SandboxClient
import os

@pytest.fixture
def client_unauth():
    """Fucking client."""
    sb = SandboxClient('cool app', '1000', 'cool machine')
    return sb

@pytest.fixture
def client_auth():
    """Fucking gonna get logged in client."""
    sb = SandboxClient('cool app', '1000', 'cool machine')
    creds = {
        'username': os.environ.get('USERNAME', ''),
        'password': os.environ.get('PASSWORD', '')
    }
    sb.add_credentials(creds)
    return sb


@pytest.fixture
def client_auth_id():
    """Fucking gonna get logged in client."""
    sb = SandboxClient('cool app', '1000', 'cool machine')
    creds = {
        'account_id': os.environ.get('ACCOUNT_ID', ''),
        'license_key': os.environ.get('LICENSE_KEY', '')
    }
    sb.add_credentials(creds)
    return sb


# def test_ping_makes_connection(client_unauth):
#     """Testing client without authorization."""
#     assert client_unauth.ping().status_code == 200


# def test_ping_auth_is_false_connection(client_unauth):
#     """Testing client without authorization."""
#     assert '"authenticated":false' in client_unauth.ping().text


# def test_ping_auth_is_TRUE_connection(client_auth):
#     """Testing client without authorization."""
#     assert '"authenticated":true' in client_auth.ping().text


def test_ping_auth_is_TRUE_using_client_id(client_auth_id):
    """Testing client without authorization."""
    assert '"authenticated":true' in client_auth_id.ping().text