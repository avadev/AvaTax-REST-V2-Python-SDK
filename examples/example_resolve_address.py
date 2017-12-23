"""Example of resolve address to retrieve geolocation information for a specified address."""
import os
from sandbox_client import SandboxClient


def create_client():
    """
    Construct a new AvaTaxClient in a Sandbox Environment

    'test app': The name of the application
    'ver 0.0': Version number of the application
    'test machine': Name of the machine on which this code is executing

    Add credentials to configure client to use the specified username/password security settings.

    Your Sandbox username and password should be set as environment variables prior to executing the request.

    Return example_client.
    """
    example_client = SandboxClient('test app', 'ver 0.0', 'test machine')
    example_client.add_credentials(
        os.environ.get('USERNAME', ''),
        os.environ.get('PASSWORD', ''))
    return example_client


def example_resolve_address():
    """
    Assign example_client to the SandboxClient instance returned from create_client().

    The address dictionary is used as a parameter in the resolve address request.
    This will be the address you are the geolocation information for.

    Return example_client with the resolve_address method, passing address as an argument."""
    example_client = create_client()
    address = {
        'line1': '410 Terry Ave. North',
        'city': 'Seattle',
        'region': 'WA',
        'postal_code': '98109',
    }
    return example_client.resolve_address(address)
