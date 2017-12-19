from sandbox_client import SandboxClient


class Client(SandboxClient):
    """."""

    def __init__(self, app_name, app_version, machine_name):
        """Init regular client obj."""
        super(Client, self).__init__(app_name, app_version, machine_name)
        self.base_url = 'https://rest.avatax.com'
