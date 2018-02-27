"""
Methods attached to the SDK client object(to be auto-generated in the future).

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
from _str_version import str_type


class Mixin:
    """Mixin class contain methods attached to Client class."""

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

        :return: requests response object
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

          :param string include: A comma separated list of child objects to
            return underneath the primary object.
          :param object model: The transaction you wish to create
        :return: requests response object
        """
        if not all(isinstance(i, (dict, type(None))) for i in [model]):
            raise ValueError('Input(s) must be py dict. or none type object')
        return requests.post('{}/api/v2/transactions/create'.format(
                             self.base_url), params=include, json=model,
                             auth=self.auth, headers=self.client_header)

    def resolve_address(self, address=None):
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
        :return: requests response object
        """
        if not isinstance(address, (dict, type(None))):
            raise ValueError('Input must be py dictionary or none type object')
        payload = address
        return requests.get('{}/api/v2/addresses/resolve'.format(
                            self.base_url), params=payload, auth=self.auth,
                            headers=self.client_header)

    def commit_transaction(self, comp_code=None, trans_code=None, commit=True):
        r"""
        Commit a transaction for reporting.

        Marks a transaction by changing its status to 'Committed'.
        Transactions that are committed are available to be reported to a tax
        authority by Avalara Managed Returns. A transaction represents a
        unique potentially taxable action that your company has recorded, and
        transactions include actions like sales, purchases, inventory
        transfer, and returns (also called refunds). Any changes made to
        a committed transaction will generate a transaction history.


          :param string companyCode: The company code of the company \
            that recorded this transaction
          :param string transactionCode: The transaction code to commit
          :param object model: The commit request you wish to execute
        :return: requests response object
        """
        if not all(isinstance(i, str_type) for i in [trans_code, comp_code]):
            raise ValueError('Input(s) must be py string or none type object')
        commit_model = {'commit': commit}
        return requests.post('{}/api/v2/companies/{}/transactions/{}/commit'.
                             format(self.base_url, comp_code, trans_code),
                             auth=self.auth, json=commit_model)

    def void_transaction(self, comp_code=None, trans_code=None,
                         code_model='DocVoided'):
        r"""
        Void a transaction.

        Voids the current transaction uniquely identified by this URL.
        A transaction represents a unique potentially taxable action that your
        company has recorded, and transactions include actions like sales,
        purchases, inventory transfer, and returns (also called refunds). When
        you void a transaction, that transaction's status is recorded as
        'DocVoided'. Transactions that have been previously reported to a
        tax authority by Avalara Managed Returns are no longer available
        to be voided.

            :param string companyCode: The company code of the company \
                that recorded this transaction
            :param string transactionCode: The transaction code to void
            :param object model: The void request you wish to execute
        :return: object
        """
        if not all(isinstance(i, str_type) for i in [code_model,
                                                     trans_code,
                                                     comp_code]):
            raise ValueError('Input(s) must be py string or none type object')
        model = {'code': code_model}
        return requests.post('{}/api/v2/companies/{}/transactions/{}/void'.format(
            self.base_url, comp_code, trans_code), json=model, auth=self.auth,
            headers=self.client_header)
