"""Test module for Commit Transaction method."""


def test_commit_transaction_commit_saved_trans(auth_client, single_transaction):
    """Test if we can commit non-commited/saved trans."""
    r = auth_client.commit_transaction('DEFAULT', single_transaction, {'commit': True})
    assert r.json()['status'] == 'Committed'


def test_commit_transaction_wont_commit_if_commit_param_false(auth_client, single_transaction):
    """Test if the transaction will not commited if commit parameter is false."""
    r = auth_client.commit_transaction('DEFAULT', single_transaction, {'commit': False})
    assert r.json()['status'] == 'Saved'

