"""
AvaTax Software Development Kit for Python.

   Copyright 2019 Avalara, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

@author     Robert Bronson
@author     Phil Werner
@author     Adrienne Karnoski
@author     Han Bao
@copyright  2019 Avalara, Inc.
@license    https://www.apache.org/licenses/LICENSE-2.0
@version    TBD
@link       https://github.com/avadev/AvaTax-REST-V2-Python-SDK

Transaction Builder methods(to be auto generated)
"""


class Mixin:
    """Mixin containing methods attached to TransactionBuilder Class."""

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
        r"""
        Set the document type.

        :param  string  type: Address Type \
        (See DocumentType::* for a list of allowable values)

        :return: TransactionBuilder
        """
        self.create_model['type'] = type_
        return self

    def with_address(self, address_type, address):
        r"""
        Add an address to this transaction.

        :param  string  address_type:  Address Type \
        (See AddressType::* for a list of allowable values)

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

    def with_line_address(self, address_type, address):
        r"""
        Add an address to this line.

        :param  string  address_type:  Address Type \
        (See AddressType::* for a list of allowable values)
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
        temp = self.get_most_recent_line('WithLineAddress')
        temp.setdefault('addresses', {})
        temp['addresses'][address_type] = address
        return self

    def with_latlong(self, address_type, lat, long_):
        r"""
        Add a lat/long coordinate to this transaction.

        :param  string  type:       Address Type \
        (See AddressType::* for a list of allowable values)

        :param  float   lat:   The geolocated latitude for this transaction
        :param  float   long_: The geolocated longitude for this transaction

        :return:  TransactionBuilder
        """
        self.create_model.setdefault('addresses', {})
        self.create_model['addresses'][address_type] = {'latitude': float(lat),
                                                        'longitude': float(long_)}
        return self

    def with_line(self, amount, quantity, item_code, tax_code, line_number=None):
        r"""
        Add a line to the transaction.

        :param  float   amount:    Value of the item.
        :param  float   quantity:  Quantity of the item.
        :param  string  item_code: Code of the item.
        :param  string  tax_code:  Tax Code of the item. If left blank, \
        the default item (P0000000) is assumed.
        :param  [int]  line_number: Value of the line number.
        :return:  TransactionBuilder
        """
        if line_number is not None:
            self.line_num = line_number;
        
        temp = {
            'number': str(self.line_num),
            'amount': amount,
            'quantity': quantity,
            'itemCode': str(item_code),
            'taxCode': str(tax_code)
        }
        self.create_model['lines'].append(temp)
        self.line_num += 1
        return self

    def with_exempt_line(self, amount, item_code, exemption_code):
        """
        Add a line with an exemption to this transaction.

        :param   float   amount:         The amount of this line item
        :param   string  item_code:      The code for the item
        :param   string  exemption_code:  The exemption code for this line item
        :return:  TransactionBuilder
        """

        temp = {
            'number': str(self.line_num),
            'quantity': 1,
            'amount': amount,
            'exemptionCode': str(exemption_code),
            'itemCode': str(item_code)
        }
        self.create_model['lines'].append(temp)
        self.line_num += 1
        return self

    def with_diagnostics(self):
        """
        Enable diagnostic information.

        - Sets the debugLevel to 'Diagnostic'
        :return: TransactionBuilder
        """
        self.create_model['debugLevel'] = 'Diagnostic'
        return self

    def with_discount_amount(self, discount):
        """
        Set a specific discount amount.

        :param  float  discount: Amount of the discount
        :return: TransactionBuilder
        """
        self.create_model['discount'] = discount
        return self

    def with_item_discount(self, discounted):
        """
        Set if discount is applicable for the current line.

        :param  boolean  discounted: Set true or false for discounted
        :return: TransactionBuilder
        """
        temp = self.get_most_recent_line('WithItemDiscount')
        temp['discounted'] = discounted
        return self

    def with_parameter(self, name, value):
        """
        Add a parameter at the document level.

        :param  string  name: Name of the parameter
        :param  string  value: Value to be assigned to the parameter
        :return: TransactionBuilder
        """
        self.create_model.setdefault('parameters', {})
        self.create_model['parameters'][name] = value
        return self

    def with_line_parameter(self, name, value):
        """
        Add a parameter to the current line.

        :param  string  name: Name of the parameter
        :param  string  value: Value to be assigned to the parameter
        :return: TransactionBuilder
        """
        temp = self.get_most_recent_line('WithLineParameter')
        temp.setdefault('parameters', {})
        temp['parameters'][name] = value
        return self

    def get_most_recent_line(self, member_name=None):
        """
        Check to see if the current model has a line.

        :return: TransactionBuilder
        """
        line = self.create_model['lines']
        if not len(line):  # if length is zero
            raise Exception('No lines have been added. The {} method applies to the most recent line. To use this function, first add a line.'.format(member_name))
        return line[-1]

    def create(self, include=None):
        """
        Create this transaction.

        :return: TransactionModel
        """
        return self.client.create_transaction(self.create_model, include)

    def with_line_tax_override(self, type_, reason, tax_amount, tax_date):
        r"""
        Add a line-level Tax Override to the current line.

        A TaxDate override requires a valid DateTime object to be passed.

        :param  string  type:        Type of the Tax Override \
        (See TaxOverrideType::* for a list of allowable values)
        :param  string  reason:      Reason of the Tax Override.
        :param  float   tax_amount:  Amount of tax to apply. \
        Required for a TaxAmount Override.
        :param  date    tax_date:    Date of a Tax Override. \
        Required for a TaxDate Override.

        :return:  TransactionBuilder
        """
        line = self.get_most_recent_line('WithLineTaxOverride')
        line['taxOverride'] = {
            'type': str(type_),
            'reason': str(reason),
            'taxAmount': float(tax_amount),
            'taxDate': tax_date
        }
        return self

    def with_tax_override(self, type_, reason, tax_amount, tax_date):
        r"""
        Add a document-level Tax Override to the transaction.

        - A TaxDate override requires a valid DateTime object to be passed

        :param  string  type_:       Type of the Tax Override \
        (See TaxOverrideType::* for a list of allowable values)
        :param  string  reason:      Reason of the Tax Override.
        :param  float   tax_amount:  Amount of tax to apply. Required for \
        a TaxAmount Override.
        :param  date    tax_date:    Date of a Tax Override. Required for \
        a TaxDate Override.
        :return:  TransactionBuilder
        """
        self.create_model['taxOverride'] = {
            'type': str(type_),
            'reason': str(reason),
            'taxAmount': tax_amount,
            'taxDate': tax_date
        }
        return self

    def with_separate_address_line(self, amount, type_, address):
        r"""
        Add a line to this transaction.

        :param  float  amount:  Value of the line
        :param  string  type_:  Address Type  \
        (See AddressType::* for a list of allowable values)
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
        r""".

        Create a transaction adjustment request that can be used with the \
        AdjustTransaction() API call.

        :return: AdjustTransactionModel
        """
        return {
            'newTransaction': self.create_model,
            'adjustmentDescription': desc,
            'adjustmentReason': reason
        }
