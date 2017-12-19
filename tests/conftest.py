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
    creds = {
        'username': os.environ.get('USERNAME', ''),
        'password': os.environ.get('PASSWORD', '')
    }
    client.add_credentials(creds)
    return client


@pytest.fixture
def auth_client_loggedin_with_id():
    """Create an instance of SanboxClient with authentification using userID/licenseKey pair."""
    client = SandboxClient('test app', 'ver 0.0', 'test machine')
    creds = {
        'account_id': os.environ.get('ACCOUNT_ID', ''),
        'license_key': os.environ.get('LICENSE_KEY', '')
    }
    client.add_credentials(creds)
    return client
