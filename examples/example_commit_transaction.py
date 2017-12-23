"""Example using commit transaction to mark a transaction's status as 'Committed'."""
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