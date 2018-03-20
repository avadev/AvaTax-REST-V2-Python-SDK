"""Conftest is a file recognize by pytest module, allowing us to share fixture across multiple tests."""
from client import AvataxClient
from transaction_builder import TransactionBuilder
import os
import pytest


@pytest.fixture(scope='function')
def unauth_client():
    """Create an instance of SanboxClient without authentification."""
    return AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')


@pytest.fixture(scope='session')
def auth_client():
    """Create an instance of SanboxClient with authentification using username/password pair."""

    try:
        login_key, login_val = cred_determine()
    except ValueError:
        raise ValueError('No testing credentials are in the environment.')
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    client.add_credentials(login_key, login_val)
    return client


@pytest.fixture(scope='function')
def mt_trans():
    """Create an instance of Transaction Builder object."""
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    login_key, login_val = cred_determine()
    client.add_credentials(login_key, login_val)
    trans = TransactionBuilder(client, 'DEFAULT', 'SalesInvoice', 'ABC123')
    return trans


@pytest.fixture
def valid_address():
    """Properly filled address fixture for testing resolve address."""
    address = {
        'line1': '410 Terry Ave. North',
        'city': 'Seattle',
        'region': 'WA',
        'postalCode': '98109',
    }
    return address


@pytest.fixture
def ship_from_address():
    """Different address for testing purpose."""
    address = {
        'line1': '123 Main Street',
        'city': 'Irvine',
        'region': 'CA',
        'postalCode': '92615'
    }
    return address


@pytest.fixture(scope='function')
def single_transaction():
    """Create an instance of AvataxClient with authentication and created transaction."""
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    login_key, login_val = cred_determine()
    client.add_credentials(login_key, login_val)
    tax_document = default_trans_model()
    r = client.create_transaction(tax_document, 'DEFAULT')
    trans_code = r.json()['code']
    return trans_code


@pytest.fixture(scope='function')
def single_transaction_purchase_invoice():
    """Create an instance of AvataxClient with authentication and created transaction(purchase invoice)."""
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    login_key, login_val = cred_determine()
    client.add_credentials(login_key, login_val)
    tax_document = default_trans_model()
    tax_document['type'] = 'PurchaseInvoice'
    r = client.create_transaction(tax_document, 'DEFAULT')
    trans_code = r.json()['code']
    return trans_code


@pytest.fixture(scope='function')
def five_transactions():
    """Create an instance of AvataxClient with authentication and created transaction."""
    trans_codes = []
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    login_key, login_val = cred_determine()
    client.add_credentials(login_key, login_val)
    addresses = [
        ('Seattle', '600 5th Ave', '98104', 'WA'),
        ('Poulsbo', '200 Moe St Ne', '98370', 'WA'),
        ('Los Angeles', '1945 S Hill St', '90007', 'CA'),
        ('Chicago', '50 W Washington St', '60602', 'IL'),
        ('Irvine', '123 Main Street', '92615', 'CA')
    ]
    for city, line1, postal, region in addresses:
        tax_document = {
            'addresses': {'SingleLocation': {'city': city,
                                             'country': 'US',
                                             'line1': line1,
                                             'postalCode': postal,
                                             'region': region}},
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
        r = client.create_transaction(tax_document, None)
        trans_codes.append(r.json()['code'])
    return trans_codes


@pytest.fixture(scope='function')
def tax_document():
    """Create a tax document dictionary."""
    return default_trans_model()

@pytest.fixture(scope='function')
def init_comp_model():
    """Return the following initialize company model for company DEFAULT."""
    return {
        "name": "Bobs Artisan Pottery",
        "companyCode": 'DEFAULT',
        "taxpayerIdNumber": "12-3456789",
        "line1": "2000 Main Street",
        "city": "Irvine",
        "region": "CA",
        "postalCode": "92614",
        "country": "US",
        "firstName": "Bob",
        "lastName": "Example",
        "title": "Owner",
        "email": "bob@example.org",
        "phoneNumber": "714 555-2121",
        "mobileNumber": "714 555-1212"}

def cred_determine():
    """Return the appropriate pair of cred."""
    if os.environ.get('USERNAME') and os.environ.get('PASSWORD'):
        return (os.environ.get('USERNAME'), os.environ.get('PASSWORD'))
    elif os.environ.get('SANDBOX_CLIENTID') and os.environ.get('SANDBOX_LICENSEKEY'):
        return (os.environ.get('SANDBOX_CLIENTID'), os.environ.get('SANDBOX_LICENSEKEY'))
    elif os.environ.get('SANDBOX_USERNAME') and os.environ.get('SANDBOX_PASSWORD'):
        return (os.environ.get('SANDBOX_USERNAME'), os.environ.get('SANDBOX_PASSWORD'))
    else:
        raise ValueError()

def default_trans_model():
    """Return the default transaction model."""
    return {
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

def pytest_runtest_makereport(item, call):
    """For incremental testing fixture called mark.increment."""
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    """For incremental testing fixture called mark.increment."""
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)


