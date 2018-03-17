"""
AvaTax Software Development Kit for Python.

(c) 2004-2017 Avalara, Inc.

For the full copyright and license information, please view the LICENSE
file that was distributed with this source code.

@author     Robert Bronson
@author     Phil Werner
@author     Adrienne Karnoski
@author     Han Bao
@copyright  2004-2017 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    TBD
@link       https://github.com/avadev/AvaTax-REST-V2-Python-SDK
"""
from requests.auth import HTTPBasicAuth
from _str_version import str_type
import client_methods
import os


class AvataxClient(client_methods.Mixin):
    """Class for our Avatax client."""

    def __init__(self, app_name=None, app_version=None, machine_name=None,
                 environment=None):
        """
        Initialize the sandbox client.

        By default the client object enviroment will be production. For
        sandbox API, set the enviroment variable to sandbox.

            :param  string  app_name: The name of your Application
            :param  string/integer  app_version:  Version of your Application
            :param  string  machine_name: Name of machine you are working on
            :param  string  enviroment: Default enviroment is production,
                input sandbox, for the sandbox API
        :return: object
        """
        if not all(isinstance(i, str_type) for i in [app_name,
                                                     machine_name,
                                                     environment]):
            raise ValueError('Input(s) must be string or none type object')
        self.base_url = 'https://rest.avatax.com'
        if environment:
            if environment.lower() == 'sandbox':
                self.base_url = 'https://sandbox-rest.avatax.com'
            elif environment[:8] == 'https://' or environment[:7] == 'http://':
                self.base_url = environment
        self.auth = None
        self.app_name = app_name
        self.app_version = app_version
        self.machine_name = machine_name
        self.client_id = '{}; {}; Python SDK; 18.2; {};'.format(app_name,
                                                                app_version,
                                                                machine_name)
        self.client_header = {'X-Avalara-Client': self.client_id}

    def add_credentials(self, username=None, password=None):
        """
        Configure this client for the specified username/password security.

        :param  string  username:    The username of your AvaTax user account
        :param  string  password:    The password of your AvaTax user account
        :param  int     accountId:   The account ID of your avatax account
        :param  string  licenseKey:  The license key of your avatax account
        :param  string  bearerToken: The OAuth 2.0 token provided by Avalara
        :return: AvaTaxClient

        Note: if you wish to use Bearer token, enter it as the ONLY argument to this method.
        """
        if not all(isinstance(i, str_type) for i in [username, password]):
            raise ValueError('Input(s) must be string or none type object')
        if username and not password:
            self.client_header['Authorization'] = 'Bearer ' + username
        else:
            self.auth = HTTPBasicAuth(username, password)
        return self

# to generate a client object on initialization of this file, uncomment the script below
# if __name__ == '__main__':  # pragma no cover
#     """Creating a client with credential, must have env variables username & password."""
#     client = AvataxClient('my test app',
#                           'ver 0.0',
#                           'my test machine',
#                           'sandbox')
#     c = client.add_credentials(os.environ.get('USERNAME', ''),
#                                os.environ.get('PASSWORD', ''))
#     print(client.ping().text)
#     tax_document = {
#         'addresses': {'SingleLocation': {'city': 'Irvine',
#                                          'country': 'US',
#                                          'line1': '123 Main Street',
#                                          'postalCode': '92615',
#                                          'region': 'CA'}},
#         'commit': False,
#         'companyCode': 'DEFAULT',
#         'currencyCode': 'USD',
#         'customerCode': 'ABC',
#         'date': '2017-04-12',
#         'description': 'Yarn',
#         'lines': [{'amount': 100,
#                   'description': 'Yarn',
#                    'itemCode': 'Y0001',
#                    'number': '1',
#                    'quantity': 1,
#                    'taxCode': 'PS081282'}],
#         'purchaseOrderNo': '2017-04-12-001',
#         'type': 'SalesInvoice'}
