"""Test module for Commit Transaction method."""
import pytest


def test_commit_transaction_with_invalid_company_code_type(auth_client):
    """Test if an error is raised with invalid input type."""
    trans_code = '94affa7f-b691-41ad-9048-301cdceaffc8'
    with pytest.raises(ValueError):
        auth_client.commit_transaction(trans_code={'code': trans_code})


def test_commit_transaction_with_invaild_trans_code_type(auth_client):
    """Test if an error is raised with lack of required variable."""
    comp_code = 'DEFAULT'
    with pytest.raises(ValueError):
        auth_client.commit_transaction(comp_code={'code': comp_code})


def test_commit_transaction_commit_saved_trans(auth_client, five_transactions):
    """Test if we can commit non-commited/saved trans."""
    for t_code in five_transactions:
        r = auth_client.commit_transaction('DEFAULT', t_code)
        assert r.json()['status'] == 'Committed'


def test_commit_transaction_wont_commit_if_commit_param_false(auth_client, five_transactions):
    """Test if the transaction will not commited if commit parameter is false."""
    for t_code in five_transactions:
        r = auth_client.commit_transaction('DEFAULT', t_code, False)
        assert r.json()['status'] == 'Saved'


