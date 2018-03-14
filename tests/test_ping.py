"""Test the ping method."""


def test_ping_makes_connection(unauth_client):
    """Testing client without authorization."""
    assert unauth_client.ping().status_code == 200


def test_ping_auth_is_false_connection(unauth_client):
    """Testing client without authorization."""
    assert '"authenticated":false' in unauth_client.ping().text


def test_ping_auth_is_true_using_client_id(auth_client):
    """Testing client with authorization from username and password."""
    assert '"authenticated":true' in auth_client.ping().text


def test_ping_auth_with_invalid_user_and_pass(unauth_client):
    """Testing client without proper username and password."""
    unauth_client.add_credentials('1234', '4321')
    assert '"authenticated":false' in unauth_client.ping().text


def test_ping_auth_with_invalid_account_id(unauth_client):
    """Testing client without proper account id and license key."""
    unauth_client.add_credentials('1234', '4321')
    assert '"authenticated":false' in unauth_client.ping().text
