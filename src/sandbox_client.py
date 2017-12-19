"""Class and methods for the sandbox client."""
import requests
from requests.auth import HTTPBasicAuth


class SandboxClient(object):
    """Class for our sandbox client."""

    def __init__(self, app_name, app_version, machine_name):
        """Initialize the sandbox client."""
        self.base_url = 'https://sandbox-rest.avatax.com'
        self.auth = None
        self.app_name = app_name
        self.app_version = app_version
        self.machine_name = machine_name
        self.client_id = '{};{};python_sdk;17.6;{};'.format(app_name, app_version, machine_name)

    def add_credentials(self, authentication):
        """Add credentials to sandbox client."""
        try:
            username = authentication['username']
            password = authentication['password']
            self.auth = HTTPBasicAuth(username, password)
        except KeyError:
            try:
                username = authentication['account_id']
                password = authentication['license_key']
                self.auth = HTTPBasicAuth(username, password)
            except KeyError:
                try:
                    bearer_token = authentication['bearer_token']
                    self.auth = 'Bearer {}'.format(bearer_token)
                except KeyError:
                    raise ValueError("You need something")

    def ping(self):
        """Pinging some pong."""
        r = requests.get('{}/api/v2/utilities/ping'.format(self.base_url), auth=self.auth)
        return r

    def create_transaction():
        """."""
        pass

    def resolve_address():
        """."""
        pass

    def commit_transaction():
        """."""
        pass
        
    def void_transaction():
        """."""
        pass
