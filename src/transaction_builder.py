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

TransactionBuilder helps you construct a new transaction using a literate interface
"""
from datetime import datetime


class TransactionBuilder(object):
    """Transaction builder class."""

    def __init__(self, client, comp_code, type_, cust_code):
        """
        The TransactionBuilder helps you construct a new transaction using a literate interface.

        :param AvaTaxClient  client:     The AvaTaxClient object to use to create this transaction
        :param string        comp_code:  The code of the company for this transaction
        :param DocumentType  type:       The type of transaction to create (See DocumentType::* for a list of allowable values)
        :param string        cust_code:  The customer code for this transaction
        """
        # The client that will be used to create the transaction
        self.client = client
        # Keeps track of line number when adding multiple lines
        self.line_num = 1
        # The in-progress model
        self.create_model = {
            'companyCode': comp_code,
            'customerCode': cust_code,
            'type': type_,
            'date': '{}'.format(datetime.now()),
            'lines': []
        }

    def with_commit(self):
        """
        Set the commit flag of the transaction.

        If commit is set to False, the transaction will only be saved.
        """
        self.create_model['commit'] = True
        return self

    def with_transaction_code(self, code):
        """
        Set a specific transaction code.

        :param  string  code:  Specific tansaction code
        :return:  TransactionBuilder
        """
        self.create_model['code'] = code
        return self

    def with_type(self, type_):
        """
        Set the document type.

        :param  string  type: (See DocumentType::* for a list of allowable values)
        :return: TransactionBuilder
        """
        self.create_model['type'] = type_
        return self

    def with_address(self, address_type, address):
        """
        Add an address to this transaction.

        :param  string  address_type:  Address Type (See AddressType::* for a list of allowable values)
        :param  dictionary  address:  A dictionary containing the following
            line1         The street address, attention line, or business name
                            of the location.
            line2         The street address, business name, or apartment/unit
                            number of the location.
            line3         The street address or apartment/unit number
                            of the location.
            city          City of the location.
            region        State or Region of the location.
            postal_code    Postal/zip code of the location.
            country       The two-letter country code of the location.
        :return: TransactionBuilder
        """
        self.create_model.setdefault('addresses', {})
        self.create_model['addresses'][address_type] = address
        return self

    def with_line_address(self, type_, address):
        """."""
        temp = self.get_most_recent_line('WithLineAddress')
        temp['addresses'][type_] = address
        return self

    def with_latlong(self, address_type, lat, long_):
        """
        Add a lat/long coordinate to this transaction.

        :param  string  type:       Address Type (See AddressType::* for a list of allowable values)
        :param  float   lat:   The latitude of the geolocation for this transaction
        :param  float   long_:  The longitude of the geolocation for this transaction
        :return:  TransactionBuilder
        """
        self.create_model['addresses'][address_type] = {'latitude': lat,
                                                        'longitude': long_}
        return self

    def with_line(self, amount, quantity, item_code, tax_code):
        """
        Add a line to the transaction.

        :param  float   amount:   Value of the item.
        :param  float   quantity: Quantity of the item.
        :param  string  item_code: Code of the item.
        :param  string  tax_code:  Tax Code of the item. If left blank, the default item (P0000000) is assumed.
        :return:  TransactionBuilder
        """
        temp = {
            'number': self.line_num,
            'quantity': quantity,
            'amount': amount,
            'taxCode': tax_code,
            'itemCode': item_code
        }
        self.create_model['lines'].append(temp)
        self.line_num += 1

    def with_exempt_line(self, amount, item_code, exemption_code):
        """
        Add a line with an exemption to this transaction.

        :param   float   amount:         The amount of this line item
        :param   string  item_code:      The code for the item
        :param   string  exemption_code:  The exemption code for this line item
        :return:  TransactionBuilder
        """
        temp = {
            'number': self.line_num,
            'quantity': 1,
            'amount': amount,
            'exemptionCode': exemption_code,
            'itemCode': item_code
        }
        self.create_model['lines'].append(temp)
        self.line_num += 1

    def with_diagnostics(self):
        """."""
        self.create_model['debugLevel'] = 'Diagnostic'
        return self

    def with_discount_amount(self, discount):
        """."""
        self.create_model['discount'] = discount

    def with_item_discount(self, discounted):
        """."""
        temp = self.get_most_recent_line('WithItemDiscount')
        temp['discounted'] = discounted
        return self

    def with_parameter(self, name, value):
        """."""
        self.create_model.setdefault('parameters', {})
        self.create_model['parameters'][name] = value
        return self

    def with_line_parameter(self, name, value):
        """."""
        temp = self.get_most_recent_line('WithLineParameter')
        temp.setdefault('parameters', {})
        temp['parameters'][name] = value
        return self

    def get_most_recent_line(self, member_name=None):
        """
        Check to see if the current model has a line.

        :return: TransactionBuilder
        """
        return self.create_model['lines'][-1]

    def create(self):
        """
        Create this transaction.

        :return: TransactionModel
        """
        include = None
        return self.client.create_transaction(include, self.create_model)

    def with_line_tax_override(self, type_, reason, tax_amount, tax_date):
        """
        Add a line-level Tax Override to the current line.

        A TaxDate override requires a valid DateTime object to be passed.

        :param  string  type:        Type of the Tax Override (See TaxOverrideType::* for a list of allowable values)
        :param  string  reason:      Reason of the Tax Override.
        :param  float   tax_amount:  Amount of tax to apply. Required for a TaxAmount Override.
        :param  date    tax_date:    Date of a Tax Override. Required for a TaxDate Override.
        :return:  TransactionBuilder
        """
        line = self.get_most_recent_line('WithLineTaxOverride')
        line['taxOverride'] = {
            'type': type_,
            'reason': reason,
            'taxAmount': tax_amount,
            'taxDate': tax_date
        }
        return self

    def with_tax_override(self, type_, reason, tax_amount, tax_date):
        """."""
        self.create_model['taxOverride'] = {
            'type': type_,
            'reason': reason,
            'taxAmount': tax_amount,
            'taxDate': tax_date
        }

    def with_separate_address_line(self, amount, type_, address):
        """."""
        temp = {
            'number': self.line_num,
            'quantity': 1,
            'amount': amount,
            'addresses': {
                type_: address
            }
        }

        self.create_model['lines'].append(temp)
        self.line_num += 1
        return self

    def create_adjustment_request(self, desc, reason):
        """."""
        return {
            'newTransaction': self.create_model,
            'adjustmentDescription': desc,
            'adjustmentReason': reason
        }
