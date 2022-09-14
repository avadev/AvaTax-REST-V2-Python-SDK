"""Test Transactin Builder class."""
from src.avalara.transaction_builder import TransactionBuilder


def test_initialize_builder_object(auth_client):
    """Test if a new transaction can be initialize."""
    new_trans = TransactionBuilder(
        auth_client, 'DEFAULT', 'SalesInvoice', 'ABC123'
    )
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
    mt_trans.with_line(20, 100, 'ITEM2001', 1234567)
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
        'taxCode': '1234567',
        'taxIncluded': False,
        'exemptionCode': '',
    }
    trans = mt_trans.with_line(20, 100, 'ITEM2001', 1234567)
    assert trans.create_model['lines'][-1] == temp


def test_with_line_method_with_string_line_number(mt_trans):
    """Test method functionality of the Transaction Builder."""
    expected_resp_str_line_number = {
        'amount': 20,
        'number': 'shipping-1',
        'quantity': 100,
        'itemCode': 'ITEM2001',
        'taxCode': '1234567',
        'taxIncluded': False,
        'exemptionCode': '',
    }
    expected_resp_int_line_number = {
        'amount': 100,
        'number': '5',
        'quantity': 1,
        'itemCode': 'ITEM2005',
        'taxCode': '5555555',
        'taxIncluded': False,
        'exemptionCode': '',
    }
    trans = mt_trans.with_line(
        amount=20,
        quantity=100,
        item_code='ITEM2001',
        tax_code=1234567,
        tax_included=False,
        line_number='shipping-1',
        exemption_code="",
    ).with_line(
        amount=100,
        quantity=1,
        item_code='ITEM2005',
        tax_code=5555555,
        tax_included=False,
        line_number=5,
        exemption_code="",
    )
    assert trans.create_model['lines'][0] == expected_resp_str_line_number
    assert trans.create_model['lines'][1] == expected_resp_int_line_number


def test_with_line_method_with_optional_parameters(mt_trans):
    """Test method functionality of the Transaction Builder."""
    expected_resp_int_line_number = {
        'amount': 100,
        'number': '5',
        'quantity': 1,
        'itemCode': 'ITEM2005',
        'taxCode': '',
        'taxIncluded': True,
        'exemptionCode': 'EXEMPT_CUST_002',
    }
    trans = mt_trans.with_line(
        amount=100,
        quantity=1,
        item_code='ITEM2005',
        tax_included=True,
        line_number=5,
        exemption_code="EXEMPT_CUST_002",
    )
    assert trans.create_model['lines'][0] == expected_resp_int_line_number


def test_with_line_method_line_number_not_null(mt_trans):
    """Test method functionality of the Transaction Builder."""
    temp = {
        'amount': 20,
        'number': '2',
        'quantity': 100,
        'itemCode': 'ITEM2001',
        'taxCode': '1234567',
        'taxIncluded': False,
        'exemptionCode': '',
    }
    trans = mt_trans.with_line(20, 100, 'ITEM2001', 1234567, 2)
    assert trans.create_model['lines'][-1] == temp


def test_with_exempt_line_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    temp = {
        'amount': 20,
        'number': '1',
        'quantity': 1,
        'itemCode': 'ITEM2001',
        'exemptionCode': '1234567',
        'taxIncluded': False,
        'taxCode': '',
    }
    trans = mt_trans.with_exempt_line(20, 'ITEM2001', 1234567)
    assert trans.create_model['lines'][-1] == temp


def test_with_exempt_line_method_quantity(mt_trans):
    """Test method functionality of the Transaction Builder."""
    temp = {
        'amount': 100,
        'number': '1',
        'quantity': 5,
        'itemCode': 'ITEM2001',
        'exemptionCode': 'EXEMPT_THIS_CUSTOMER',
        'taxIncluded': False,
        'taxCode': '',
    }
    trans = mt_trans.with_exempt_line(
        quantity=5,
        amount=100,
        item_code='ITEM2001',
        exemption_code='EXEMPT_THIS_CUSTOMER',
    )
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
    mt_trans.with_line(20, 100, 'ITEM2001', 1234567)
    line = mt_trans.get_most_recent_line('TestName')
    assert line is mt_trans.create_model['lines'][-1]


def test_with_line_tax_overrride_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    model = {
        "type": "TaxAmount",
        "taxAmount": 6.25,
        "taxDate": "2017-12-14",
        "reason": "Precalculated Tax",
    }
    trans = mt_trans.with_tax_override(
        'TaxAmount', 'Precalculated Tax', 6.25, '2017-12-14'
    )
    assert trans.create_model['taxOverride'] == model


def test_with_separate_address_method(mt_trans, valid_address):
    """Test method functionality of the Transaction Builder."""
    model = {
        'number': 1,
        'quantity': 1,
        'amount': 200,
        'addresses': {'SingleLocation': valid_address},
    }
    trans = mt_trans.with_separate_address_line(
        200, 'SingleLocation', valid_address
    )
    assert trans.create_model['lines'][-1] == model


def test_create_adjustment_request_method(mt_trans):
    """Test method functionality of the Transaction Builder."""
    model = {
        'newTransaction': mt_trans.create_model,
        'adjustmentDescription': 'EOY adjustment',
        'adjustmentReason': 'internal transfer',
    }
    re = mt_trans.create_adjustment_request(
        'EOY adjustment', 'internal transfer'
    )
    assert re == model


def test_create_trans_without_commit(mt_trans, valid_address):
    """Test creating a transaction with transaction builder."""
    trans = (
        mt_trans.with_address('SingleLocation', valid_address)
        .with_line(20, 100, 'ITEM2001', 1234567)
        .create()
    )
    assert '"status":"Saved"' in trans.text


def test_create_trans_with_commit(mt_trans, valid_address):
    """Test creating a transaction with transaction builder."""
    trans = (
        mt_trans.with_address('SingleLocation', valid_address)
        .with_line(20, 100, 'ITEM2001', 1234567)
        .with_commit()
        .create()
    )
    assert '"status":"Committed"' in trans.text


def test_create_trans_with_two_lines(
    mt_trans, valid_address, ship_from_address
):
    """Test creating transaction with 2 lines."""
    trans = (
        mt_trans.with_address('ShipFrom', ship_from_address)
        .with_address('ShipTo', valid_address)
        .with_line(100.0, 1, None, 'P0000000')
        .create()
    )
    assert trans.status_code == 201


def test_create_trans_with_exempt_line(mt_trans, valid_address):
    """Test creating a transaction with transaction builder."""
    trans = (
        mt_trans.with_address('SingleLocation', valid_address)
        .with_line(100.0, 1, None, 'P0000000')
        .with_exempt_line(50.0, None, 'NT')
        .create()
    )
    assert trans.status_code == 201


def test_create_trans_with_line_address(
    mt_trans, valid_address, ship_from_address
):
    """Test creating a transaction with transaction builder."""
    trans = (
        mt_trans.with_line(100.0, 1, None, 'P0000000')
        .with_line_address('ShipFrom', ship_from_address)
        .with_line_address('ShipTo', valid_address)
        .create()
    )
    assert trans.status_code == 201
