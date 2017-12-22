"""Test resolve address method."""


def test_address_fixture_import(valid_address):
    """Test address fixture imports without errors."""
    assert isinstance(valid_address, dict)


def test_resolve_address_response_code_200(auth_client, valid_address):
    """Testing client without authorization."""
    assert auth_client.resolve_address(valid_address).status_code == 200


def test_resolved_address_response_has_coordinates(auth_client, valid_address):
    """Test the response has latitude for resolved address."""
    response_json = auth_client.resolve_address(valid_address).json()
    assert isinstance(response_json['coordinates']['latitude'], float)


def test_resolve_address_response_code_400(auth_client):
    """Test resolve address with incomplete data."""
    bad_address = {'line1': 'Incomplete Address'}
    assert auth_client.resolve_address(bad_address).status_code == 400


def test_incomplete_resolve_address_response_code_401(unauth_client):
    """Test resolve address with incomplete data and unauthorized user."""
    bad_address = {'line1': 'Incomplete Address'}
    assert unauth_client.resolve_address(bad_address).status_code == 401


def test_unauthorized_resolve_address_response_code_401(unauth_client, valid_address):
    """Test resolve address with correct data and unauthorized user."""
    assert unauth_client.resolve_address(valid_address).status_code == 401


def test_resolve_address_error_message(auth_client):
    """Test that incomplete address returns error message."""
    bad_address = {'line1': 'Incomplete Address'}
    assert auth_client.resolve_address(bad_address).json()['error']
