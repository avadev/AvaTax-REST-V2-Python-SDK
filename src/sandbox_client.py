"""Class and methods for the sandbox client."""
import requests
from requests.auth import HTTPBasicAuth
import os


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
        self.client_header = {'X-Avalara-Client': self.client_id}

    def add_credentials(self, authentication):
        """Add credentials to sandbox client."""
        try:
            username = authentication['username']
            password = authentication['password']
            self.auth = HTTPBasicAuth(username, password)
        except KeyError:
            try:
                account_id = authentication['account_id']
                license_key = authentication['license_key']
                self.auth = HTTPBasicAuth(account_id, license_key)
            except KeyError:
                try:
                    bearer_token = authentication['bearer_token']
                    self.auth = 'Bearer {}'.format(bearer_token)
                except KeyError:
                    raise ValueError("You need something")

    def ping(self):
        """Ping the avatax api, can be called with or without credential."""
        return requests.get('{}/api/v2/utilities/ping'.format(self.base_url),
                            auth=self.auth, headers=self.client_header)

    def create_transaction(self, include=None, model=None):
        """Create transaction."""
        if not model:
            raise ValueError('A model with transaction detail is required')
        return requests.post('{}/api/v2/transactions/create'.format(
                             self.base_url), params=include, json=model,
                             auth=self.auth, headers=self.client_header)

    def resolve_address(self, address):
        """Verify address and returns tax region information."""
        payload = address
        try:
            payload['postalCode'] = payload['postal_code']
            del payload['postal_code']
        except KeyError:
            pass
        try:
            payload['textCase'] = payload['text_case']
            del payload['text_case']
        except KeyError:
            pass
        return requests.get('{}/api/v2/addresses/resolve'.format(
                            self.base_url), params=payload, auth=self.auth,
                            headers=self.client_header)

    def commit_transaction(self, comp_code=None, trans_code=None, commit=True):
        """Commit a single transaction with given transaction_id."""
        if not comp_code or not trans_code:
            raise ValueError('A company code and a transaction code is required')
        commit_model = {'commit': commit}
        return requests.post('{}/api/v2/companies/{}/transactions/{}/commit'.
                             format(self.base_url, comp_code, trans_code),
                             auth=self.auth, json=commit_model)

    def void_transaction():
        """."""
        pass

if __name__ == '__main__':  # pragma no cover
    sb = SandboxClient('cool app', '1000', 'cool machine')
    sb.add_credentials({
        'username': os.environ.get('USERNAME'),
        'password': os.environ.get('PASSWORD')
    })
    print(sb.ping().text)
    tax_document = {
        'addresses': {'SingleLocation': {'city': 'Irvine',
                                         'country': 'US',
                                         'line1': '123 Main Street',
                                         'postalCode': '92615',
                                         'region': 'CA'}},
        'commit': False,
        'companyCode': 'DEFAULT',
        'currencyCode': 'USD',
        'customerCode': 'ABC',
        'date': '2017-04-12',
        'description': 'Yarn',
        'lines': [{'amount': 100,
                  'description': 'Yarn',
                   'itemCode': 'Y0001',
                   'number': '1',
                   'quantity': 1,
                   'taxCode': 'PS081282'}],
        'purchaseOrderNo': '2017-04-12-001',
        'type': 'SalesInvoice'}


# You may specify one or more of the following values in the $include parameter to fetch additional nested data, using commas to separate multiple values:

# Lines
# Details (implies lines)
# Summary (implies details)
# Addresses
# SummaryOnly (omit lines and details - reduces API response size)
# LinesOnly (omit details - reduces API response size)
# ForceTimeout - Simulates a timeout. This adds a 30 second delay and error to your API call. This can be used to test your code to ensure it can respond correctly in the case of a dropped connection.
# If you omit the $include parameter, the API will assume you want Summary,Addresses.