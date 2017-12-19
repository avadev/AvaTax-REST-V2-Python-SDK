"""Test module for Create Transaction method."""
import pytest
from requests import Response


def test_no_transaction_infor(auth_client_loggedin_with_username):
    """Test that an error is returned from the server."""
    with pytest.raises(ValueError):
        auth_client_loggedin_with_username.create_transaction()


def test_201_response_when_creating_transaction(auth_client_loggedin_with_username, tax_document):
    """Test recieving 200 status code when valid data passed in."""
    user = auth_client_loggedin_with_username
    r = user.create_transaction(None, tax_document)
    assert r.status_code == 201


def test_response_is_proper_response_object(auth_client_loggedin_with_username, tax_document):
    """Test recieving 200 status code when valid data passed in."""
    user = auth_client_loggedin_with_username
    r = user.create_transaction(None, tax_document)
    assert isinstance(r, Response)


def test_transaction_is_saved_when_commit_is_false(auth_client_loggedin_with_username, tax_document):
    """Test that a transaction is saved when commit is false."""
    user = auth_client_loggedin_with_username
    tax_document['commit'] = False
    r = user.create_transaction(None, tax_document)
    assert '"status":"Saved"' in r.text


def test_transaction_is_commited_when_commit_is_true(auth_client_loggedin_with_username, tax_document):
    """Test that a transaction is commited when commit is true."""
    user = auth_client_loggedin_with_username
    tax_document['commit'] = True
    r = user.create_transaction(None, tax_document)
    assert '"status":"Committed"' in r.text

