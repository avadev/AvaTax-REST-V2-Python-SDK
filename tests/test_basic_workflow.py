"""
Ensure all methods needed for new user are functional, including going through
the Transaction State Diagram to verify all methods needed for the lifecycle of 
a single transaction works properly.
"""
import pytest


@pytest.mark.incremental  # allow "test-step" : only continue to next test if previous ones all pass
class TestBasicWorkFlow(object):
	def test_connection(self, auth_client):
		"""Test internet connection of the testing env."""
		assert auth_client.ping().status_code == 200

	def test_ping(self, auth_client):
		"""Test credential is valid."""
		assert '"authenticated":true' in auth_client.ping().text

	def test_check_default_company_exist(self, auth_client):
		"""Test if the user has default company set up already, create one otherwise."""
		response = auth_client.query_companies()
		assert response.status_code == 200
		if '"companyCode":"DEFAULT"' not in response.text:
			response = auth_client.company_initialize(init_comp_model)
			assert response.status_code == 201
			assert response.json()['isActive'] == True

	def test_create_transaction(self, auth_client, tax_document):
		"""Create a transaction(save it only) using the company created(DEFAULT)."""
		tax_document['commit'] = False
		response = auth_client.create_transaction(tax_document, None)
		assert response.json()['status'] == 'Saved'
		auth_client.trans_code = response.json()['code']

	def test_verfiy_transaction(self, auth_client):
		"""Verify the transaction that has been created."""
		response = auth_client.verify_transaction('DEFAULT', auth_client.trans_code, {})
		assert response.json()['status'] == 'Posted'




