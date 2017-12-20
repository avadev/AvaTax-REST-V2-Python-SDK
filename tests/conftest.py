"""Conftest is a file recognize by pytest module, allowing us to share fixture across multiple tests."""
from client import AvataxClient
import os
import pytest


@pytest.fixture(scope='function')
def unauth_client():
    """Create an instance of SanboxClient without authentification."""
    return AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')


@pytest.fixture(scope='session')
def auth_client_loggedin_with_username():
    """Create an instance of SanboxClient with authentification using username/password pair."""
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    client.add_credentials(os.environ.get('USERNAME', ''), os.environ.get('PASSWORD', ''))
    return client


@pytest.fixture(scope='session')
def auth_client():
    """Create an instance of SanboxClient with authentification using username/password pair."""
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    client.add_credentials(os.environ.get('USERNAME', ''), os.environ.get('PASSWORD', ''))
    return client


@pytest.fixture(scope='session')
def auth_client_loggedin_with_id():
    """Create an instance of SanboxClient with authentification using userID/licenseKey pair."""
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    client.add_credentials(os.environ.get('ACCOUNT_ID', ''), os.environ.get('LICENSE_KEY', ''))
    return client


@pytest.fixture
def good_address():
    """Properly filled address fixture for testing resolve address."""
    address = {
        'line1': '410 Terry Ave. North',
        'city': 'Seattle',
        'region': 'WA',
        'postal_code': '98109',
    }
    return address


@pytest.fixture(scope='function')
def single_transaction():
    """Create an instance of AvataxClient with authentication and created transaction."""
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    client.add_credentials(os.environ.get('USERNAME', ''), os.environ.get('PASSWORD', ''))
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
    r = client.create_transaction('DEFAULT', tax_document)
    trans_code = r.json()['code']
    return trans_code


@pytest.fixture(scope='function')
def five_transactions():
    """Create an instance of AvataxClient with authentication and created transaction."""
    trans_codes = []
    client = AvataxClient('test app', 'ver 0.0', 'test machine', 'sandbox')
    client.add_credentials(os.environ.get('USERNAME', ''), os.environ.get('PASSWORD', ''))
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
        r = client.create_transaction(None, tax_document)
        trans_codes.append(r.json()['code'])
    return trans_codes


@pytest.fixture(scope='function')
def tax_document():
    """Create a tax document dictionary."""
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

