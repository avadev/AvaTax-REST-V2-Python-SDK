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
def invalid_auth():
    """Fucking gonna get logged in client."""
    sb = SandboxClient('cool app', '1000', 'cool machine')
    creds = {
        'username': 'potato',
        'password': 'tomato'
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


@pytest.fixture
def invalid_account_id():
    """Fucking gonna get logged in client."""
    sb = SandboxClient('cool app', '1000', 'cool machine')
    creds = {
        'account_id': '8998',
        'license_key': 'P90S4'
    }
    sb.add_credentials(creds)
    return sb


@pytest.fixture
def invalid_bearer():
    """Fucking gonna get logged in client."""
    sb = SandboxClient('cool app', '1000', 'cool machine')
    creds = {
        'bearer_token': '8998',
    }
    sb.add_credentials(creds)
    return sb


def test_ping_makes_connection(client_unauth):
    """Testing client without authorization."""
    assert client_unauth.ping().status_code == 200


def test_ping_auth_is_false_connection(client_unauth):
    """Testing client without authorization."""
    assert '"authenticated":false' in client_unauth.ping().text


def test_ping_auth_is_TRUE_connection(client_auth):
    """Testing client without authorization."""
    assert '"authenticated":true' in client_auth.ping().text


def test_ping_auth_is_TRUE_using_client_id(client_auth_id):
    """Testing client with authorization from account ID."""
    assert '"authenticated":true' in client_auth_id.ping().text


def test_ping_auth_with_invalid_user_and_pass(invalid_auth):
    """Testing client without authorization."""
    assert '"authenticated":false' in invalid_auth.ping().text


def test_ping_auth_with_invalid_account_id(invalid_account_id):
    """Testing client without valid account id."""
    assert '"authenticated":false' in invalid_account_id.ping().text


# def test_ping_auth_with_invalid_bearer(invalid_bearer):
#     """Testing client without authorization."""
#     assert '"authenticated":false' in invalid_bearer.ping().text