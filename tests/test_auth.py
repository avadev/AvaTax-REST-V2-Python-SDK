"""Test the authorization."""
import pytest
from sandbox_client import SandboxClient


test_creds = {
    'username': 'joe',
    'password': '1234',
    }

test_creds_2 = {
    'username': '123321',
    'password': 'abcdef',
    }

test_creds_3 = {
    'bearer_token': '123321',
    }

@pytest.fixture
def client_function():
    """Fucking client."""
    sb = SandboxClient('cool app', '1000', 'cool machine')
    return sb


def test_username_auth(client_function):
    """Test passing in username to authorization."""
    client_function.add_credentials(test_creds)
    assert client_function.auth.username == 'joe'


def test_username_auth_2(client_function):
    """Test passing in username to authorization."""
    client_function.add_credentials(test_creds)
    assert client_function.auth.password == '1234'


def test_account_id_auth(client_function):
    """Test passing in account id to authorization."""
    client_function.add_credentials(test_creds_2)
    assert client_function.auth.username == '123321'


def test_account_id_auth_2(client_function):
    """Test passing in account id to authorization."""
    client_function.add_credentials(test_creds_2)
    assert client_function.auth.password == 'abcdef'


def test_bearer_token_auth(client_function):
    """Test passing in bearer to authorization."""
    client_function.add_credentials(test_creds_3)
    assert client_function.auth == 'Bearer 123321'


def test_auth_raises_value_error(client_function):
    """Test value error is raised with imporper authorization."""
    with pytest.raises(ValueError):
        client_function.add_credentials({})
