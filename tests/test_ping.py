"""Test the ping method."""


def test_ping_makes_connection(unauth_client):
    """Testing client without authorization."""
    assert unauth_client.ping().status_code == 200


def test_ping_auth_is_false_connection(unauth_client):
    """Testing client without authorization."""
    assert '"authenticated":false' in unauth_client.ping().text


def test_ping_auth_is_true_connection(auth_client_loggedin_with_username):
    """Testing client with authorization from username and password."""
    assert '"authenticated":true' in auth_client_loggedin_with_username.ping().text


def test_ping_auth_is_true_using_client_id(auth_client_loggedin_with_id):
    """Testing client with authorization from account ID and license key."""
    assert '"authenticated":true' in auth_client_loggedin_with_id.ping().text


def test_ping_auth_with_invalid_user_and_pass(unauth_client):
    """Testing client without proper username and password."""
    unauth_client.add_credentials({'username': '1234', 'password': '4321'})
    assert '"authenticated":false' in unauth_client.ping().text


def test_ping_auth_with_invalid_account_id(unauth_client):
    """Testing client without proper account id and license key."""
    unauth_client.add_credentials({'account_id': '1234', 'license_key': '4321'})
    assert '"authenticated":false' in unauth_client.ping().text
