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
        """
        Configure this client to use the specified username/password security settings.

        :param  string   username:     The username for your AvaTax user account
        :param  string   password:     The password for your AvaTax user account
        :param  int      accountId:    The account ID of your avatax account
        :param  string   licenseKey:   The license key of your avatax account
        :param  string   bearerToken:  The OAuth 2.0 token provided by Avalara Identity
        :return: AvaTaxClient
        """
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
        """
        Test connectivity and version of the service.

        This API helps diagnose connectivity problems between your
        application and AvaTax; you may call this API even if you do not
        have verified connection credentials.The results of this API call
        will help you determine whether your computer can contact AvaTax
        via the network, whether your authentication credentials are
        recognized, and the roundtrip time it takes to communicate with
        AvaTax.

        :return: object
        """
        return requests.get('{}/api/v2/utilities/ping'.format(self.base_url),
                            auth=self.auth, headers=self.client_header)

    def create_transaction(self, include=None, model=None):
        """
        Create a new transaction.

        Records a new transaction in AvaTax.

        The `CreateTransaction` endpoint uses the configuration values
        specified by your company to identify the correct tax rules
        and rates to apply to all line items in this transaction, and
        reports the total tax calculated by AvaTax based on your company's
        configuration and the data provided in this API call.

        If you don't specify type in the provided data, a new transaction
        with type of SalesOrder will be recorded by default.

        A transaction represents a unique potentially taxable action that
        your company has recorded, and transactions include actions like sales,
        purchases, inventory transfer, and returns (also called refunds).
        You may specify one or more of the following values in the '$include'
        parameter to fetch additional nested data, using commas to separate
        multiple values:

          * Lines
          * Details (implies lines)
          * Summary (implies details)
          * Addresses
          * SummaryOnly (exclude lines and details for a smaller response)

        If you omit the `include` parameter, the API will assume you
        want `Summary,Addresses`.

          :param string include: A comma separated list of child objects to return underneath the primary object.
          :param object model: The transaction you wish to create
        :return: object
        """
        if not model:
            raise ValueError('A model with transaction detail is required')
        return requests.post('{}/api/v2/transactions/create'.format(
                             self.base_url), params=include, json=model,
                             auth=self.auth, headers=self.client_header)

    def resolve_address(self, address):
        """
        Retrieve geolocation information for a specified address.

        Resolve an address against Avalara's address-validation system. If the
        address can be resolved, this API provides the latitude and longitude
        of the resolved location. The value 'resolutionQuality' can be used
        to identify how closely this address can be located. If the address
        cannot be clearly located, use the 'messages' structure to learn more
        about problems with this address.
        This is the same API as the POST /api/v2/addresses/resolve endpoint.
        Both verbs are supported to provide for flexible implementation.


            :param string line1: Line 1
            :param string line2: Line 2
            :param string line3: Line 3
            :param string city: City
            :param string region: State / Province / Region
            :param string postalCode: Postal Code / Zip Code
            :param string country: Two character ISO 3166 Country Code
                (see /api/v2/definitions/countries for a full list)
            :param string textCase: selectable text case for address validation
                (See TextCase::* for a list of allowable values)
            :param float latitude: Geospatial latitude measurement
            :param float longitude: Geospatial longitude measurement
        :return: object
        """
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
        """
        Commit a transaction for reporting.

        Marks a transaction by changing its status to 'Committed'.
        Transactions that are committed are available to be reported to a tax
        authority by Avalara Managed Returns. A transaction represents a
        unique potentially taxable action that your company has recorded, and
        transactions include actions like sales, purchases, inventory
        transfer, and returns (also called refunds). Any changes made to
        a committed transaction will generate a transaction history.


          :param string companyCode: The company code of the company that recorded this transaction
          :param string transactionCode: The transaction code to commit
          :param object model: The commit request you wish to execute
        :return: object
        """
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
