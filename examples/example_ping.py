"""Example of ping method to test connectivity and version of the service."""
import os
from sandbox_client import SandboxClient


def create_client():
    """Construct a new AvaTaxClient in a Sandbox Environment

    'test app': The name of the application
    'ver 0.0': Version number of the application
    'test machine': Name of the machine on which this code is executing

    """
    example_client = SandboxClient('test app', 'ver 0.0', 'test machine')
    example_client.add_credentials(
        os.environ.get('USERNAME', ''),
        os.environ.get('PASSWORD', ''))
    return example_client


def example_ping():
    """
    Assign example_client to the SandboxClient instance returned from create_client().

    Return example_client with the ping method.
    """
    example_client = create_client()
    return example_client.ping()
