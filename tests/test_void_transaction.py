"""Test void transaction method."""
import pytest


def test_imports(single_transaction, auth_client):
    """Test import works without errors."""
    trans_code = single_transaction
    assert trans_code is not None


def test_void_changes_transaction_status_to(single_transaction, auth_client):
    """Test that running void_transaction voids it."""
    result = auth_client.void_transaction('DEFAULT', single_transaction,
                                          {'code': 'DocVoided'}).json()
    assert result['status'] == "Cancelled"


def test_void_without_model_info_raises_error(single_transaction, auth_client):
    """Test error is raised when called without all params."""
    with pytest.raises(ValueError):
        auth_client.void_transaction("DEFAULT", single_transaction)


def test_void_without_company_code_raises_errror(single_transaction,
                                                 auth_client):
    """Test error is raised when called without all params."""
    with pytest.raises(ValueError):
        auth_client.void_transaction(single_transaction, {'code': 'DocVoided'})


def test_void_without_transaction_num_raises_error(single_transaction,
                                                   auth_client):
    """Test error is raised when called without all params."""
    with pytest.raises(ValueError):
        auth_client.void_transaction('DEFAULT', {'code': 'DocVoided'})
