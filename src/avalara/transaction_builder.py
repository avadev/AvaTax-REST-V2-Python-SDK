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

TransactionBuilder helps you construct a new transaction using a literate
interface
"""
from datetime import datetime
import transaction_builder_methods


class TransactionBuilder(transaction_builder_methods.Mixin):
    """Transaction builder class."""

    def __init__(self, client, comp_code, type_, cust_code):
        r""".

        The TransactionBuilder helps you construct a new transaction using a \
        literate interface.

        :param AvaTaxClient  client:     The AvaTaxClient object to use to \
                                            create this transaction
        :param string        comp_code:  The code of the company for this transaction
        :param DocumentType  type:       The type of transaction to create \
                        (See DocumentType::* for a list of allowable values)
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
            'date': '{}'.format(datetime.utcnow()),
            'lines': []
        }
