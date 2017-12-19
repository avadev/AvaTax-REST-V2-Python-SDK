"""Test the client model."""
import pytest
from sandbox_client import SandboxClient

@pytest.fixture
def client_function():
    """Fucking client."""
    sb = SandboxClient('cool app', '1000', 'cool machine')
    return sb


def test_client_can_be_created(client_function):
    """Test that the client object can be created."""
    assert isinstance(client_function, SandboxClient)


def test_client_has_base_url_attribute(client_function):
    """Test the client model has attributes available."""
    assert client_function.base_url == 'https://sandbox-rest.avatax.com'


def test_client_has_app_name_attribute(client_function):
    """Test the client model has attributes available."""
    assert client_function.app_name == 'cool app'


def test_client_has_app_version_attribute(client_function):
    """Test the client model has attributes available."""
    assert client_function.app_version == '1000'


def test_client_has_machine_name_attribute(client_function):
    """Test the client model has attributes available."""
    assert client_function.machine_name == 'cool machine'


def test_that_client_id_is_created(client_function):
    """Test that the client id is created and properly formatted."""
    assert client_function.client_id == 'cool app;1000;python_sdk;17.6;cool machine;'