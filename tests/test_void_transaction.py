"""Test void transaction method."""
import pytest


def test_imports(single_transaction, auth_client):
    """Test import works without errors."""
    trans_code = single_transaction
    assert trans_code is not None


def test_void_changes_transaction_status_to(single_transaction, auth_client):
    """Test that running void_transaction voids it with default void model."""
    result = auth_client.void_transaction('DEFAULT', single_transaction).json()
    assert result['status'] == "Cancelled"


def test_void_changes_transaction_status_to_with_model(single_transaction, auth_client):
    """Test that running void_transaction voids it."""
    result = auth_client.void_transaction('DEFAULT', single_transaction, 'DocVoided').json()
    assert result['status'] == "Cancelled"


def test_void_with_invalid_type_model_info_raises_error(single_transaction, auth_client):
    """Test error is raised when called without proper params."""
    with pytest.raises(ValueError):
        auth_client.void_transaction(code_model={})


def test_void_with_invalid_type_company_code_raises_errror(single_transaction,
                                                           auth_client):
    """Test error is raised when called without proper params."""
    with pytest.raises(ValueError):
        auth_client.void_transaction(comp_code=983922)


def test_void_with_invalid_type_transaction_num_raises_error(single_transaction,
                                                             auth_client):
    """Test error is raised when called without proper params."""
    with pytest.raises(ValueError):
        auth_client.void_transaction(trans_code=332422234)
