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
from datetime import datetime


class TransactionBuilder(object):
    """Transaction builder class."""

    def __init__(self, client, comp_code, type_, cust_code):
        """."""
        self.client = client
        self.line_num = 1
        self.create_model = {
            'addresses': {},
            'companyCode': comp_code,
            'customerCode': cust_code,
            'type': type_,
            'date': '{}'.format(datetime.now()),
            'lines': []
        }

    def with_commit(self):
        """."""
        self.create_model['commit'] = True
        return self

    def with_transaction_code(self, code):
        """."""
        self.create_model['code'] = code
        return self

    def with_type(self, type_):
        """."""
        self.create_model['type'] = type_
        return self

    def with_address(self, address_type, address):
        """."""
        if self.create_model['addresses'] == {}:
            self.create_model['addresses'][address_type] = address
        return self

    def with_latlong(self, address_type, lat, long_):
        """."""
        self.create_model['addresses'][address_type] = {'latitude': lat,
                                                        'longitude': long_}
        return self

    def with_line(self, amount, quantity, item_code, tax_code):
        """."""
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
        """."""
        temp = {
            'number': self.line_num,
            'quantity': 1,
            'amount': amount,
            'exemptionCode': exemption_code,
            'itemCode': item_code
        }
        self.create_model['lines'].append(temp)
        self.line_num += 1

    def get_most_recent_line(self, member_name=None):
        """."""
        return self.create_model['lines'][-1]

    def create(self):
        """."""
        include = None
        return self.client.create_transaction(include, self.create_model)

    def with_line_tax_override(self, type_, reason, tax_amount, tax_date):
        """."""
        line = self.get_most_recent_line('WithLineTaxOverride')
        line['taxOverride'] = {
            'type': type_,
            'reason': reason,
            'taxAmount': tax_amount,
            'taxDate': tax_date
        }
        return self
