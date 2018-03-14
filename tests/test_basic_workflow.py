"""
Ensure all methods needed for new user are functional, including going through
the Transaction State Diagram to verify all methods needed for the lifecycle of 
a single transaction works properly.
"""
from faker import Faker
import pytest

client_info = {
	'company_name': None,

}


@pytest.mark.incremental  # allow "test-step" : only continue to next test if previous ones all pass
class TestBasicWorkFlow(object):
	def test_connection(self, auth_client):
		"""Test internet connection of the testing env."""
		assert auth_client.ping().status_code == 200

	def test_ping(self, auth_client):
		"""Test credential is valid."""
		assert '"authenticated":true' in auth_client.ping().text

	def test_company_initialization(self, auth_client, init_comp_model):
		"""Test a basic company can be initalized."""
		fake = Faker()
		comp_name = fake.first_name().upper()  # create new company each time test is run to prevent conflict
		model = init_comp_model
		model['companyCode'] = comp_name
		response = auth_client.company_initialize(model)
		assert response.status_code == 201
		if response.status_code == 201:
			assert response.json()['isActive'] == True
			client_info['company_name'] = comp_name

	def test_create_transaction(auth_client):
		"""Create a transaction using the company just created"""
		pass


