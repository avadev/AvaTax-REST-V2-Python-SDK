"""Test module for Create Transaction method."""
import pytest
from requests import Response


def test_201_response_when_creating_transaction(auth_client, tax_document):
    """Test recieving 200 status code when valid data passed in."""
    r = auth_client.create_transaction(tax_document, None)
    assert r.status_code == 201


def test_response_is_proper_response_object(auth_client, tax_document):
    """Test recieving 200 status code when valid data passed in."""
    r = auth_client.create_transaction(tax_document, None)
    assert isinstance(r, Response)


def test_transaction_is_saved_when_commit_is_false(auth_client, tax_document):
    """Test that a transaction is saved when commit is false."""
    tax_document['commit'] = False
    r = auth_client.create_transaction(tax_document, None)
    assert '"status":"Saved"' in r.text


def test_transaction_is_commited_when_commit_is_true(
    auth_client, tax_document
):
    """Test that a transaction is commited when commit is true."""
    tax_document['commit'] = True
    r = auth_client.create_transaction(tax_document, None)
    assert '"status":"Committed"' in r.text


def test_include_param_is_summary_only(auth_client, tax_document):
    """Test param is 'summary only' return corresponding response format."""
    include = {'$include': 'SummaryOnly'}
    r = auth_client.create_transaction(tax_document, include)
    assert 'addresses' not in r.text


def test_include_param_is_addresses(auth_client, tax_document):
    """Test param is 'addresses' return corresponding response format."""
    include = {'$include': 'Addresses'}
    r = auth_client.create_transaction(tax_document, include)
    assert 'addresses' in r.text
