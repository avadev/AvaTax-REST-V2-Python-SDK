"""Class and methods for the sandbox client."""
import requests
from requests.auth import HTTPBasicAuth


class SandboxClient(object):
    """Class for our sandbox client."""

    def __init__(self, app_name, app_version, machine_name):
        """Initialize the sandbox client."""
        self.base_url = 'https://sandbox-rest.avatax.com'
        self.app_name = app_name
        self.app_version = app_version
        self.machine_name = machine_name
        self.client_id = '{};{};python_sdk;17.6;{};'.format(app_name, app_version, machine_name)

    def add_credentials(self, authentication):
        """Add credentials to sandbox client."""
        if authentication['username']:
            username = authentication['username']
            password = authentication['password']
            self.auth = HTTPBasicAuth(username, password)
        elif authentication['account_id']:
            account_id = authentication['account_id']
            license_key = authentication['license_key']
            self.auth = HTTPBasicAuth(account_id, license_key)
        else:
            bearer_token = authentication['bearer_token']
            self.auth = 'Bearer {}'.format(bearer_token)

    def ping(self):
        """Pinging some pong."""
        r = requests.get('{}/api/v2/utilities/ping'.format(self.base_url), auth=self.auth)
        return r
