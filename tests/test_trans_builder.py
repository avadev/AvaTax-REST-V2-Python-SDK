"""Test Transactin Builder class."""
from transaction_builder import TransactionBuilder


def test_initialize_builder_object(auth_client):
    """Test if a new transaction can be initialize."""
    new_trans = TransactionBuilder(auth_client, 'DEFAULT', 'SalesInvoice', 'ABC123')
    assert isinstance(new_trans, TransactionBuilder)


def test_with_commit_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    trans = mt_trans.with_commit()
    assert trans.create_model['commit'] is True


def test_with_transaction_code_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    trans = mt_trans.with_transaction_code('1234567')
    assert trans.create_model['code'] == '1234567'


def test_with_type_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    trans = mt_trans.with_type('SalesInvoice')
    assert trans.create_model['type'] == 'SalesInvoice'


def test_with_address_method(mt_trans, valid_address):
    """Test method functionality of the Transaction Builder."""
    trans = mt_trans.with_address('SingleLocation', valid_address)
    assert trans.create_model['addresses']['SingleLocation'] == valid_address


def test_with_line_address_method(mt_trans, valid_address):
    """Test method functionality of the Transaction Builder."""
    mt_trans.with_line_address('SingleLocation', valid_address)
    last_line = mt_trans.get_most_recent_line()
    assert last_line['addresses']['SingleLocation'] == valid_address


def test_with_latlong_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    lat_long = {'latitude': 47.6187, 'longitude': -122.3524}
    trans = mt_trans.with_latlong('SingleLocation', 47.6187, -122.3524)
    assert trans.create_model['addresses']['SingleLocation'] == lat_long


def test_with_line_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    temp = {
        'amount': 20,
        'number': '1',
        'quantity': 100,
        'itemCode': 'ITEM2001',
        'taxCode': '1234567'
    }
    trans = mt_trans.with_line(20, 100, 'ITEM2001', 1234567)
    assert trans.create_model['lines'][-1] == temp


def test_with_exempt_line_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    temp = {
        'amount': 20,
        'number': '1',
        'quantity': 1,
        'itemCode': 'ITEM2001',
        'exemptionCode': '1234567'
    }
    trans = mt_trans.with_exempt_line(20, 'ITEM2001', 1234567)
    assert trans.create_model['lines'][-1] == temp


def test_with_diagnostics_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    trans = mt_trans.with_diagnostics()
    assert trans.create_model['debugLevel'] == 'Diagnostic'


def test_with_discount_amount_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    trans = mt_trans.with_discount_amount(200)
    assert trans.create_model['discount'] == 200


def test_with_parameter_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    trans = mt_trans.with_parameter('param', 'param_val')
    assert trans.create_model['parameters']['param'] == 'param_val'


def test_with_line_parameter_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    trans = mt_trans.with_parameter('param', 'param_val')
    assert trans.create_model['parameters']['param'] == 'param_val'


def test_get_most_recent_line_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    line = mt_trans.get_most_recent_line('TestName')
    assert line is mt_trans.create_model['lines'][-1]


def test_with_line_tax_overrride_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    model = {
        "type": "TaxAmount",
        "taxAmount": 6.25,
        "taxDate": "2017-12-14",
        "reason": "Precalculated Tax"
    }
    trans = mt_trans.with_tax_override('TaxAmount', 'Precalculated Tax', 6.25, '2017-12-14')
    assert trans.create_model['taxOverride'] == model


def test_with_separate_address_method(mt_trans, valid_address):
    """Test method functionality of the Transaction Builder."""
    model = {
        'number': 1,
        'quantity': 1,
        'amount': 200,
        'addresses': {
            'SingleLocation': valid_address
        }
    }
    trans = mt_trans.with_separate_address_line(200, 'SingleLocation', valid_address)
    assert trans.create_model['lines'][-1] == model


def test_create_adjustment_request_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    model = {
        'newTransaction': mt_trans.create_model,
        'adjustmentDescription': 'EOY adjustment',
        'adjustmentReason': 'internal transfer'
    }
    re = mt_trans.create_adjustment_request('EOY adjustment', 'internal transfer')
    assert re == model







