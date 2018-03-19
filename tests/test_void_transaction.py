"""Test void transaction method."""


def test_imports(single_transaction, auth_client):
	"""Test import works without errors."""
	trans_code = single_transaction
	assert trans_code is not None


def test_void_changes_transaction_status_to_with_model(single_transaction, auth_client):
	"""Test that running void_transaction voids it."""
	result = auth_client.void_transaction('DEFAULT', single_transaction, {'code':'DocVoided'}).json()
	assert result['status'] == "Cancelled"


def test_void_transaction_with_param(single_transaction_purchase_invoice, auth_client):
	"""Test if we can void a purchase invoice transaction by passing type into param."""
	include = {'documentType': 'PurchaseInvoice'}
	result = auth_client.void_transaction('DEFAULT', single_transaction_purchase_invoice, {'code':'DocVoided'}, include).json()
	assert result['status'] == "Cancelled"

