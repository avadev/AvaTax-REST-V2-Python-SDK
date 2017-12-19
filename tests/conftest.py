"""Conftest is a file recognize by pytest module, allowing us to share fixture across multiple tests."""
from sandbox_client import SandboxClient
import os
import pytest


@pytest.fixture(scope='function')
def unauth_client():
    """Create an instance of SanboxClient without authentification."""
    return SandboxClient('test app', 'ver 0.0', 'test machine')


@pytest.fixture(scope='function')
def auth_client_loggedin_with_username():
    """Create an instance of SanboxClient with authentification using username/password pair."""
    client = SandboxClient('test app', 'ver 0.0', 'test machine')
    client.add_credentials(os.environ.get('USERNAME', ''), os.environ.get('PASSWORD', ''))
    return client


@pytest.fixture
def auth_client_loggedin_with_id():
    """Create an instance of SanboxClient with authentification using userID/licenseKey pair."""
    client = SandboxClient('test app', 'ver 0.0', 'test machine')
    client.add_credentials(os.environ.get('ACCOUNT_ID', ''), os.environ.get('LICENSE_KEY', ''))
    return client


@pytest.fixture
def auth_client():
    """Helper fixture."""
    client = SandboxClient('test app', 'ver 0.0', 'test machine')
    client.add_credentials(os.environ.get('USERNAME', ''), os.environ.get('PASSWORD', ''))
    return client


@pytest.fixture
def good_address():
    """Properly filled address fixture for testing resolve address."""
    address = {
        'line1': '410 Terry Ave. North',
        'city': 'Seattle',
        'region': 'WA',
        'postal_code': '98109',
    }
    return address

