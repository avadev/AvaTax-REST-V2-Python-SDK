"""
AvaTax Software Development Kit for Python.

   Copyright 2019 Avalara, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import requests
from ._str_version import str_type


class Mixin:
    """Mixin class contain methods attached to Client class."""

    r"""
    Reset this account's license key
    
    Resets the existing license key for this account to a new key.
      To reset your account, you must specify the ID of the account you wish to reset and confirm the action.
      This API is only available to account administrators for the account in question, and may only be called after
      an account has been activated by reading and accepting Avalara's terms and conditions. To activate your account
      please log onto the AvaTax website or call the `ActivateAccount` API.
      Resetting a license key cannot be undone. Any previous license keys will immediately cease to work when a new key is created.
      When you call this API, all account administrators for this account will receive an email with the newly updated license key.
      The email will specify which user reset the license key and it will contain the new key to use to update your connectors.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] The ID of the account you wish to update.
      :param model [ResetLicenseKeyModel] A request confirming that you wish to reset the license key of this account.
      :return LicenseKeyModel
    """
    def account_reset_license_key(self, id_, model):
        return requests.post('{}/api/v2/accounts/{}/resetlicensekey'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Activate an account by accepting terms and conditions
    
    Activate the account specified by the unique accountId number.
      This activation request can only be called by account administrators. You must indicate
      that you have read and accepted Avalara's terms and conditions to call this API.
      Once you have activated your account, use the `AccountResetLicenseKey` API to generate
      a license key for your account.
      If you have not read or accepted the terms and conditions, this API call will return the
      unchanged account model.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] The ID of the account to activate
      :param model [ActivateAccountModel] The activation request
      :return AccountModel
    """
    def activate_account(self, id_, model):
        return requests.post('{}/api/v2/accounts/{}/activate'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve audit history for an account.
    
    Retrieve audit trace history for an account.
      Your audit trace history contains a record of all API calls made against the AvaTax REST API. You can use this API to investigate
      problems and see exactly what information was sent back and forth between your code and AvaTax.
      When specifying a start and end datetime, please include a valid timezone indicator, such as the "Z" present in the examples for the start and end query parameters.
      You can learn more about valid time zone designators at https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators.
      This API enforces limits to the amount of data retrieved. These limits are subject to change.
      * You may request data from a maximum of a one-hour time period.
      * The amount of data and number of API calls returned by this API are limited and may be adjusted at any time.
      * Old records may be migrated out of immediately available storage. To request older data, please contact your account manager.
      * New records must migrate to available storage before they can be retrieved. You may need to wait a period of time before newly created records can be fetched.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The ID of the account you wish to audit.
      :param start [datetime] The start datetime of audit history you with to retrieve, e.g. "2018-06-08T17:00:00Z". Defaults to the past 15 minutes.
      :param end [datetime] The end datetime of audit history you with to retrieve, e.g. "2018-06-08T17:15:00Z. Defaults to the current time. Maximum of an hour after the start time.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :return FetchResult
    """
    def audit_account(self, id_, include=None):
        return requests.get('{}/api/v2/accounts/{}/audit'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single account
    
    Get the account object identified by this URL.
      You may use the '$include' parameter to fetch additional nested data:
      * Subscriptions
      * Users
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The ID of the account to retrieve
      :param include [string] A comma separated list of special fetch options
      :return AccountModel
    """
    def get_account(self, id_, include=None):
        return requests.get('{}/api/v2/accounts/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Get configuration settings for this account
    
    Retrieve a list of all configuration settings tied to this account.
      Configuration settings provide you with the ability to control features of your account and of your
      tax software. The category names `TaxServiceConfig` and `AddressServiceConfig` are reserved for
      Avalara internal software configuration values; to store your own account-level settings, please
      create a new category name that begins with `X-`, for example, `X-MyCustomCategory`.
      Account settings are permanent settings that cannot be deleted. You can set the value of an
      account setting to null if desired.
      Avalara-based account settings for `TaxServiceConfig` and `AddressServiceConfig` affect your account's
      tax calculation and address resolution, and should only be changed with care.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param id_ [int] 
      :return AccountConfigurationModel
    """
    def get_account_configuration(self, id_):
        return requests.get('{}/api/v2/accounts/{}/configuration'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all accounts
    
    List all account objects that can be seen by the current user.
      This API lists all accounts you are allowed to see. In general, most users will only be able to see their own account.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Subscriptions
      * Users
      For more information about filtering in REST, please see the documentation at http://developer.avalara.com/avatax/filtering-in-rest/ .
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param include [string] A comma separated list of objects to fetch underneath this account. Any object with a URL path underneath this account can be fetched by specifying its name.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* subscriptions, users
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_accounts(self, include=None):
        return requests.get('{}/api/v2/accounts'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Change configuration settings for this account
    
    Update configuration settings tied to this account.
      Configuration settings provide you with the ability to control features of your account and of your
      tax software. The category names `TaxServiceConfig` and `AddressServiceConfig` are reserved for
      Avalara internal software configuration values; to store your own account-level settings, please
      create a new category name that begins with `X-`, for example, `X-MyCustomCategory`.
      Account settings are permanent settings that cannot be deleted. You can set the value of an
      account setting to null if desired.
      Avalara-based account settings for `TaxServiceConfig` and `AddressServiceConfig` affect your account's
      tax calculation and address resolution, and should only be changed with care.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] 
      :param model [AccountConfigurationModel] 
      :return AccountConfigurationModel
    """
    def set_account_configuration(self, id_, model):
        return requests.post('{}/api/v2/accounts/{}/configuration'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve geolocation information for a specified address
    
    Resolve an address against Avalara's address-validation system. If the address can be resolved, this API
      provides the latitude and longitude of the resolved location. The value 'resolutionQuality' can be used
      to identify how closely this address can be located. If the address cannot be clearly located, use the
      'messages' structure to learn more about problems with this address.
      This is the same API as the POST /api/v2/addresses/resolve endpoint.
      Both verbs are supported to provide for flexible implementation.
      Inorder to get any evaluation for an address please provide atleast one of the following fields/pairs:
      1. postal code
      2. line1 + city + region
      3. line1 + postal code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AutoAddress.
    
      :param line1 [string] Line 1
      :param line2 [string] Line 2
      :param line3 [string] Line 3
      :param city [string] City
      :param region [string] State / Province / Region
      :param postalCode [string] Postal Code / Zip Code
      :param country [string] Two character ISO 3166 Country Code (see /api/v2/definitions/countries for a full list)
      :param textCase [TextCase] selectable text case for address validation (See TextCase::* for a list of allowable values)
      :return AddressResolutionModel
    """
    def resolve_address(self, include=None):
        return requests.get('{}/api/v2/addresses/resolve'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve geolocation information for a specified address
    
    Resolve an address against Avalara's address-validation system. If the address can be resolved, this API
      provides the latitude and longitude of the resolved location. The value 'resolutionQuality' can be used
      to identify how closely this address can be located. If the address cannot be clearly located, use the
      'messages' structure to learn more about problems with this address.
      This is the same API as the GET /api/v2/addresses/resolve endpoint.
      Both verbs are supported to provide for flexible implementation.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AutoAddress.
    
      :param model [AddressValidationInfo] The address to resolve
      :return AddressResolutionModel
    """
    def resolve_address_post(self, model):
        return requests.post('{}/api/v2/addresses/resolve'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new AvaFileForm
    
    Create one or more AvaFileForms
      A 'AvaFileForm' represents a form supported by our returns team
      ### Security Policies
      * This API requires the user role Compliance Root User.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param model [AvaFileFormModel] The AvaFileForm you wish to create.
      :return AvaFileFormModel
    """
    def create_ava_file_forms(self, model):
        return requests.post('{}/api/v2/avafileforms'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single AvaFileForm
    
    Marks the existing AvaFileForm object at this URL as deleted.
      ### Security Policies
      * This API requires one of the following user roles: Compliance Root User, ComplianceUser, FirmAdmin.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param id_ [int] The ID of the AvaFileForm you wish to delete.
      :return ErrorDetail
    """
    def delete_ava_file_form(self, id_):
        return requests.delete('{}/api/v2/avafileforms/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single AvaFileForm
    
    Get the AvaFileForm object identified by this URL.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CompanyUser, Compliance Root User, Compliance Temp User, ComplianceAdmin, ComplianceUser, FirmAdmin, FirmUser, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
    
      :param id_ [int] The primary key of this AvaFileForm
      :return AvaFileFormModel
    """
    def get_ava_file_form(self, id_):
        return requests.get('{}/api/v2/avafileforms/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all AvaFileForms
    
    Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CompanyUser, Compliance Root User, Compliance Temp User, ComplianceAdmin, ComplianceUser, FirmAdmin, FirmUser, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* outletTypeId
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_ava_file_forms(self, include=None):
        return requests.get('{}/api/v2/avafileforms'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a AvaFileForm
    
    All data from the existing object will be replaced with data in the object you PUT.
      To set a field's value to null, you may either set its value to null or omit that field from the object you post.
      ### Security Policies
      * This API requires the user role Compliance Root User.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param id_ [int] The ID of the AvaFileForm you wish to update
      :param model [AvaFileFormModel] The AvaFileForm model you wish to update.
      :return AvaFileFormModel
    """
    def update_ava_file_form(self, id_, model):
        return requests.put('{}/api/v2/avafileforms/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new batch
    
    Create one or more new batch objects attached to this company.
      Each batch object may have one or more file objects (currently only one file is supported).
      When a batch is created, it is added to the AvaTax Batch Queue and will be
      processed as quickly as possible in the order it was received. To check the
      status of a batch, fetch the batch and retrieve the results of the batch
      operation.
      Because the batch system processes with a degree of concurrency, and
      because of batch sizes in the queue vary, AvaTax API is unable to accurately
      predict when a batch will complete. If high performance processing is
      required, please use the
      [CreateTransaction API](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Transactions/CreateTransaction/).
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CSPTester, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this batch.
      :param model [BatchModel] The batch you wish to create.
      :return BatchModel
    """
    def create_batches(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/batches'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single batch
    
    Marks the batch identified by this URL as deleted.
      If you attempt to delete a batch that is being processed, you will receive an error message.
      Deleting a batch does not delete any transactions that were created by importing the batch.
      Because the batch system processes with a degree of concurrency, and
      because of batch sizes in the queue vary, AvaTax API is unable to accurately
      predict when a batch will complete. If high performance processing is
      required, please use the
      [CreateTransaction API](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Transactions/CreateTransaction/).
      ### Security Policies
      * This API requires one of the following user roles: CSPAdmin, CSPTester, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this batch.
      :param id_ [int] The ID of the batch to delete.
      :return ErrorDetail
    """
    def delete_batch(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/batches/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Download a single batch file
    
    Download a single batch file identified by this URL.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns this batch
      :param batchId [int] The ID of the batch object
      :param id_ [int] The primary key of this batch file object
      :return String
    """
    def download_batch(self, companyId, batchId, id_):
        return requests.get('{}/api/v2/companies/{}/batches/{}/files/{}/attachment'.format(self.base_url, companyId, batchId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single batch
    
    Get the batch object identified by this URL. A batch object is a large
      collection of API calls stored in a compact file.
      Use this endpoint to retrieve the results or check the status of a batch.
      When a batch is created, it is added to the AvaTax Batch Queue and will be
      processed as quickly as possible in the order it was received. To check the
      status of a batch, fetch the batch and retrieve the results of the batch
      operation.
      Because the batch system processes with a degree of concurrency, and
      because of batch sizes in the queue vary, AvaTax API is unable to accurately
      predict when a batch will complete. If high performance processing is
      required, please use the
      [CreateTransaction API](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Transactions/CreateTransaction/).
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns this batch
      :param id_ [int] The primary key of this batch
      :return BatchModel
    """
    def get_batch(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/batches/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all batches for this company
    
    List all batch objects attached to the specified company.
      A batch object is a large collection of API calls stored in a compact file.
      Search for specific objects using the criteria in the `$filter` parameter;
      full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate results using the `$top`, `$skip`, and `$orderby` parameters.
      Use [GetBatch](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Batches/GetBatch/)
      to retrieve the results, or check the status, of an individual batch.
      When a batch is created, it is added to the AvaTax Batch Queue and will be
      processed as quickly as possible in the order it was received. To check the
      status of a batch, fetch the batch and retrieve the results of the batch
      operation.
      Because the batch system processes with a degree of concurrency, and
      because of batch sizes in the queue vary, AvaTax API is unable to accurately
      predict when a batch will complete. If high performance processing is
      required, please use the
      [CreateTransaction API](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Transactions/CreateTransaction/).
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns these batches
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* files
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_batches_by_company(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/batches'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all batches
    
    Get multiple batch objects across all companies.
      A batch object is a large collection of API calls stored in a compact file.
      Search for specific objects using the criteria in the `$filter` parameter;
      full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate results using the `$top`, `$skip`, and `$orderby` parameters.
      When a batch is created, it is added to the AvaTax Batch Queue and will be
      processed as quickly as possible in the order it was received. To check the
      status of a batch, fetch the batch and retrieve the results of the batch
      operation.
      Because the batch system processes with a degree of concurrency, and
      because of batch sizes in the queue vary, AvaTax API is unable to accurately
      predict when a batch will complete. If high performance processing is
      required, please use the
      [CreateTransaction API](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Transactions/CreateTransaction/).
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* files
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_batches(self, include=None):
        return requests.get('{}/api/v2/batches'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a CertExpress invitation
    
    Creates an invitation for a customer to self-report certificates using the CertExpress website.
      This invitation is delivered by your choice of method, or you can present a hyperlink to the user
      directly in your connector. Your customer will be redirected to https://app.certexpress.com/ where
      they can follow a step-by-step guide to enter information about their exemption certificates. The
      certificates entered will be recorded and automatically linked to their customer record.
      The [CertExpress website](https://app.certexpress.com/home) is available for customers to use at any time.
      Using CertExpress with this API will ensure that your certificates are automatically linked correctly into
      your company so that they can be used for tax exemptions.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that will record certificates
      :param customerCode [string] The number of the customer where the request is sent to
      :param model [CreateCertExpressInvitationModel] the requests to send out to customers
      :return CertExpressInvitationStatusModel
    """
    def create_cert_express_invitation(self, companyId, customerCode, model):
        return requests.post('{}/api/v2/companies/{}/customers/{}/certexpressinvites'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single CertExpress invitation
    
    Retrieve an existing CertExpress invitation sent to a customer.
      A CertExpression invitation allows a customer to follow a helpful step-by-step guide to provide information
      about their certificates. This step by step guide allows the customer to complete and upload the full
      certificate in a convenient, friendly web browser experience. When the customer completes their certificates,
      they will automatically be recorded to your company and linked to the customer record.
      The [CertExpress website](https://app.certexpress.com/home) is available for customers to use at any time.
      Using CertExpress with this API will ensure that your certificates are automatically linked correctly into
      your company so that they can be used for tax exemptions.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that issued this invitation
      :param customerCode [string] The number of the customer where the request is sent to
      :param id_ [int] The unique ID number of this CertExpress invitation
      :param include [string] OPTIONAL: A comma separated list of special fetch options. No options are defined at this time.
      :return CertExpressInvitationModel
    """
    def get_cert_express_invitation(self, companyId, customerCode, id_, include=None):
        return requests.get('{}/api/v2/companies/{}/customers/{}/certexpressinvites/{}'.format(self.base_url, companyId, customerCode, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List CertExpress invitations
    
    Retrieve CertExpress invitations sent by this company.
      A CertExpression invitation allows a customer to follow a helpful step-by-step guide to provide information
      about their certificates. This step by step guide allows the customer to complete and upload the full
      certificate in a convenient, friendly web browser experience. When the customer completes their certificates,
      they will automatically be recorded to your company and linked to the customer record.
      The [CertExpress website](https://app.certexpress.com/home) is available for customers to use at any time.
      Using CertExpress with this API will ensure that your certificates are automatically linked correctly into
      your company so that they can be used for tax exemptions.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that issued this invitation
      :param include [string] OPTIONAL: A comma separated list of special fetch options.      No options are defined at this time.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* companyId, customer, coverLetter, exposureZones, exemptReasons, requestLink
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_cert_express_invitations(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/certexpressinvites'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create certificates for this company
    
    Record one or more certificates document for this company.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      When you create a certificate, it will be processed by Avalara and will become available for use in
      calculating tax exemptions when processing is complete. For a certificate to be used in calculating exemptions,
      it must have the following:
      * A list of exposure zones indicating where the certificate is valid
      * A link to the customer that is allowed to use this certificate
      * Your tax transaction must contain the correct customer code
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      If the users specified in the certificates do not exist, the API will create the user and link them to the certificate
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The ID number of the company recording this certificate
      :param preValidatedExemptionReason [boolean] If set to true, the certificate will bypass the human verification process.
      :param model [CertificateModel] Certificates to be created
      :return CertificateModel
    """
    def create_certificates(self, companyId, model, include=None):
        return requests.post('{}/api/v2/companies/{}/certificates'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Revoke and delete a certificate
    
    Revoke the certificate identified by this URL, then delete it.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Revoked certificates can no longer be used.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :return ErrorDetail
    """
    def delete_certificate(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/certificates/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Download an image for this certificate
    
    Download an image or PDF file for this certificate.
      This API can be used to download either a single-page preview of the certificate or a full PDF document.
      To retrieve a preview image, set the `$type` parameter to `Jpeg` and the `$page` parameter to `1`.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :param page [int] If you choose `$type`=`Jpeg`, you must specify which page number to retrieve.
      :param type [CertificatePreviewType] The data format in which to retrieve the certificate image (See CertificatePreviewType::* for a list of allowable values)
      :return String
    """
    def download_certificate_image(self, companyId, id_, include=None):
        return requests.get('{}/api/v2/companies/{}/certificates/{}/attachment'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single certificate
    
    Get the current certificate identified by this URL.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      You can use the `$include` parameter to fetch the following additional objects for expansion:
      * customers - Retrieves the list of customers linked to the certificate.
      * po_numbers - Retrieves all PO numbers tied to the certificate.
      * attributes - Retrieves all attributes applied to the certificate.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :param include [string] OPTIONAL: A comma separated list of special fetch options. You can specify one or more of the following:      * customers - Retrieves the list of customers linked to the certificate.   * po_numbers - Retrieves all PO numbers tied to the certificate.   * attributes - Retrieves all attributes applied to the certificate.
      :return CertificateModel
    """
    def get_certificate(self, companyId, id_, include=None):
        return requests.get('{}/api/v2/companies/{}/certificates/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Check a company's exemption certificate status.
    
    Checks whether this company is configured to use exemption certificates in AvaTax.
      Exemption certificates are tracked through a different auditable data store than the one that
      holds AvaTax transactions. To use the AvaTax exemption certificate document store, please call
      `GetCertificateSetup` to see if your company is configured to use the exemption certificate
      document store. To request setup, please call `RequestCertificateSetup` and your company will
      be configured with data storage in the auditable certificate system.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The company ID to check
      :return ProvisionStatusModel
    """
    def get_certificate_setup(self, companyId):
        return requests.get('{}/api/v2/companies/{}/certificates/setup'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Link attributes to a certificate
    
    Link one or many attributes to a certificate.
      A certificate may have multiple attributes that control its behavior. You may link or unlink attributes to a
      certificate at any time. The full list of defined attributes may be found using `ListCertificateAttributes`.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :param model [CertificateAttributeModel] The list of attributes to link to this certificate.
      :return FetchResult
    """
    def link_attributes_to_certificate(self, companyId, id_, model):
        return requests.post('{}/api/v2/companies/{}/certificates/{}/attributes/link'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Link customers to a certificate
    
    Link one or more customers to an existing certificate.
      Customers and certificates must be linked before a customer can make use of a certificate to obtain
      a tax exemption in AvaTax. Since some certificates may cover more than one business entity, a certificate
      can be connected to multiple customer records using the `LinkCustomersToCertificate` API.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :param model [LinkCustomersModel] The list of customers needed be added to the Certificate for exemption
      :return FetchResult
    """
    def link_customers_to_certificate(self, companyId, id_, model):
        return requests.post('{}/api/v2/companies/{}/certificates/{}/customers/link'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all attributes applied to this certificate
    
    Retrieve the list of attributes that are linked to this certificate.
      A certificate may have multiple attributes that control its behavior. You may link or unlink attributes to a
      certificate at any time. The full list of defined attributes may be found using [ListCertificateAttributes](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Definitions/ListCertificateAttributes/) API.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :return FetchResult
    """
    def list_attributes_for_certificate(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/certificates/{}/attributes'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List customers linked to this certificate
    
    List all customers linked to this certificate.
      Customers must be linked to a certificate in order to make use of its tax exemption features. You
      can link or unlink customers to a certificate at any time.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :param include [string] OPTIONAL: A comma separated list of special fetch options.   No options are currently available when fetching customers.
      :return FetchResult
    """
    def list_customers_for_certificate(self, companyId, id_, include=None):
        return requests.get('{}/api/v2/companies/{}/certificates/{}/customers'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all certificates for a company
    
    List all certificates recorded by a company
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      You can use the `$include` parameter to fetch the following additional objects for expansion:
      * customers - Retrieves the list of customers linked to the certificate.
      * po_numbers - Retrieves all PO numbers tied to the certificate.
      * attributes - Retrieves all attributes applied to the certificate.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The ID number of the company to search
      :param include [string] OPTIONAL: A comma separated list of special fetch options. You can specify one or more of the following:      * customers - Retrieves the list of customers linked to the certificate.   * po_numbers - Retrieves all PO numbers tied to the certificate.   * attributes - Retrieves all attributes applied to the certificate.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* exemptionNumber, status, ecmsId, ecmsStatus, pdf, pages
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_certificates(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/certificates'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Request setup of exemption certificates for this company.
    
    Requests the setup of exemption certificates for this company.
      Exemption certificates are tracked through a different auditable data store than the one that
      holds AvaTax transactions. To use the AvaTax exemption certificate document store, please call
      `GetCertificateSetup` to see if your company is configured to use the exemption certificate
      document store. To request setup, please call `RequestCertificateSetup` and your company will
      be configured with data storage in the auditable certificate system.
      This API will return the current status of exemption certificate setup for this company.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] 
      :return ProvisionStatusModel
    """
    def request_certificate_setup(self, companyId):
        return requests.post('{}/api/v2/companies/{}/certificates/setup'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Unlink attributes from a certificate
    
    Unlink one or many attributes from a certificate.
      A certificate may have multiple attributes that control its behavior. You may link or unlink attributes to a
      certificate at any time. The full list of defined attributes may be found using `ListCertificateAttributes`.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :param model [CertificateAttributeModel] The list of attributes to unlink from this certificate.
      :return FetchResult
    """
    def unlink_attributes_from_certificate(self, companyId, id_, model):
        return requests.post('{}/api/v2/companies/{}/certificates/{}/attributes/unlink'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Unlink customers from a certificate
    
    Unlinks one or more customers from a certificate.
      Unlinking a certificate from a customer will prevent the certificate from being used to generate
      tax exemptions for the customer in the future. If any previous transactions for this customer had
      used this linked certificate, those transactions will be unchanged and will still have a link to the
      exemption certificate in question.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :param model [LinkCustomersModel] The list of customers to unlink from this certificate
      :return FetchResult
    """
    def unlink_customers_from_certificate(self, companyId, id_, model):
        return requests.post('{}/api/v2/companies/{}/certificates/{}/customers/unlink'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single certificate
    
    Replace the certificate identified by this URL with a new one.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :param model [CertificateModel] The new certificate object that will replace the existing one
      :return CertificateModel
    """
    def update_certificate(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/certificates/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Upload an image or PDF attachment for this certificate
    
    Upload an image or PDF attachment for this certificate.
      Image attachments can be of the format `PDF`, `JPEG`, `TIFF`, or `PNG`. To upload a multi-page image, please
      use the `PDF` data type.
      A certificate is a document stored in either AvaTax Exemptions or CertCapture. The certificate document
      can contain information about a customer's eligibility for exemption from sales or use taxes based on
      criteria you specify when you store the certificate. To view or manage your certificates directly, please
      log onto the administrative website for the product you purchased.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this certificate
      :param id_ [int] The unique ID number of this certificate
      :param file [String] The exemption certificate file you wanted to upload. Accepted formats are: PDF, JPEG, TIFF, PNG.
      :return string
    """
    def upload_certificate_image(self, companyId, id_):
        return requests.post('{}/api/v2/companies/{}/certificates/{}/attachment'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Checks whether the integration being used to set up this company and run transactions onto this company is compliant to all requirements.
    
    Examines the most recent 100 transactions or data from the last month when verifying transaction-related integrations.
      For partners who write integrations against AvaTax for many clients, this API is a way to do a quick self testing to verify whether the
      written integrations for a company are sufficient enough to be delivered to the respective customers to start using it.
      This API provides messages specific enough (through predefined checks) to guide the partner on what integrations are still missing from the company to get fully certified.
      The API makes the following checks to conclude if the company is NOT fully certified:
      1. Any past month items contains generic tax code of P0000000.
      2. All the companies on the requesting account are test companies.
      3. No Voided/Cancelled documents in the past 30 days.
      4. There are less than 2 committed documents.
      5. Any documentCode is a generic GUID string.
      6. Any customerCode on document is a generic GUID string.
      7. No document has more than 1 documentLine.
      8. All of the documents have missing exemptionNo, customerUsageType, taxDateOverride or negative amount.
      9. Any document quantity is a negative number.
      10. Any document have repeated lines.
      11. No document has shipping charge.
      12. All documents have same ItemCodes, descriptions and taxCodes.
      13. Less than 2 addresses used across all documents.
      14. Whether locationCode was used in documents.
      15. Account with AvaGlobal subscription and no documents have VATBuyerId.
      16. Any document has currencyCode not being USD for accounts with AvaGlobal subscription.
      17. All documents have countryCode used for accounts with AvaGlobal subscription.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The ID of the company to check if its integration is certified.
      :return string
    """
    def certify_integration(self, id_):
        return requests.get('{}/api/v2/companies/{}/certify'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Change the filing status of this company
    
    Changes the current filing status of this company.
      For customers using Avalara's Managed Returns Service, each company within their account can request
      for Avalara to file tax returns on their behalf. Avalara compliance team members will review all
      requested filing calendars prior to beginning filing tax returns on behalf of this company.
      The following changes may be requested through this API:
      * If a company is in `NotYetFiling` status, the customer may request this be changed to `FilingRequested`.
      * Avalara compliance team members may change a company from `FilingRequested` to `FirstFiling`.
      * Avalara compliance team members may change a company from `FirstFiling` to `Active`.
      All other status changes must be requested through the Avalara customer support team.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] 
      :param model [FilingStatusChangeModel] 
      :return string
    """
    def change_filing_status(self, id_, model):
        return requests.post('{}/api/v2/companies/{}/filingstatus'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Quick setup for a company with a single physical address
    
    Shortcut to quickly setup a single-physical-location company with critical information and activate it.
      This API provides quick and simple company setup functionality and does the following things:
      * Create a company object with its own tax profile
      * Add a key contact person for the company
      * Set up one physical location for the main office
      * Declare nexus in all taxing jurisdictions for that main office address
      * Activate the company
      This API only provides a limited subset of functionality compared to the 'Create Company' API call.
      If you need additional features or options not present in this 'Quick Setup' API call, please use the full 'Create Company' call instead.
      Please allow 1 minute before making transactions using the company.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param model [CompanyInitializationModel] Information about the company you wish to create.
      :return CompanyModel
    """
    def company_initialize(self, model):
        return requests.post('{}/api/v2/companies/initialize'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create new companies
    
    Create one or more new company objects.
      A 'company' represents a single corporation or individual that is registered to handle transactional taxes.
      You may attach nested data objects such as contacts, locations, and nexus with this CREATE call, and those objects will be created with the company.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param model [CompanyModel] Either a single company object or an array of companies to create
      :return CompanyModel
    """
    def create_companies(self, model):
        return requests.post('{}/api/v2/companies'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Request managed returns funding setup for a company
    
    This API is available by invitation only.
      Companies that use the Avalara Managed Returns or the SST Certified Service Provider services are
      required to setup their funding configuration before Avalara can begin filing tax returns on their
      behalf.
      Funding configuration for each company is set up by submitting a funding setup request, which can
      be sent either via email or via an embedded HTML widget.
      When the funding configuration is submitted to Avalara, it will be reviewed by treasury team members
      before approval.
      This API records that an ambedded HTML funding setup widget was activated.
      This API requires a subscription to Avalara Managed Returns or SST Certified Service Provider.
      ### Security Policies
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The unique identifier of the company
      :param model [FundingInitiateModel] The funding initialization request
      :return FundingStatusModel
    """
    def create_funding_request(self, id_, model):
        return requests.post('{}/api/v2/companies/{}/funding/setup'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single company
    
    Deleting a company will delete all child companies, and all users attached to this company.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, SSTAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] The ID of the company you wish to delete.
      :return ErrorDetail
    """
    def delete_company(self, id_):
        return requests.delete('{}/api/v2/companies/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Check the funding configuration of a company
    
    This API is available by invitation only.
      Requires a subscription to Avalara Managed Returns or SST Certified Service Provider.
      Returns the funding configuration of the requested company.
      .
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The unique identifier of the company
      :return FundingConfigurationModel
    """
    def funding_configuration_by_company(self, companyId):
        return requests.get('{}/api/v2/companies/{}/funding/configuration'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Check the funding configuration of a company
    
    This API is available by invitation only.
      Requires a subscription to Avalara Managed Returns or SST Certified Service Provider.
      Returns the funding configuration of the requested company.
      .
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The unique identifier of the company
      :param currency [string] The currency of the funding. USD and CAD are the only valid currencies
      :return FundingConfigurationModel
    """
    def funding_configurations_by_company_and_currency(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/funding/configurations'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single company
    
    Get the company object identified by this URL.
      A 'company' represents a single corporation or individual that is registered to handle transactional taxes.
      You may specify one or more of the following values in the '$include' parameter to fetch additional nested data, using commas to separate multiple values:
       * Contacts
       * Items
       * Locations
       * Nexus
       * Settings
       * TaxCodes
       * TaxRules
       * UPC
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The ID of the company to retrieve.
      :param include [string] OPTIONAL: A comma separated list of special fetch options.      * Child objects - Specify one or more of the following to retrieve objects related to each company: "Contacts", "FilingCalendars", "Items", "Locations", "Nexus", "TaxCodes", "NonReportingChildren" or "TaxRules".   * Deleted objects - Specify "FetchDeleted" to retrieve information about previously deleted objects.
      :return CompanyModel
    """
    def get_company(self, id_, include=None):
        return requests.get('{}/api/v2/companies/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Get configuration settings for this company
    
    Retrieve a list of all configuration settings tied to this company.
      Configuration settings provide you with the ability to control features of your account and of your
      tax software. The category name `AvaCertServiceConfig` is reserved for
      Avalara internal software configuration values; to store your own company-level settings, please
      create a new category name that begins with `X-`, for example, `X-MyCustomCategory`.
      Company settings are permanent settings that cannot be deleted. You can set the value of a
      company setting to null if desired and if the particular setting supports it.
      Avalara-based company settings for `AvaCertServiceConfig` affect your company's exemption certificate
      processing, and should be changed with care.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param id_ [int] 
      :return CompanyConfigurationModel
    """
    def get_company_configuration(self, id_):
        return requests.get('{}/api/v2/companies/{}/configuration'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Get this company's filing status
    
    Retrieve the current filing status of this company.
      For customers using Avalara's Managed Returns Service, each company within their account can request
      for Avalara to file tax returns on their behalf. Avalara compliance team members will review all
      requested filing calendars prior to beginning filing tax returns on behalf of this company.
      A company's filing status can be one of the following values:
      * `NoReporting` - This company is not configured to report tax returns; instead, it reports through a parent company.
      * `NotYetFiling` - This company has not yet begun filing tax returns through Avalara's Managed Returns Service.
      * `FilingRequested` - The company has requested to begin filing tax returns, but Avalara's compliance team has not yet begun filing.
      * `FirstFiling` - The company has recently filing tax returns and is in a new status.
      * `Active` - The company is currently active and is filing tax returns via Avalara Managed Returns.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] 
      :return string
    """
    def get_filing_status(self, id_):
        return requests.get('{}/api/v2/companies/{}/filingstatus'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Check managed returns funding status for a company
    
    This API is available by invitation only.
      Requires a subscription to Avalara Managed Returns or SST Certified Service Provider.
      Returns a list of funding setup requests and their current status.
      Each object in the result is a request that was made to setup or adjust funding status for this company.
      ### Security Policies
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The unique identifier of the company
      :return FundingStatusModel
    """
    def list_funding_requests_by_company(self, id_):
        return requests.get('{}/api/v2/companies/{}/funding'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a list of MRS Companies with account
    
    This API is available by invitation only.
      Get a list of companies with an active MRS service.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :return FetchResult
    """
    def list_mrs_companies(self):
        return requests.get('{}/api/v2/companies/mrs'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all companies
    
    Get multiple company objects.
      A `company` represents a single corporation or individual that is registered to handle transactional taxes.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Contacts
      * Items
      * Locations
      * Nexus
      * Settings
      * TaxCodes
      * TaxRules
      * UPC
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param include [string] A comma separated list of objects to fetch underneath this company. Any object with a URL path underneath this company can be fetched by specifying its name.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* IsFein, contacts, items, locations, nexus, settings, taxCodes, taxRules, upcs, nonReportingChildCompanies, exemptCerts
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_companies(self, include=None):
        return requests.get('{}/api/v2/companies'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Change configuration settings for this company
    
    Update configuration settings tied to this company.
      Configuration settings provide you with the ability to control features of your account and of your
      tax software. The category names `AvaCertServiceConfig` is reserved for
      Avalara internal software configuration values; to store your own company-level settings, please
      create a new category name that begins with `X-`, for example, `X-MyCustomCategory`.
      Company settings are permanent settings that cannot be deleted. You can set the value of a
      company setting to null if desired and if the particular setting supports it.
      Avalara-based company settings for `AvaCertServiceConfig` affect your company's exemption certificate
      processing, and should be changed with care.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] 
      :param model [CompanyConfigurationModel] 
      :return CompanyConfigurationModel
    """
    def set_company_configuration(self, id_, model):
        return requests.post('{}/api/v2/companies/{}/configuration'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single company
    
    Replace the existing company object at this URL with an updated object.
      A `CompanyModel` represents a single corporation or individual that is registered to handle transactional taxes.
      All data from the existing object will be replaced with data in the object you PUT.
      When calling `UpdateCompany`, you are permitted to update the company itself. Updates to the nested objects
      such as contacts, locations, or settings are not permitted. To update the nested objects
      To set a field's value to `null`, you may either set its value to `null` or omit that field from the object you PUT.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] The ID of the company you wish to update.
      :param model [CompanyModel] The company object you wish to update.
      :return CompanyModel
    """
    def update_company(self, id_, model):
        return requests.put('{}/api/v2/companies/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    API to modify the reference fields at the document and the line level.
    
    
    
      :param companyId [int] 
      :param model [TransactionReferenceFieldModel] 
      :return FetchResult
    """
    def tag_transaction(self, companyId, model):
        return requests.put('{}/api/v2/companies/{}/transactions/tag'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new contact
    
    Create one or more new contact objects.
      A 'contact' is a person associated with a company who is designated to handle certain responsibilities of
      a tax collecting and filing entity.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this contact.
      :param model [ContactModel] The contacts you wish to create.
      :return ContactModel
    """
    def create_contacts(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/contacts'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single contact
    
    Mark the existing contact object at this URL as deleted.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this contact.
      :param id_ [int] The ID of the contact you wish to delete.
      :return ErrorDetail
    """
    def delete_contact(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/contacts/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single contact
    
    Get the contact object identified by this URL.
      A 'contact' is a person associated with a company who is designated to handle certain responsibilities of
      a tax collecting and filing entity.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param companyId [int] The ID of the company for this contact
      :param id_ [int] The primary key of this contact
      :return ContactModel
    """
    def get_contact(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/contacts/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve contacts for this company
    
    List all contact objects assigned to this company.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param companyId [int] The ID of the company that owns these contacts
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_contacts_by_company(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/contacts'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all contacts
    
    Get multiple contact objects across all companies.
      A 'contact' is a person associated with a company who is designated to handle certain responsibilities of
      a tax collecting and filing entity.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_contacts(self, include=None):
        return requests.get('{}/api/v2/contacts'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single contact
    
    Replace the existing contact object at this URL with an updated object.
      A 'contact' is a person associated with a company who is designated to handle certain responsibilities of
      a tax collecting and filing entity.
      All data from the existing object will be replaced with data in the object you PUT.
      To set a field's value to null, you may either set its value to null or omit that field from the object you post.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that this contact belongs to.
      :param id_ [int] The ID of the contact you wish to update
      :param model [ContactModel] The contact you wish to update.
      :return ContactModel
    """
    def update_contact(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/contacts/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create customers for this company
    
    Create one or more customers for this company.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this `customer` object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      A nested object such as CustomFields could be specified and created along with the customer object. To fetch the
      nested object, please call 'GetCustomer' API with appropriate $include parameters.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this customer
      :param model [CustomerModel] The list of customer objects to be created
      :return CustomerModel
    """
    def create_customers(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/customers'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a customer record
    
    Deletes the customer object referenced by this URL.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this `customer` object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this customer
      :param customerCode [string] The unique code representing this customer
      :return CustomerModel
    """
    def delete_customer(self, companyId, customerCode):
        return requests.delete('{}/api/v2/companies/{}/customers/{}'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single customer
    
    Retrieve the customer identified by this URL.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this customer object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      You can use the `$include` parameter to fetch the following additional objects for expansion:
      * Certificates - Fetch a list of certificates linked to this customer.
      * CustomFields - Fetch a list of custom fields associated to this customer.
      * attributes - Retrieves all attributes applied to the customer.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this customer
      :param customerCode [string] The unique code representing this customer
      :param include [string] Specify optional additional objects to include in this fetch request
      :return CustomerModel
    """
    def get_customer(self, companyId, customerCode, include=None):
        return requests.get('{}/api/v2/companies/{}/customers/{}'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Link attributes to a customer
    
    Link one or many attributes to a customer.
      A customer may have multiple attributes that control its behavior. You may link or unlink attributes to a
      customer at any time. The full list of defined attributes may be found using `QueryCompanyCustomerAttributes` API.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this customer object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded the provided customer
      :param customerCode [string] The unique code representing the current customer
      :param model [CustomerAttributeModel] The list of attributes to link to the customer.
      :return FetchResult
    """
    def link_attributes_to_customer(self, companyId, customerCode, model):
        return requests.put('{}/api/v2/companies/{}/customers/{}/attributes/link'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Link certificates to a customer
    
    Link one or more certificates to a customer.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this `customer` object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this customer
      :param customerCode [string] The unique code representing this customer
      :param model [LinkCertificatesModel] The list of certificates to link to this customer
      :return FetchResult
    """
    def link_certificates_to_customer(self, companyId, customerCode, model):
        return requests.post('{}/api/v2/companies/{}/customers/{}/certificates/link'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Link two customer records together
    
    Links a Ship-To customer record with a Bill-To customer record.
      Customer records represent businesses or individuals who can provide exemption certificates. Some customers
      may have certificates that are linked to their shipping address or their billing address. To group these
      customer records together, you may link multiple bill-to and ship-to addresses together to represent a single
      entity that has multiple different addresses of different kinds.
      In general, a customer will have only one primary billing address and multiple ship-to addresses, representing
      all of the different locations where they receive goods. To facilitate this type of customer, you can send in
      one bill-to customer code and multiple ship-to customer codes in a single API call.
      Note that you can only link a ship-to customer record to a bill-to customer record. You may not link two customers
      of the same kind together.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company defining customers.
      :param code [string] The code of the bill-to customer to link.
      :param model [LinkCustomersModel] A list of information about ship-to customers to link to this bill-to customer.
      :return CustomerModel
    """
    def link_ship_to_customers_to_bill_customer(self, companyId, code, model):
        return requests.post('{}/api/v2/companies/{}/customers/billto/{}/shipto/link'.format(self.base_url, companyId, code),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a customer's attributes
    
    Retrieve the attributes linked to the customer identified by this URL.
      A customer may have multiple attributes that control its behavior. You may link or unlink attributes to a
      customer at any time. The full list of defined attributes may be found using `QueryCompanyCustomerAttributes` API.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this customer object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded the provided customer
      :param customerCode [string] The unique code representing the current customer
      :return FetchResult
    """
    def list_attributes_for_customer(self, companyId, customerCode):
        return requests.get('{}/api/v2/companies/{}/customers/{}/attributes'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List certificates linked to a customer
    
    List all certificates linked to a customer.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this `customer` object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this customer
      :param customerCode [string] The unique code representing this customer
      :param include [string] OPTIONAL: A comma separated list of special fetch options. You can specify one or more of the following:      * customers - Retrieves the list of customers linked to the certificate.   * po_numbers - Retrieves all PO numbers tied to the certificate.   * attributes - Retrieves all attributes applied to the certificate.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* exemptionNumber, status, ecmsId, ecmsStatus, pdf, pages
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_certificates_for_customer(self, companyId, customerCode, include=None):
        return requests.get('{}/api/v2/companies/{}/customers/{}/certificates'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List valid certificates for a location
    
    List valid certificates linked to a customer in a particular country and region.
      This API is intended to help identify whether a customer has already provided a certificate that
      applies to a particular country and region. This API is intended to help you remind a customer
      when they have or have not provided copies of their exemption certificates to you during the sales
      order process.
      If a customer does not have a certificate on file and they wish to provide one, you should send the customer
      a CertExpress invitation link so that the customer can upload proof of their exemption certificate. Please
      see the `CreateCertExpressInvitation` API to create an invitation link for this customer.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this customer
      :param customerCode [string] The unique code representing this customer
      :param country [string] Search for certificates matching this country. Uses the ISO 3166 two character country code.
      :param region [string] Search for certificates matching this region. Uses the ISO 3166 two or three character state, region, or province code.
      :return ExemptionStatusModel
    """
    def list_valid_certificates_for_customer(self, companyId, customerCode, country, region):
        return requests.get('{}/api/v2/companies/{}/customers/{}/certificates/{}/{}'.format(self.base_url, companyId, customerCode, country, region),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all customers for this company
    
    List all customers recorded by this company matching the specified criteria.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this `customer` object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      You can use the `$include` parameter to fetch the following additional objects for expansion:
      * Certificates - Fetch a list of certificates linked to this customer.
      * attributes - Retrieves all attributes applied to the customer.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this customer
      :param include [string] OPTIONAL - You can specify the value `certificates` to fetch information about certificates linked to the customer.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* shipTos
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_customers(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/customers'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Unlink attributes from a customer
    
    Unlink one or many attributes from a customer.
      A customer may have multiple attributes that control its behavior. You may link or unlink attributes to a
      customer at any time. The full list of defined attributes may be found using `QueryCompanyCustomerAttributes` API.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this customer object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded the customer
      :param customerCode [string] The unique code representing the current customer
      :param model [CustomerAttributeModel] The list of attributes to unlink from the customer.
      :return FetchResult
    """
    def unlink_attributes_from_customer(self, companyId, customerCode, model):
        return requests.put('{}/api/v2/companies/{}/customers/{}/attributes/unlink'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Unlink certificates from a customer
    
    Remove one or more certificates to a customer.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this `customer` object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this customer
      :param customerCode [string] The unique code representing this customer
      :param model [LinkCertificatesModel] The list of certificates to link to this customer
      :return FetchResult
    """
    def unlink_certificates_from_customer(self, companyId, customerCode, model):
        return requests.post('{}/api/v2/companies/{}/customers/{}/certificates/unlink'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single customer
    
    Replace the customer object at this URL with a new record.
      A customer object defines information about a person or business that purchases products from your
      company. When you create a tax transaction in AvaTax, you can use the `customerCode` from this
      record in your `CreateTransaction` API call. AvaTax will search for this `customerCode` value and
      identify any certificates linked to this `customer` object. If any certificate applies to the transaction,
      AvaTax will record the appropriate elements of the transaction as exempt and link it to the `certificate`.
      Using exemption certificates endpoints requires setup of an auditable document storage for each company that will use certificates.
      Companies that do not have this storage system set up will receive the error `CertCaptureNotConfiguredError` when they call exemption
      certificate related APIs. To check if this company is set up, call `GetCertificateSetup`. To request setup of the auditable document
      storage for this company, call `RequestCertificateSetup`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The unique ID number of the company that recorded this customer
      :param customerCode [string] The unique code representing this customer
      :param model [CustomerModel] The new customer model that will replace the existing record at this URL
      :return CustomerModel
    """
    def update_customer(self, companyId, customerCode, model):
        return requests.put('{}/api/v2/companies/{}/customers/{}'.format(self.base_url, companyId, customerCode),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create and store new datasources for the respective companies.
    
    Create one or more datasource objects.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The id of the company you which to create the datasources
      :param model [DataSourceModel] 
      :return DataSourceModel
    """
    def create_data_sources(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/datasources'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a datasource by datasource id for a company.
    
    Marks the existing datasource for a company as deleted.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The id of the company the datasource belongs to.
      :param id_ [int] The id of the datasource you wish to delete.
      :return ErrorDetail
    """
    def delete_data_source(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/datasources/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Get data source by data source id
    
    Retrieve the data source by its unique ID number.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] 
      :param id_ [int] data source id
      :return DataSourceModel
    """
    def get_data_source_by_id(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/datasources/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all datasources for this company
    
    Gets multiple datasource objects for a given company.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The id of the company you wish to retrieve the datasources.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* isEnabled, isSynced, isAuthorized
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_data_sources(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/datasources'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all datasources
    
    Get multiple datasource objects across all companies.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* isEnabled, isSynced, isAuthorized
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_data_sources(self, include=None):
        return requests.get('{}/api/v2/datasources'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a datasource identified by id for a company
    
    Updates a datasource for a company.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The id of the company the datasource belongs to.
      :param id_ [int] The id of the datasource you wish to delete.
      :param model [DataSourceModel] 
      :return DataSourceModel
    """
    def update_data_source(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/datasources/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Lists all parents of an HS Code.
    
    Retrieves the specified HS code and all of its parents, reflecting all sections, chapters, headings, and subheadings
      a list of HS Codes that are the parents and information branches of the HS Code for the given
      destination country, if lower detail is available.
      This API will include information branches if applicable. These do not have HS Codes and cannot be referenced,
      but can contain information relevant to deciding the correct HS Code.
      This API is intended to be useful to review the descriptive hierarchy of an HS Code, which can be particularly helpful
      when HS Codes can have multiple levels of generic descriptions.
      ### Security Policies
      * This API depends on the following active services<br />*Required* (all): AvaTaxGlobal.
    
      :param country [string] The name or code of the destination country.
      :param hsCode [string] The partial or full HS Code for which you would like to view all of the parents.
      :return FetchResult
    """
    def get_cross_border_code(self, country, hsCode):
        return requests.get('{}/api/v2/definitions/crossborder/{}/{}/hierarchy'.format(self.base_url, country, hsCode),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Test whether a form supports online login verification
    
    This API is intended to be useful to identify whether the user should be allowed
      to automatically verify their login and password. This API will provide a result only if the form supports automatic online login verification.
    
      :param form [string] The name of the form you would like to verify. This is the tax form code
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* taxFormCodes, scraperType, expectedResponseTime, requiredFilingCalendarDataFields
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def get_login_verifier_by_form(self, form, include=None):
        return requests.get('{}/api/v2/definitions/filingcalendars/loginverifiers/{}'.format(self.base_url, form),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of the AvaFile Forms available
    
    This API is deprecated.
      Please use the ListTaxForms API.
      Returns the full list of Avalara-supported AvaFile Forms
      This API is intended to be useful to identify all the different AvaFile Forms
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* outletTypeId
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_ava_file_forms(self, include=None):
        return requests.get('{}/api/v2/definitions/avafileforms'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List certificate attributes used by a company
    
    List the certificate attributes defined by a company.
      A certificate may have multiple attributes that control its behavior. You may apply or remove attributes to a
      certificate at any time.
      If you see the 'CertCaptureNotConfiguredError', please use CheckProvision and RequestProvision endpoints to
      check and provision account.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_certificate_attributes(self, include=None):
        return requests.get('{}/api/v2/definitions/certificateattributes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List the certificate exempt reasons defined by a company
    
    List the certificate exempt reasons defined by a company.
      An exemption reason defines why a certificate allows a customer to be exempt
      for purposes of tax calculation.
      If you see the 'CertCaptureNotConfiguredError', please use CheckProvision and RequestProvision endpoints to
      check and provision account.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_certificate_exempt_reasons(self, include=None):
        return requests.get('{}/api/v2/definitions/certificateexemptreasons'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List certificate exposure zones used by a company
    
    List the certificate exposure zones defined by a company.
      An exposure zone is a location where a certificate can be valid. Exposure zones may indicate a taxing
      authority or other legal entity to which a certificate may apply.
      If you see the 'CertCaptureNotConfiguredError', please use CheckProvision and RequestProvision endpoints to
      check and provision account.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* id, companyId, name, tag, description, created, modified, region, country
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_certificate_exposure_zones(self, include=None):
        return requests.get('{}/api/v2/definitions/certificateexposurezones'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of communications service types
    
    Returns full list of service types for a given transaction type ID.
    
      :param id_ [int] The transaction type ID to examine
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* requiredParameters
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_communications_service_types(self, id_, include=None):
        return requests.get('{}/api/v2/definitions/communications/transactiontypes/{}/servicetypes'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of communications transactiontypes
    
    Returns full list of communications transaction types which
      are accepted in communication tax calculation requests.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_communications_transaction_types(self, include=None):
        return requests.get('{}/api/v2/definitions/communications/transactiontypes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of communications transaction/service type pairs
    
    Returns full list of communications transaction/service type pairs which
      are accepted in communication tax calculation requests.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* requiredParameters
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_communications_t_s_pairs(self, include=None):
        return requests.get('{}/api/v2/definitions/communications/tspairs'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all ISO 3166 countries
    
    Returns a list of all ISO 3166 country codes, and their US English friendly names.
      This API is intended to be useful when presenting a dropdown box in your website to allow customers to select a country for
      a shipping address.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* alpha3Code, isEuropeanUnion, localizedNames, addressesRequireRegion
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_countries(self, include=None):
        return requests.get('{}/api/v2/definitions/countries'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List certificate exposure zones used by a company
    
    List available cover letters that can be used when sending invitation to use CertExpress to upload certificates.
      The CoverLetter model represents a message sent along with an invitation to use CertExpress to
      upload certificates. An invitation allows customers to use CertExpress to upload their exemption
      certificates directly; this cover letter explains why the invitation was sent.
      If you see the 'CertCaptureNotConfiguredError', please use CheckProvision and RequestProvision endpoints to
      check and provision account.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* id, companyId, subject, description, createdDate, modifiedDate, pageCount, templateFilename, version
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_cover_letters(self, include=None):
        return requests.get('{}/api/v2/definitions/coverletters'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Lists the next level of HS Codes given a destination country and HS Code prefix.
    
    Retrieves a list of HS Codes that are the children of the prefix for the given destination country, if
      additional children are available.
      HS Code is interchangeable with "tariff code" and definitions are generally unique to a destination country.
      An HS Code describes an item and its eligibility/rate for tariffs. HS Codes are organized by
      Section/Chapter/Heading/Subheading/Classification.
      This API is intended to be useful to identify the correct HS Code to use for your item.
      ### Security Policies
      * This API depends on the following active services<br />*Required* (all): AvaTaxGlobal.
    
      :param country [string] The name or code of the destination country.
      :param hsCode [string] The Section or partial HS Code for which you would like to view the next level of HS Code detail, if more detail is available.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* hsCodeSource, system, destinationCountry, isDecisionNode, zeroPaddingCount, isSystemDefined, isTaxable, effDate, endDate, hsCodeSourceLength
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_cross_border_codes(self, country, hsCode, include=None):
        return requests.get('{}/api/v2/definitions/crossborder/{}/{}'.format(self.base_url, country, hsCode),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List top level HS Code Sections.
    
    Returns the full list of top level HS Code Sections. Sections are the broadest level of detail for
      classifying tariff codes and the items to which they apply. HS Codes are organized
      by Section/Chapter/Heading/Subheading/Classification.
      This API is intended to be useful to identify the top level Sections for
      further LandedCost HS Code lookups.
      ### Security Policies
      * This API depends on the following active services<br />*Required* (all): AvaTaxGlobal.
    
      :return FetchResult
    """
    def list_cross_border_sections(self):
        return requests.get('{}/api/v2/definitions/crossborder/sections'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all ISO 4217 currencies supported by AvaTax.
    
    Lists all ISO 4217 currencies supported by AvaTax.
      This API produces a list of currency codes that can be used when calling AvaTax. The values from this API can be used to fill out the
      `currencyCode` field in a `CreateTransactionModel`.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_currencies(self, include=None):
        return requests.get('{}/api/v2/definitions/currencies'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported entity use codes
    
    Returns the full list of Avalara-supported entity use codes.
      Entity/Use Codes are definitions of the entity who is purchasing something, or the purpose for which the transaction
      is occurring. This information is generally used to determine taxability of the product.
      In order to facilitate correct reporting of your taxes, you are encouraged to select the proper entity use codes for
      all transactions that are exempt.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* validCountries
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_entity_use_codes(self, include=None):
        return requests.get('{}/api/v2/definitions/entityusecodes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported filing frequencies.
    
    Returns the full list of Avalara-supported filing frequencies.
      This API is intended to be useful to identify all the different filing frequencies that can be used in notices.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_filing_frequencies(self, include=None):
        return requests.get('{}/api/v2/definitions/filingfrequencies'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List jurisdictions based on the filter provided
    
    Returns a list of all Avalara-supported taxing jurisdictions.
      This API allows you to examine all Avalara-supported jurisdictions. You can filter your search by supplying
      SQL-like query for fetching only the ones you concerned about. For example: effectiveDate &gt; '2016-01-01'
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* rate, salesRate, signatureCode, useRate
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_jurisdictions(self, include=None):
        return requests.get('{}/api/v2/definitions/jurisdictions'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List jurisdictions near a specific address
    
    Returns a list of all Avalara-supported taxing jurisdictions that apply to this address.
      This API allows you to identify which jurisdictions are nearby a specific address according to the best available geocoding information.
      It is intended to allow you to create a "Jurisdiction Override", which allows an address to be configured as belonging to a nearby
      jurisdiction in AvaTax.
      The results of this API call can be passed to the `CreateJurisdictionOverride` API call.
    
      :param line1 [string] The first address line portion of this address.
      :param line2 [string] The second address line portion of this address.
      :param line3 [string] The third address line portion of this address.
      :param city [string] The city portion of this address.
      :param region [string] The region, state, or province code portion of this address.
      :param postalCode [string] The postal code or zip code portion of this address.
      :param country [string] The two-character ISO-3166 code of the country portion of this address.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* country, Jurisdictions
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_jurisdictions_by_address(self, include=None):
        return requests.get('{}/api/v2/definitions/jurisdictionsnearaddress'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the list of questions that are required for a tax location
    
    Returns the list of additional questions you must answer when declaring a location in certain taxing jurisdictions.
      Some tax jurisdictions require that you register or provide additional information to configure each physical place where
      your company does business.
      This information is not usually required in order to calculate tax correctly, but is almost always required to file your tax correctly.
      You can call this API call for any address and obtain information about what questions must be answered in order to properly
      file tax in that location.
    
      :param line1 [string] The first line of this location's address.
      :param line2 [string] The second line of this location's address.
      :param line3 [string] The third line of this location's address.
      :param city [string] The city part of this location's address.
      :param region [string] The region, state, or province part of this location's address.
      :param postalCode [string] The postal code of this location's address.
      :param country [string] The country part of this location's address.
      :param latitude [decimal] Optionally identify the location via latitude/longitude instead of via address.
      :param longitude [decimal] Optionally identify the location via latitude/longitude instead of via address.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_location_questions_by_address(self, include=None):
        return requests.get('{}/api/v2/definitions/locationquestions'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all forms where logins can be verified automatically
    
    List all forms where logins can be verified automatically.
      This API is intended to be useful to identify whether the user should be allowed
      to automatically verify their login and password.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* taxFormCodes, scraperType, expectedResponseTime, requiredFilingCalendarDataFields
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_login_verifiers(self, include=None):
        return requests.get('{}/api/v2/definitions/filingcalendars/loginverifiers'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported nexus for all countries and regions.
    
    Returns the full list of all Avalara-supported nexus for all countries and regions.
      This API is intended to be useful if your user interface needs to display a selectable list of nexus.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* streamlinedSalesTax, isSSTActive, taxAuthorityId
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_nexus(self, include=None):
        return requests.get('{}/api/v2/definitions/nexus'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all nexus that apply to a specific address.
    
    Returns a list of all Avalara-supported taxing jurisdictions that apply to this address.
      This API allows you to identify which tax authorities apply to a physical location, salesperson address, or point of sale.
      In general, it is usually expected that a company will declare nexus in all the jurisdictions that apply to each physical address
      where the company does business.
      The results of this API call can be passed to the 'Create Nexus' API call to declare nexus for this address.
    
      :param line1 [string] The first address line portion of this address.
      :param line2 [string] The first address line portion of this address.
      :param line3 [string] The first address line portion of this address.
      :param city [string] The city portion of this address.
      :param region [string] Name or ISO 3166 code identifying the region portion of the address.      This field supports many different region identifiers:   * Two and three character ISO 3166 region codes   * Fully spelled out names of the region in ISO supported languages   * Common alternative spellings for many regions      For a full list of all supported codes and names, please see the Definitions API `ListRegions`.
      :param postalCode [string] The postal code or zip code portion of this address.
      :param country [string] Name or ISO 3166 code identifying the country portion of this address.      This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries      For a full list of all supported codes and names, please see the Definitions API `ListCountries`.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* streamlinedSalesTax, isSSTActive, taxAuthorityId
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_nexus_by_address(self, include=None):
        return requests.get('{}/api/v2/definitions/nexus/byaddress'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported nexus for a country.
    
    Returns all Avalara-supported nexus for the specified country.
      This API is intended to be useful if your user interface needs to display a selectable list of nexus filtered by country.
    
      :param country [string] The country in which you want to fetch the system nexus
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* streamlinedSalesTax, isSSTActive, taxAuthorityId
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_nexus_by_country(self, country, include=None):
        return requests.get('{}/api/v2/definitions/nexus/{}'.format(self.base_url, country),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported nexus for a country and region.
    
    Returns all Avalara-supported nexus for the specified country and region.
      This API is intended to be useful if your user interface needs to display a selectable list of nexus filtered by country and region.
    
      :param country [string] The two-character ISO-3166 code for the country.
      :param region [string] The two or three character region code for the region.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* streamlinedSalesTax, isSSTActive, taxAuthorityId
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_nexus_by_country_and_region(self, country, region, include=None):
        return requests.get('{}/api/v2/definitions/nexus/{}/{}'.format(self.base_url, country, region),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List nexus related to a tax form
    
    Retrieves a list of nexus related to a tax form.
      The concept of `Nexus` indicates a place where your company has sufficient physical presence and is obligated
      to collect and remit transaction-based taxes.
      When defining companies in AvaTax, you must declare nexus for your company in order to correctly calculate tax
      in all jurisdictions affected by your transactions.
      This API is intended to provide useful information when examining a tax form. If you are about to begin filing
      a tax form, you may want to know whether you have declared nexus in all the jurisdictions related to that tax
      form in order to better understand how the form will be filled out.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param formCode [string] The form code that we are looking up the nexus for
      :return NexusByTaxFormModel
    """
    def list_nexus_by_form_code(self, formCode):
        return requests.get('{}/api/v2/definitions/nexus/byform/{}'.format(self.base_url, formCode),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of nexus tax type groups
    
    Returns the full list of Avalara-supported nexus tax type groups
      This API is intended to be useful to identify all the different tax sub-types.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* subscriptionTypeId, subscriptionDescription, tabName, showColumn
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_nexus_tax_type_groups(self, include=None):
        return requests.get('{}/api/v2/definitions/nexustaxtypegroups'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax notice customer funding options.
    
    Returns the full list of Avalara-supported tax notice customer funding options.
      This API is intended to be useful to identify all the different notice customer funding options that can be used in notices.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* activeFlag, sortOrder
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notice_customer_funding_options(self, include=None):
        return requests.get('{}/api/v2/definitions/noticecustomerfundingoptions'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax notice customer types.
    
    Returns the full list of Avalara-supported tax notice customer types.
      This API is intended to be useful to identify all the different notice customer types.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* activeFlag, sortOrder
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notice_customer_types(self, include=None):
        return requests.get('{}/api/v2/definitions/noticecustomertypes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax notice filing types.
    
    Returns the full list of Avalara-supported tax notice filing types.
      This API is intended to be useful to identify all the different notice filing types that can be used in notices.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* description, activeFlag, sortOrder
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notice_filingtypes(self, include=None):
        return requests.get('{}/api/v2/definitions/noticefilingtypes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax notice priorities.
    
    Returns the full list of Avalara-supported tax notice priorities.
      This API is intended to be useful to identify all the different notice priorities that can be used in notices.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* activeFlag, sortOrder
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notice_priorities(self, include=None):
        return requests.get('{}/api/v2/definitions/noticepriorities'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax notice reasons.
    
    Returns the full list of Avalara-supported tax notice reasons.
      This API is intended to be useful to identify all the different tax notice reasons.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* description, activeFlag, sortOrder
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notice_reasons(self, include=None):
        return requests.get('{}/api/v2/definitions/noticereasons'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax notice responsibility ids
    
    Returns the full list of Avalara-supported tax notice responsibility ids
      This API is intended to be useful to identify all the different tax notice responsibilities.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* sortOrder
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notice_responsibilities(self, include=None):
        return requests.get('{}/api/v2/definitions/noticeresponsibilities'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax notice root causes
    
    Returns the full list of Avalara-supported tax notice root causes
      This API is intended to be useful to identify all the different tax notice root causes.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* sortOrder
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notice_root_causes(self, include=None):
        return requests.get('{}/api/v2/definitions/noticerootcauses'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax notice statuses.
    
    Returns the full list of Avalara-supported tax notice statuses.
      This API is intended to be useful to identify all the different tax notice statuses.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* isOpen, sortOrder
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notice_statuses(self, include=None):
        return requests.get('{}/api/v2/definitions/noticestatuses'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax notice types.
    
    Returns the full list of Avalara-supported tax notice types.
      This API is intended to be useful to identify all the different notice types that can be used in notices.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* activeFlag, sortOrder
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notice_types(self, include=None):
        return requests.get('{}/api/v2/definitions/noticetypes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported extra parameters for creating transactions.
    
    Returns the full list of Avalara-supported extra parameters for the 'Create Transaction' API call.
      This list of parameters is available for use when configuring your transaction.
      Some parameters are only available for use if you have subscribed to certain features of AvaTax.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* serviceTypes, regularExpression, values
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_parameters(self, include=None):
        return requests.get('{}/api/v2/definitions/parameters'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the parameters by companyCode and itemCode.
    
    Returns the list of parameters based on the company country and state jurisdiction and the item code.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyCode [string] Company code.
      :param itemCode [string] Item code.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* serviceTypes, regularExpression, values
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_parameters_by_item(self, companyCode, itemCode, include=None):
        return requests.get('{}/api/v2/definitions/parameters/byitem/{}/{}'.format(self.base_url, companyCode, itemCode),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported permissions
    
    Returns the full list of Avalara-supported permission types.
      This API is intended to be useful to identify the capabilities of a particular user logon.
    
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :return FetchResult
    """
    def list_permissions(self, include=None):
        return requests.get('{}/api/v2/definitions/permissions'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported postal codes.
    
    Retrieves the list of Avalara-supported postal codes.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_postal_codes(self, include=None):
        return requests.get('{}/api/v2/definitions/postalcodes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all customs duty programs recognized by AvaTax
    
    List all preferred customs duty programs recognized by AvaTax.
      A customs duty program is an optional program you can use to obtain favorable treatment from customs and duty agents.
      An example of a preferred program is NAFTA, which provides preferential rates for products being shipped from neighboring
      countries.
      To select a preferred program for calculating customs and duty rates, call this API to find the appropriate code for your
      preferred program. Next, set the parameter `AvaTax.LC.PreferredProgram` in your `CreateTransaction` call to the code of
      the program.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* effectiveDate, endDate
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_preferred_programs(self, include=None):
        return requests.get('{}/api/v2/definitions/preferredprograms'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all available product classification systems.
    
    List all available product classification systems.
      Tax authorities use product classification systems as a way to identify products and associate them with a tax rate.
      More than one tax authority might use the same product classification system, but they might charge different tax rates for products.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* countries
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_product_classification_systems(self, include=None):
        return requests.get('{}/api/v2/definitions/productclassificationsystems'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all product classification systems available to a company based on its nexus.
    
    Lists all product classification systems available to a company based on its nexus.
      Tax authorities use product classification systems as a way to identify products and associate them with a tax rate.
      More than one tax authority might use the same product classification system, but they might charge different tax rates for products.
    
      :param companyCode [string] The company code.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* countries
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_product_classification_systems_by_company(self, companyCode, include=None):
        return requests.get('{}/api/v2/definitions/productclassificationsystems/bycompany/{}'.format(self.base_url, companyCode),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of rate types for each country
    
    Returns the full list of Avalara-supported rate type file types
      This API is intended to be useful to identify all the different rate types.
    
      :param country [string] The country to examine for rate types
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_rate_types_by_country(self, country, include=None):
        return requests.get('{}/api/v2/definitions/countries/{}/ratetypes'.format(self.base_url, country),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all ISO 3166 regions
    
    Returns a list of all ISO 3166 region codes and their US English friendly names.
      This API is intended to be useful when presenting a dropdown box in your website to allow customers to select a region
      within the country for a shipping addresses.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* localizedNames
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_regions(self, include=None):
        return requests.get('{}/api/v2/definitions/regions'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all ISO 3166 regions for a country
    
    Returns a list of all ISO 3166 region codes for a specific country code, and their US English friendly names.
      This API is intended to be useful when presenting a dropdown box in your website to allow customers to select a region
      within the country for a shipping addresses.
    
      :param country [string] The country of which you want to fetch ISO 3166 regions
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* localizedNames
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_regions_by_country(self, country, include=None):
        return requests.get('{}/api/v2/definitions/countries/{}/regions'.format(self.base_url, country),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported resource file types
    
    Returns the full list of Avalara-supported resource file types
      This API is intended to be useful to identify all the different resource file types.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_resource_file_types(self, include=None):
        return requests.get('{}/api/v2/definitions/resourcefiletypes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported permissions
    
    Returns the full list of Avalara-supported permission types.
      This API is intended to be useful when designing a user interface for selecting the security role of a user account.
      Some security roles are restricted for Avalara internal use.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_security_roles(self, include=None):
        return requests.get('{}/api/v2/definitions/securityroles'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported subscription types
    
    Returns the full list of Avalara-supported subscription types.
      This API is intended to be useful for identifying which features you have added to your account.
      You may always contact Avalara's sales department for information on available products or services.
      You cannot change your subscriptions directly through the API.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_subscription_types(self, include=None):
        return requests.get('{}/api/v2/definitions/subscriptiontypes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax authorities.
    
    Returns the full list of Avalara-supported tax authorities.
      This API is intended to be useful to identify all the different authorities that receive tax.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_tax_authorities(self, include=None):
        return requests.get('{}/api/v2/definitions/taxauthorities'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported forms for each tax authority.
    
    Returns the full list of Avalara-supported forms for each tax authority.
      This list represents tax forms that Avalara recognizes.
      Customers who subscribe to Avalara Managed Returns Service can request these forms to be filed automatically
      based on the customer's AvaTax data.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_tax_authority_forms(self, include=None):
        return requests.get('{}/api/v2/definitions/taxauthorityforms'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax authority types.
    
    Returns the full list of Avalara-supported tax authority types.
      This API is intended to be useful to identify all the different authority types.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_tax_authority_types(self, include=None):
        return requests.get('{}/api/v2/definitions/taxauthoritytypes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax codes.
    
    Retrieves the list of Avalara-supported system tax codes.
      A 'TaxCode' represents a uniquely identified type of product, good, or service.
      Avalara supports correct tax rates and taxability rules for all TaxCodes in all supported jurisdictions.
      If you identify your products by tax code in your 'Create Transacion' API calls, Avalara will correctly calculate tax rates and
      taxability rules for this product in all supported jurisdictions.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_tax_codes(self, include=None):
        return requests.get('{}/api/v2/definitions/taxcodes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of Avalara-supported tax code types.
    
    Returns the full list of recognized tax code types.
      A 'Tax Code Type' represents a broad category of tax codes, and is less detailed than a single TaxCode.
      This API is intended to be useful for broadly searching for tax codes by tax code type.
    
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :return TaxCodeTypesModel
    """
    def list_tax_code_types(self, include=None):
        return requests.get('{}/api/v2/definitions/taxcodetypes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of the Tax Forms available
    
    Returns the full list of Avalara-supported Tax Forms
      This API is intended to be useful to identify all the different Tax Forms
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_tax_forms(self, include=None):
        return requests.get('{}/api/v2/definitions/taxforms'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of tax sub types
    
    Returns the full list of Avalara-supported tax sub-types
      This API is intended to be useful to identify all the different tax sub-types.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_tax_sub_types(self, include=None):
        return requests.get('{}/api/v2/definitions/taxsubtypes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve the full list of tax type groups
    
    Returns the full list of Avalara-supported tax type groups
      This API is intended to be useful to identify all the different tax type groups.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* subscriptionTypeId, subscriptionDescription, tabName, showColumn, displaySequence
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_tax_type_groups(self, include=None):
        return requests.get('{}/api/v2/definitions/taxtypegroups'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all defined units of measurement
    
    List all units of measurement systems defined by Avalara.
      A unit of measurement system is a method of measuring a quantity, such as distance, mass, or others.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* id
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_unit_of_measurement(self, include=None):
        return requests.get('{}/api/v2/definitions/unitofmeasurements'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create one or more DistanceThreshold objects
    
    Create one or more DistanceThreshold objects for this company.
      A company-distance-threshold model indicates the distance between a company
      and the taxing borders of various countries. Distance thresholds are necessary
      to correctly calculate some value-added taxes.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The unique ID number of the company that owns this DistanceThreshold
      :param model [CompanyDistanceThresholdModel] The DistanceThreshold object or objects you wish to create.
      :return CompanyDistanceThresholdModel
    """
    def create_distance_threshold(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/distancethresholds'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single DistanceThreshold object
    
    Marks the DistanceThreshold object identified by this URL as deleted.
      A company-distance-threshold model indicates the distance between a company
      and the taxing borders of various countries. Distance thresholds are necessary
      to correctly calculate some value-added taxes.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The unique ID number of the company that owns this DistanceThreshold
      :param id_ [int] The unique ID number of the DistanceThreshold object you wish to delete.
      :return ErrorDetail
    """
    def delete_distance_threshold(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/distancethresholds/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single DistanceThreshold
    
    Retrieves a single DistanceThreshold object defined by this URL.
      A company-distance-threshold model indicates the distance between a company
      and the taxing borders of various countries. Distance thresholds are necessary
      to correctly calculate some value-added taxes.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param companyId [int] The ID of the company that owns this DistanceThreshold object
      :param id_ [int] The unique ID number referring to this DistanceThreshold object
      :return CompanyDistanceThresholdModel
    """
    def get_distance_threshold(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/distancethresholds/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all DistanceThresholds for this company.
    
    Lists all DistanceThreshold objects that belong to this company.
      A company-distance-threshold model indicates the distance between a company
      and the taxing borders of various countries. Distance thresholds are necessary
      to correctly calculate some value-added taxes.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param companyId [int] The ID of the company whose DistanceThreshold objects you wish to list.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_distance_thresholds(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/distancethresholds'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all DistanceThreshold objects
    
    Lists all DistanceThreshold objects that belong to this account.
      A company-distance-threshold model indicates the distance between a company
      and the taxing borders of various countries. Distance thresholds are necessary
      to correctly calculate some value-added taxes.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_distance_thresholds(self, include=None):
        return requests.get('{}/api/v2/distancethresholds'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a DistanceThreshold object
    
    Replace the existing DistanceThreshold object at this URL with an updated object.
      A company-distance-threshold model indicates the distance between a company
      and the taxing borders of various countries. Distance thresholds are necessary
      to correctly calculate some value-added taxes.
      All data from the existing object will be replaced with data in the object you PUT.
      To set a field's value to null, you may either set its value to null or omit that field from the object you post.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The unique ID number of the company that owns this DistanceThreshold object.
      :param id_ [int] The unique ID number of the DistanceThreshold object to replace.
      :param model [CompanyDistanceThresholdModel] The new DistanceThreshold object to store.
      :return CompanyDistanceThresholdModel
    """
    def update_distance_threshold(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/distancethresholds/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a batch of error transactions
    
    Delete a batch of error transactions attached to a company.
      If any of the provided error transaction isn't found then it'll be treated as a success.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param model [DeleteErrorTransactionsRequestModel] The request that contains error transactions to be deleted
      :return DeleteErrorTransactionsResponseModel
    """
    def delete_error_transactions(self, model):
        return requests.delete('{}/api/v2/errortransactions'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve list of error transactions
    
    List error transactions attached to this company. Results are dependent on `$filter` if provided.
      This endpoint is limited to returning 250 error transactions at a time maximum.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The company code to filter on. This query parameter is required.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* companyId, avataxErrorJson, avataxCreateTransactionJson
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_error_transactions(self, include=None):
        return requests.get('{}/api/v2/errortransactions'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Approves linkage to a firm for a client account
    
    This API enables the account admin of a client account to approve linkage request by a firm.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] 
      :return FirmClientLinkageOutputModel
    """
    def approve_firm_client_linkage(self, id_):
        return requests.post('{}/api/v2/firmclientlinkages/{}/approve'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Request a new FirmClient account and create an approved linkage to it
    
    This API is for use by Firms only.
      Avalara allows firms to manage returns for clients without the clients needing to use AvaTax service.
      Firms can create accounts of FirmClient for customers they are managing using this API.
      Calling this API creates an account with the specified product subscriptions, but without a new user for account.
      Account is then linked to the Firm so they can managed their returns.
      You should call this API when a customer does not have an AvaTax account and is to be managed only by the firm.
      The created account will be created in `Active` status but there will be no user or license key associated with account.
      ### Security Policies
      * This API requires one of the following user roles: FirmAdmin, Registrar, SiteAdmin, SystemAdmin.
    
      :param model [NewFirmClientAccountRequestModel] Information about the account you wish to create.
      :return FirmClientLinkageOutputModel
    """
    def create_and_link_new_firm_client_account(self, model):
        return requests.post('{}/api/v2/firmclientlinkages/createandlinkclient'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Links a firm account with the client account
    
    This API enables the firm admins/firm users to request the linkage of a firm account and a client account.
      ### Security Policies
      * This API requires one of the following user roles: FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param model [FirmClientLinkageInputModel] FirmClientLinkageInputModel
      :return FirmClientLinkageOutputModel
    """
    def create_firm_client_linkage(self, model):
        return requests.post('{}/api/v2/firmclientlinkages'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a linkage
    
    This API marks a linkage between a firm and client as deleted.
      ### Security Policies
      * This API requires one of the following user roles: FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] 
      :return ErrorDetail
    """
    def delete_firm_client_linkage(self, id_):
        return requests.delete('{}/api/v2/firmclientlinkages/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Get linkage between a firm and client by id
    
    This API enables the firm admins/firm users to request the linkage of a firm account and a client account.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] 
      :return FirmClientLinkageOutputModel
    """
    def get_firm_client_linkage(self, id_):
        return requests.get('{}/api/v2/firmclientlinkages/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List client linkages for a firm or client
    
    This API enables the firm or account users to request the associated linkages to the account.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* firmAccountName, clientAccountName
      :return FetchResult
    """
    def list_firm_client_linkage(self, include=None):
        return requests.get('{}/api/v2/firmclientlinkages'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Rejects linkage to a firm for a client account
    
    This API enables the account admin of a client account to reject linkage request by a firm.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] 
      :return FirmClientLinkageOutputModel
    """
    def reject_firm_client_linkage(self, id_):
        return requests.post('{}/api/v2/firmclientlinkages/{}/reject'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Reset linkage status between a client and firm back to requested
    
    This API enables the firm admin of a client account to reset a previously created linkage request by a firm.
      ### Security Policies
      * This API requires one of the following user roles: FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] 
      :return FirmClientLinkageOutputModel
    """
    def reset_firm_client_linkage(self, id_):
        return requests.post('{}/api/v2/firmclientlinkages/{}/reset'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Revokes previously approved linkage to a firm for a client account
    
    This API enables the account admin of a client account to revoke a previously approved linkage request by a firm.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] 
      :return FirmClientLinkageOutputModel
    """
    def revoke_firm_client_linkage(self, id_):
        return requests.post('{}/api/v2/firmclientlinkages/{}/revoke'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    FREE API - Request a free trial of AvaTax
    
    Call this API to obtain a free AvaTax account.
      This API is free to use. No authentication credentials are required to call this API. You must read and
      accept [Avalara's terms and conditions](https://www1.avalara.com/us/en/legal/terms.html) for the account to be
      created.
      If all conditions are met, this API will grant a free trial version of AvaTax. For a list of functionality
      available in the free trial and its limitations, please see the [AvaTax Developer Website Free Trial page](https://developer.avalara.com/avatax/signup/).
      After your free trial concludes, you will still be able to use the [Free AvaTax API Suite](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Free/).
      ### Security Policies
      * This API may be called without providing authentication credentials.
    
      :param model [FreeTrialRequestModel] Required information to provision a free trial account.
      :return NewAccountModel
    """
    def request_free_trial(self, model):
        return requests.post('{}/api/v2/accounts/freetrials/request'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    FREE API - Sales tax rates for a specified address
    
    # Free-To-Use
      The TaxRates API is a free-to-use, no cost option for estimating sales tax rates.
      Any customer can request a free AvaTax account and make use of the TaxRates API.
      Usage of this API is subject to rate limits. Users who exceed the rate limit will receive HTTP
      response code 429 - `Too Many Requests`.
      This API assumes that you are selling general tangible personal property at a retail point-of-sale
      location in the United States only.
      For more powerful tax calculation, please consider upgrading to the `CreateTransaction` API,
      which supports features including, but not limited to:
      * Nexus declarations
      * Taxability based on product/service type
      * Sourcing rules affecting origin/destination states
      * Customers who are exempt from certain taxes
      * States that have dollar value thresholds for tax amounts
      * Refunds for products purchased on a different date
      * Detailed jurisdiction names and state assigned codes
      * And more!
      Please see [Estimating Tax with REST v2](http://developer.avalara.com/blog/2016/11/04/estimating-tax-with-rest-v2/)
      for information on how to upgrade to the full AvaTax CreateTransaction API.
    
      :param line1 [string] The street address of the location.
      :param line2 [string] The street address of the location.
      :param line3 [string] The street address of the location.
      :param city [string] The city name of the location.
      :param region [string] Name or ISO 3166 code identifying the region within the country.     This field supports many different region identifiers:   * Two and three character ISO 3166 region codes   * Fully spelled out names of the region in ISO supported languages   * Common alternative spellings for many regions     For a full list of all supported codes and names, please see the Definitions API `ListRegions`.
      :param postalCode [string] The postal code of the location.
      :param country [string] Name or ISO 3166 code identifying the country.     This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries     For a full list of all supported codes and names, please see the Definitions API `ListCountries`.
      :return TaxRateModel
    """
    def tax_rates_by_address(self, include=None):
        return requests.get('{}/api/v2/taxrates/byaddress'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    FREE API - Sales tax rates for a specified country and postal code. This API is only available for US postal codes.
    
    # Free-To-Use
      This API is only available for a US postal codes.
      The TaxRates API is a free-to-use, no cost option for estimating sales tax rates.
      Any customer can request a free AvaTax account and make use of the TaxRates API.
      Usage of this API is subject to rate limits. Users who exceed the rate limit will receive HTTP
      response code 429 - `Too Many Requests`.
      This API assumes that you are selling general tangible personal property at a retail point-of-sale
      location in the United States only.
      For more powerful tax calculation, please consider upgrading to the `CreateTransaction` API,
      which supports features including, but not limited to:
      * Nexus declarations
      * Taxability based on product/service type
      * Sourcing rules affecting origin/destination states
      * Customers who are exempt from certain taxes
      * States that have dollar value thresholds for tax amounts
      * Refunds for products purchased on a different date
      * Detailed jurisdiction names and state assigned codes
      * And more!
      Please see [Estimating Tax with REST v2](http://developer.avalara.com/blog/2016/11/04/estimating-tax-with-rest-v2/)
      for information on how to upgrade to the full AvaTax CreateTransaction API.
    
      :param country [string] Name or ISO 3166 code identifying the country.     This field supports many different country identifiers:   * Two character ISO 3166 codes   * Three character ISO 3166 codes   * Fully spelled out names of the country in ISO supported languages   * Common alternative spellings for many countries     For a full list of all supported codes and names, please see the Definitions API `ListCountries`.
      :param postalCode [string] The postal code of the location.
      :return TaxRateModel
    """
    def tax_rates_by_postal_code(self, include=None):
        return requests.get('{}/api/v2/taxrates/bypostalcode'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Request the javascript for a funding setup widget
    
    This API is available by invitation only.
      Companies that use the Avalara Managed Returns or the SST Certified Service Provider services are
      required to setup their funding configuration before Avalara can begin filing tax returns on their
      behalf.
      Funding configuration for each company is set up by submitting a funding setup request, which can
      be sent either via email or via an embedded HTML widget.
      When the funding configuration is submitted to Avalara, it will be reviewed by treasury team members
      before approval.
      This API returns back the actual javascript code to insert into your application to render the
      JavaScript funding setup widget inline.
      Use the 'methodReturn.javaScript' return value to insert this widget into your HTML page.
      This API requires a subscription to Avalara Managed Returns or SST Certified Service Provider.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param id_ [int] The unique ID number of this funding request
      :return FundingStatusModel
    """
    def activate_funding_request(self, id_):
        return requests.get('{}/api/v2/fundingrequests/{}/widget'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve status about a funding setup request
    
    This API is available by invitation only.
      Companies that use the Avalara Managed Returns or the SST Certified Service Provider services are
      required to setup their funding configuration before Avalara can begin filing tax returns on their
      behalf.
      Funding configuration for each company is set up by submitting a funding setup request, which can
      be sent either via email or via an embedded HTML widget.
      When the funding configuration is submitted to Avalara, it will be reviewed by treasury team members
      before approval.
      This API checks the status on an existing funding request.
      This API requires a subscription to Avalara Managed Returns or SST Certified Service Provider.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param id_ [int] The unique ID number of this funding request
      :return FundingStatusModel
    """
    def funding_request_status(self, id_):
        return requests.get('{}/api/v2/fundingrequests/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete all classifications for an item
    
    Delete all the classifications for a given item.
      A classification is the code for a product in a particular tax system. Classifications enable an item to be used in multiple tax systems which may have different tax rates for a product.
      When an item is used in a transaction, the applicable classification will be used to determine the appropriate tax rate.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this item.
      :param itemId [int] The ID of the item you wish to delete the classifications.
      :return ErrorDetail
    """
    def batch_delete_item_classifications(self, companyId, itemId):
        return requests.delete('{}/api/v2/companies/{}/items/{}/classifications'.format(self.base_url, companyId, itemId),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete all parameters for an item
    
    Delete all the parameters for a given item.
      Some items can be taxed differently depending on the properties of that item, such as the item grade or by a particular measurement of that item. In AvaTax, these tax-affecting properties are called "parameters".
      A parameter added to an item will be used by default in tax calculation but will not show on the transaction line referencing the item .
      A parameter specified on a transaction line will override an item parameter if they share the same parameter name.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this item.
      :param itemId [int] The ID of the item you wish to delete the parameters.
      :return ErrorDetail
    """
    def batch_delete_item_parameters(self, companyId, itemId):
        return requests.delete('{}/api/v2/companies/{}/items/{}/parameters'.format(self.base_url, companyId, itemId),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Add classifications to an item.
    
    Add classifications to an item.
      A classification is the code for a product in a particular tax system. Classifications enable an item to be used in multiple tax systems which may have different tax rates for a product.
      When an item is used in a transaction, the applicable classification will be used to determine the appropriate tax rate.
      An item may only have one classification per tax system.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The company id.
      :param itemId [int] The item id.
      :param model [ItemClassificationInputModel] The item classifications you wish to create.
      :return ItemClassificationOutputModel
    """
    def create_item_classifications(self, companyId, itemId, model):
        return requests.post('{}/api/v2/companies/{}/items/{}/classifications'.format(self.base_url, companyId, itemId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Add parameters to an item.
    
    Add parameters to an item.
      Some items can be taxed differently depending on the properties of that item, such as the item grade or by a particular measurement of that item. In AvaTax, these tax-affecting properties are called "parameters".
      A parameter added to an item will be used by default in tax calculation but will not show on the transaction line referencing the item .
      A parameter specified on a transaction line will override an item parameter if they share the same parameter name.
      To see available parameters for this item, call `/api/v2/definitions/parameters?$filter=attributeType eq Product`
      Some parameters are only available for use if you have subscribed to specific AvaTax services. To see which parameters you are able to use, add the query parameter "$showSubscribed=true" to the parameter definition call above.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this item parameter.
      :param itemId [int] The item id.
      :param model [ItemParameterModel] The item parameters you wish to create.
      :return ItemParameterModel
    """
    def create_item_parameters(self, companyId, itemId, model):
        return requests.post('{}/api/v2/companies/{}/items/{}/parameters'.format(self.base_url, companyId, itemId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new item
    
    Creates one or more new item objects attached to this company.
      Items are a way of separating your tax calculation process from your tax configuration details. If you choose, you
      can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,
      and other data fields. AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters
      from the item table instead. This allows your CreateTransaction call to be as simple as possible, and your tax compliance
      team can manage your item catalog and adjust the tax behavior of items without having to modify your software.
      The tax code takes precedence over the tax code id if both are provided.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this item.
      :param model [ItemModel] The item you wish to create.
      :return ItemModel
    """
    def create_items(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/items'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single item
    
    Deletes the item object at this URL.
      Items are a way of separating your tax calculation process from your tax configuration details. If you choose, you
      can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,
      and other data fields. AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters
      from the item table instead. This allows your CreateTransaction call to be as simple as possible, and your tax compliance
      team can manage your item catalog and adjust the tax behavior of items without having to modify your software.
      Deleting an item will also delete the parameters and classifications associated with that item.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this item.
      :param id_ [int] The ID of the item you wish to delete.
      :return ErrorDetail
    """
    def delete_item(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/items/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single item classification.
    
    Delete a single item classification.
      A classification is the code for a product in a particular tax system. Classifications enable an item to be used in multiple tax systems which may have different tax rates for a product.
      When an item is used in a transaction, the applicable classification will be used to determine the appropriate tax rate.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The company id.
      :param itemId [int] The item id.
      :param id_ [int] The item classification id.
      :return ErrorDetail
    """
    def delete_item_classification(self, companyId, itemId, id_):
        return requests.delete('{}/api/v2/companies/{}/items/{}/classifications/{}'.format(self.base_url, companyId, itemId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single item parameter
    
    Delete a single item parameter.
      Some items can be taxed differently depending on the properties of that item, such as the item grade or by a particular measurement of that item. In AvaTax, these tax-affecting properties are called "parameters".
      A parameter added to an item will be used by default in tax calculation but will not show on the transaction line referencing the item .
      A parameter specified on a transaction line will override an item parameter if they share the same parameter name.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The company id
      :param itemId [int] The item id
      :param id_ [int] The parameter id
      :return ErrorDetail
    """
    def delete_item_parameter(self, companyId, itemId, id_):
        return requests.delete('{}/api/v2/companies/{}/items/{}/parameters/{}'.format(self.base_url, companyId, itemId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single item
    
    Get the `Item` object identified by this URL.
      Items are a way of separating your tax calculation process from your tax configuration details. If you choose, you
      can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,
      and other data fields. AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters
      from the item table instead. This allows your CreateTransaction call to be as simple as possible, and your tax compliance
      team can manage your item catalog and adjust the tax behavior of items without having to modify your software.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns this item object
      :param id_ [int] The primary key of this item
      :param include [string] A comma separated list of additional data to retrieve.
      :return ItemModel
    """
    def get_item(self, companyId, id_, include=None):
        return requests.get('{}/api/v2/companies/{}/items/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single item classification.
    
    Retrieve a single item classification.
      A classification is the code for a product in a particular tax system. Classifications enable an item to be used in multiple tax systems which may have different tax rates for a product.
      When an item is used in a transaction, the applicable classification will be used to determine the appropriate tax rate.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The company id.
      :param itemId [int] The item id.
      :param id_ [int] The item classification id.
      :return ItemClassificationOutputModel
    """
    def get_item_classification(self, companyId, itemId, id_):
        return requests.get('{}/api/v2/companies/{}/items/{}/classifications/{}'.format(self.base_url, companyId, itemId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single item parameter
    
    Retrieve a single item parameter.
      Some items can be taxed differently depending on the properties of that item, such as the item grade or by a particular measurement of that item. In AvaTax, these tax-affecting properties are called "parameters".
      A parameter added to an item will be used by default in tax calculation but will not show on the transaction line referencing the item .
      A parameter specified on a transaction line will override an item parameter if they share the same parameter name.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The company id
      :param itemId [int] The item id
      :param id_ [int] The parameter id
      :return ItemParameterModel
    """
    def get_item_parameter(self, companyId, itemId, id_):
        return requests.get('{}/api/v2/companies/{}/items/{}/parameters/{}'.format(self.base_url, companyId, itemId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve classifications for an item.
    
    List classifications for an item.
      A classification is the code for a product in a particular tax system. Classifications enable an item to be used in multiple tax systems which may have different tax rates for a product.
      When an item is used in a transaction, the applicable classification will be used to determine the appropriate tax rate.
      Search for specific objects using the criteria in the `$filter` classification; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` classifications.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The company id.
      :param itemId [int] The item id.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* productCode, systemCode
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_item_classifications(self, companyId, itemId, include=None):
        return requests.get('{}/api/v2/companies/{}/items/{}/classifications'.format(self.base_url, companyId, itemId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve parameters for an item
    
    List parameters for an item.
      Some items can be taxed differently depending on the properties of that item, such as the item grade or by a particular measurement of that item. In AvaTax, these tax-affecting properties are called "parameters".
      A parameter added to an item will be used by default in tax calculation but will not show on the transaction line referencing the item .
      A parameter specified on a transaction line will override an item parameter if they share the same parameter name.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The company id
      :param itemId [int] The item id
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* name, unit
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_item_parameters(self, companyId, itemId, include=None):
        return requests.get('{}/api/v2/companies/{}/items/{}/parameters'.format(self.base_url, companyId, itemId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve items for this company
    
    List all items defined for the current company.
      Items are a way of separating your tax calculation process from your tax configuration details. If you choose, you
      can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,
      and other data fields. AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters
      from the item table instead. This allows your CreateTransaction call to be as simple as possible, and your tax compliance
      team can manage your item catalog and adjust the tax behavior of items without having to modify your software.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Parameters
      * Classifications
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that defined these items
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* taxCode, classifications, parameters
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_items_by_company(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/items'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all items
    
    Get multiple item objects across all companies.
      Items are a way of separating your tax calculation process from your tax configuration details. If you choose, you
      can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,
      and other data fields. AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters
      from the item table instead. This allows your CreateTransaction call to be as simple as possible, and your tax compliance
      team can manage your item catalog and adjust the tax behavior of items without having to modify your software.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* taxCode, classifications, parameters
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_items(self, include=None):
        return requests.get('{}/api/v2/items'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Sync items from a product catalog
    
    Syncs a list of items with AvaTax without waiting for them to be created. It is ideal for syncing large product catalogs
      with AvaTax.
      Any invalid or duplicate items will be ignored. To diagnose why an item is not created, use the normal create transaction API to receive validation information.
      This API is currently limited to 1000 items per call (the limit is subject to change).
      Items are a way of separating your tax calculation process from your tax configuration details. If you choose, you
      can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,
      and other data fields. AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters
      from the item table instead. This allows your CreateTransaction call to be as simple as possible, and your tax compliance
      team can manage your item catalog and adjust the tax behavior of items without having to modify your software.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this item.
      :param model [SyncItemsRequestModel] The request object.
      :return SyncItemsResponseModel
    """
    def sync_items(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/items/sync'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single item
    
    Replace the existing `Item` object at this URL with an updated object.
      Items are a way of separating your tax calculation process from your tax configuration details. If you choose, you
      can provide `itemCode` values for each `CreateTransaction()` API call rather than specifying tax codes, parameters, descriptions,
      and other data fields. AvaTax will automatically look up each `itemCode` and apply the correct tax codes and parameters
      from the item table instead. This allows your CreateTransaction call to be as simple as possible, and your tax compliance
      team can manage your item catalog and adjust the tax behavior of items without having to modify your software.
      All data from the existing object will be replaced with data in the object you PUT. To set a field's value to null,
      you may either set its value to null or omit that field from the object you post.
      The tax code takes precedence over the tax code id if both are provided.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that this item belongs to.
      :param id_ [int] The ID of the item you wish to update
      :param model [ItemModel] The item object you wish to update.
      :return ItemModel
    """
    def update_item(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/items/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update an item classification.
    
    Update an item classification.
      A classification is the code for a product in a particular tax system. Classifications enable an item to be used in multiple tax systems which may have different tax rates for a product.
      When an item is used in a transaction, the applicable classification will be used to determine the appropriate tax rate.
      An item may only have one classification per tax system.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The company id.
      :param itemId [int] The item id.
      :param id_ [int] The item classification id.
      :param model [ItemClassificationInputModel] The item object you wish to update.
      :return ItemClassificationOutputModel
    """
    def update_item_classification(self, companyId, itemId, id_, model):
        return requests.put('{}/api/v2/companies/{}/items/{}/classifications/{}'.format(self.base_url, companyId, itemId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update an item parameter
    
    Update an item parameter.
      Some items can be taxed differently depending on the properties of that item, such as the item grade or by a particular measurement of that item. In AvaTax, these tax-affecting properties are called "parameters".
      A parameter added to an item will be used by default in tax calculation but will not show on the transaction line referencing the item .
      A parameter specified on a transaction line will override an item parameter if they share the same parameter name.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The company id.
      :param itemId [int] The item id
      :param id_ [int] The item parameter id
      :param model [ItemParameterModel] The item object you wish to update.
      :return ItemParameterModel
    """
    def update_item_parameter(self, companyId, itemId, id_, model):
        return requests.put('{}/api/v2/companies/{}/items/{}/parameters/{}'.format(self.base_url, companyId, itemId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create one or more overrides
    
    Creates one or more jurisdiction override objects for this account.
      A Jurisdiction Override is a configuration setting that allows you to select the taxing
      jurisdiction for a specific address. If you encounter an address that is on the boundary
      between two different jurisdictions, you can choose to set up a jurisdiction override
      to switch this address to use different taxing jurisdictions.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param accountId [int] The ID of the account that owns this override
      :param model [JurisdictionOverrideModel] The jurisdiction override objects to create
      :return JurisdictionOverrideModel
    """
    def create_jurisdiction_overrides(self, accountId, model):
        return requests.post('{}/api/v2/accounts/{}/jurisdictionoverrides'.format(self.base_url, accountId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single override
    
    Marks the item object at this URL as deleted.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param accountId [int] The ID of the account that owns this override
      :param id_ [int] The ID of the override you wish to delete
      :return ErrorDetail
    """
    def delete_jurisdiction_override(self, accountId, id_):
        return requests.delete('{}/api/v2/accounts/{}/jurisdictionoverrides/{}'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single override
    
    Get the item object identified by this URL.
      A Jurisdiction Override is a configuration setting that allows you to select the taxing
      jurisdiction for a specific address. If you encounter an address that is on the boundary
      between two different jurisdictions, you can choose to set up a jurisdiction override
      to switch this address to use different taxing jurisdictions.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param accountId [int] The ID of the account that owns this override
      :param id_ [int] The primary key of this override
      :return JurisdictionOverrideModel
    """
    def get_jurisdiction_override(self, accountId, id_):
        return requests.get('{}/api/v2/accounts/{}/jurisdictionoverrides/{}'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve overrides for this account
    
    List all jurisdiction override objects defined for this account.
      A Jurisdiction Override is a configuration setting that allows you to select the taxing
      jurisdiction for a specific address. If you encounter an address that is on the boundary
      between two different jurisdictions, you can choose to set up a jurisdiction override
      to switch this address to use different taxing jurisdictions.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param accountId [int] The ID of the account that owns this override
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* country, Jurisdictions
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_jurisdiction_overrides_by_account(self, accountId, include=None):
        return requests.get('{}/api/v2/accounts/{}/jurisdictionoverrides'.format(self.base_url, accountId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all overrides
    
    Get multiple jurisdiction override objects across all companies.
      A Jurisdiction Override is a configuration setting that allows you to select the taxing
      jurisdiction for a specific address. If you encounter an address that is on the boundary
      between two different jurisdictions, you can choose to set up a jurisdiction override
      to switch this address to use different taxing jurisdictions.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* country, Jurisdictions
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_jurisdiction_overrides(self, include=None):
        return requests.get('{}/api/v2/jurisdictionoverrides'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single jurisdictionoverride
    
    Replace the existing jurisdictionoverride object at this URL with an updated object.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param accountId [int] The ID of the account that this jurisdictionoverride belongs to.
      :param id_ [int] The ID of the jurisdictionoverride you wish to update
      :param model [JurisdictionOverrideModel] The jurisdictionoverride object you wish to update.
      :return JurisdictionOverrideModel
    """
    def update_jurisdiction_override(self, accountId, id_, model):
        return requests.put('{}/api/v2/accounts/{}/jurisdictionoverrides/{}'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new location
    
    Create one or more new location objects attached to this company.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this location.
      :param model [LocationModel] The location you wish to create.
      :return LocationModel
    """
    def create_locations(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/locations'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single location
    
    Mark the location object at this URL as deleted.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this location.
      :param id_ [int] The ID of the location you wish to delete.
      :return ErrorDetail
    """
    def delete_location(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/locations/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single location
    
    Get the location object identified by this URL.
      An 'Location' represents a physical address where a company does business.
      Many taxing authorities require that you define a list of all locations where your company does business.
      These locations may require additional custom configuration or tax registration with these authorities.
      For more information on metadata requirements, see the '/api/v2/definitions/locationquestions' API.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * LocationSettings
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param companyId [int] The ID of the company that owns this location
      :param id_ [int] The primary key of this location
      :param include [string] A comma separated list of additional data to retrieve. You may specify `LocationSettings` to retrieve location settings.
      :return LocationModel
    """
    def get_location(self, companyId, id_, include=None):
        return requests.get('{}/api/v2/companies/{}/locations/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve locations for this company
    
    List all location objects defined for this company.
      An 'Location' represents a physical address where a company does business.
      Many taxing authorities require that you define a list of all locations where your company does business.
      These locations may require additional custom configuration or tax registration with these authorities.
      For more information on metadata requirements, see the '/api/v2/definitions/locationquestions' API.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * LocationSettings
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param companyId [int] The ID of the company that owns these locations
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* settings
      :param include [string] A comma separated list of additional data to retrieve. You may specify `LocationSettings` to retrieve location settings.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_locations_by_company(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/locations'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all locations
    
    Get multiple location objects across all companies.
      An 'Location' represents a physical address where a company does business.
      Many taxing authorities require that you define a list of all locations where your company does business.
      These locations may require additional custom configuration or tax registration with these authorities.
      For more information on metadata requirements, see the '/api/v2/definitions/locationquestions' API.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * LocationSettings
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* settings
      :param include [string] A comma separated list of additional data to retrieve. You may specify `LocationSettings` to retrieve location settings.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_locations(self, include=None):
        return requests.get('{}/api/v2/locations'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single location
    
    Replace the existing location object at this URL with an updated object.
      All data from the existing object will be replaced with data in the object you PUT.
      To set a field's value to null, you may either set its value to null or omit that field from the object you post.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that this location belongs to.
      :param id_ [int] The ID of the location you wish to update
      :param model [LocationModel] The location you wish to update.
      :return LocationModel
    """
    def update_location(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/locations/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Validate the location against local requirements
    
    Returns validation information for this location.
      This API call is intended to compare this location against the currently known taxing authority rules and regulations,
      and provide information about what additional work is required to completely setup this location.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, FirmAdmin, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param companyId [int] The ID of the company that owns this location
      :param id_ [int] The primary key of this location
      :return LocationValidationModel
    """
    def validate_location(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/locations/{}/validate'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Adjust a MultiDocument transaction
    
    Adjusts the current MultiDocument transaction uniquely identified by this URL.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      When you adjust a transaction, that transaction's status is recorded as `Adjusted`.
      Both the revisions will be available for retrieval based on their code and ID numbers. Only transactions in Committed status can be reported on a tax filing by Avalara's Managed Returns Service.
      Transactions that have been previously reported to a tax authority by Avalara Managed Returns are considered locked and are no longer available for adjustments.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param code [string] The transaction code for this MultiDocument transaction
      :param type [DocumentType] The transaction type for this MultiDocument transaction (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :param model [AdjustMultiDocumentModel] The adjust request you wish to execute
      :return MultiDocumentModel
    """
    def adjust_multi_document_transaction(self, code, type, model, include=None):
        return requests.post('{}/api/v2/transactions/multidocument/{}/type/{}/adjust'.format(self.base_url, code, type),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Get audit information about a MultiDocument transaction
    
    Retrieve audit information about a MultiDocument transaction stored in AvaTax.
      The audit API retrieves audit information related to a specific MultiDocument transaction. This audit
      information includes the following:
      * The `code` of the MultiDocument transaction
      * The `type` of the MultiDocument transaction
      * The server timestamp representing the exact server time when the transaction was created
      * The server duration - how long it took to process this transaction
      * Whether exact API call details were logged
      * A reconstructed API call showing what the original create call looked like
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param code [string] The transaction code for this MultiDocument transaction
      :param type [DocumentType] The transaction type for this MultiDocument transaction (See DocumentType::* for a list of allowable values)
      :return AuditMultiDocumentModel
    """
    def audit_multi_document_transaction(self, code, type):
        return requests.get('{}/api/v2/transactions/multidocument/{}/type/{}/audit'.format(self.base_url, code, type),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Commit a MultiDocument transaction
    
    Marks a list of transactions by changing its status to `Committed`.
      Transactions that are committed are available to be reported to a tax authority by Avalara Managed Returns.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      Any changes made to a committed transaction will generate a transaction history.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, ProStoresOperator, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param model [CommitMultiDocumentModel] The commit request you wish to execute
      :return MultiDocumentModel
    """
    def commit_multi_document_transaction(self, model):
        return requests.post('{}/api/v2/transactions/multidocument/commit'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new MultiDocument transaction
    
    Records a new MultiDocument transaction in AvaTax.
      A traditional transaction requires exactly two parties: a seller and a buyer. MultiDocument transactions can
      involve a marketplace of vendors, each of which contributes some portion of the final transaction. Within
      a MultiDocument transaction, each individual buyer and seller pair are matched up and converted to a separate
      document. This separation of documents allows each seller to file their taxes separately.
      This API will report an error if you attempt to create a transaction when one already exists with the specified `code`.
      If you would like the API to automatically update the transaction when it already exists, please set the `allowAdjust`
      value to `true`.
      To generate a refund for a transaction, use the `RefundTransaction` API.
      The field `type` identifies the kind of transaction - for example, a sale, purchase, or refund. If you do not specify
      a `type` value, you will receive an estimate of type `SalesOrder`, which will not be recorded.
      The origin and destination locations for a transaction must be identified by either address or geocode. For address-based transactions, please
      provide addresses in the fields `line`, `city`, `region`, `country` and `postalCode`. For geocode-based transactions, please provide the geocode
      information in the fields `latitude` and `longitude`. If either `latitude` or `longitude` or both are null, the transaction will be calculated
      using the best available address location information.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * ForceTimeout - Simulates a timeout. This adds a 30 second delay and error to your API call. This can be used to test your code to ensure it can respond correctly in the case of a dropped connection.
      If you omit the `$include` parameter, the API will assume you want `Summary,Addresses`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param include [string] Specifies objects to include in the response after transaction is created
      :param model [CreateMultiDocumentModel] the multi document transaction model
      :return MultiDocumentModel
    """
    def create_multi_document_transaction(self, model, include=None):
        return requests.post('{}/api/v2/transactions/multidocument'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a MultiDocument transaction
    
    Get the current MultiDocument transaction identified by this URL.
      If this transaction was adjusted, the return value of this API will be the current transaction with this code.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param code [string] 
      :param type [DocumentType]  (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in the response after transaction is created
      :return MultiDocumentModel
    """
    def get_multi_document_transaction_by_code_and_type(self, code, type, include=None):
        return requests.get('{}/api/v2/transactions/multidocument/{}/type/{}'.format(self.base_url, code, type),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a MultiDocument transaction by ID
    
    Get the unique MultiDocument transaction identified by this URL.
      A traditional transaction requires exactly two parties: a seller and a buyer. MultiDocument transactions can
      involve a marketplace of vendors, each of which contributes some portion of the final transaction. Within
      a MultiDocument transaction, each individual buyer and seller pair are matched up and converted to a separate
      document. This separation of documents allows each seller to file their taxes separately.
      This endpoint retrieves the exact transaction identified by this ID number even if that transaction was later adjusted
      by using the `AdjustTransaction` endpoint.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param id_ [int] The unique ID number of the MultiDocument transaction to retrieve
      :param include [string] Specifies objects to include in the response after transaction is created
      :return MultiDocumentModel
    """
    def get_multi_document_transaction_by_id(self, id_, include=None):
        return requests.get('{}/api/v2/transactions/multidocument/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all MultiDocument transactions
    
    List all MultiDocument transactions within this account.
      This endpoint is limited to returning 1,000 MultiDocument transactions at a time. To retrieve more than 1,000 MultiDocument
      transactions, please use the pagination features of the API.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* documents
      :param include [string] Specifies objects to include in the response after transaction is created
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_multi_document_transactions(self, include=None):
        return requests.get('{}/api/v2/transactions/multidocument'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a refund for a MultiDocument transaction
    
    Create a refund for a MultiDocument transaction.
      A traditional transaction requires exactly two parties: a seller and a buyer. MultiDocument transactions can
      involve a marketplace of vendors, each of which contributes some portion of the final transaction. Within
      a MultiDocument transaction, each individual buyer and seller pair are matched up and converted to a separate
      document. This separation of documents allows each seller to file their taxes separately.
      The `RefundTransaction` API allows you to quickly and easily create a `ReturnInvoice` representing a refund
      for a previously created `SalesInvoice` transaction. You can choose to create a full or partial refund, and
      specify individual line items from the original sale for refund.
      The `RefundTransaction` API ensures that the tax amount you refund to the customer exactly matches the tax that
      was calculated during the original transaction, regardless of any changes to your company's configuration, rules,
      nexus, or any other setting.
      This API is intended to be a shortcut to allow you to quickly and accurately generate a refund for the following
      common refund scenarios:
      * A full refund of a previous sale
      * Refunding the tax that was charged on a previous sale, when the customer provides an exemption certificate after the purchase
      * Refunding one or more items (lines) from a previous sale
      * Granting a customer a percentage refund of a previous sale
      For more complex scenarios than the ones above, please use `CreateTransaction` with document type `ReturnInvoice` to
      create a custom refund transaction.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      If you omit the `$include` parameter, the API will assume you want `Summary,Addresses`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param code [string] The code of this MultiDocument transaction
      :param type [DocumentType] The type of this MultiDocument transaction (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in the response after transaction is created
      :param model [RefundTransactionModel] Information about the refund to create
      :return MultiDocumentModel
    """
    def refund_multi_document_transaction(self, code, type, model, include=None):
        return requests.post('{}/api/v2/transactions/multidocument/{}/type/{}/refund'.format(self.base_url, code, type),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Verify a MultiDocument transaction
    
    Verifies that the MultiDocument transaction uniquely identified by this URL matches certain expected values.
      If the transaction does not match these expected values, this API will return an error code indicating which value did not match.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param model [VerifyMultiDocumentModel] Information from your accounting system to verify against this MultiDocument transaction as it is stored in AvaTax
      :return MultiDocumentModel
    """
    def verify_multi_document_transaction(self, model):
        return requests.post('{}/api/v2/transactions/multidocument/verify'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Void a MultiDocument transaction
    
    Voids the current transaction uniquely identified by this URL.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      When you void a transaction, that transaction's status is recorded as `DocVoided`.
      Transactions that have been previously reported to a tax authority by Avalara Managed Returns Service are considered `locked`,
      and they are no longer available to be voided.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CSPTester, ProStoresOperator, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param code [string] The transaction code for this MultiDocument transaction
      :param type [DocumentType] The transaction type for this MultiDocument transaction (See DocumentType::* for a list of allowable values)
      :param model [VoidTransactionModel] The void request you wish to execute
      :return MultiDocumentModel
    """
    def void_multi_document_transaction(self, code, type, model):
        return requests.post('{}/api/v2/transactions/multidocument/{}/type/{}/void'.format(self.base_url, code, type),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new nexus
    
    Creates one or more new nexus declarations attached to this company.
      The concept of Nexus indicates a place where your company is legally obligated to collect and remit transactional
      taxes. The legal requirements for nexus may vary per country and per jurisdiction; please seek advice from your
      accountant or lawyer prior to declaring nexus.
      To create a nexus declaration for your company, you must first call the Definitions API `ListNexus` to obtain a
      list of Avalara-defined nexus. Once you have determined which nexus you wish to declare, you should customize
      only the user-selectable fields in this object.
      The user selectable fields for the nexus object are `companyId`, `effectiveDate`, `endDate`, `localNexusTypeId`,
      `taxId`, `nexusTypeId`, `hasPermanentEstablishment`, and `isSellerImporterOfRecord`.
      When calling `CreateNexus` or `UpdateNexus`, all values in your nexus object except for the user-selectable fields
      must match an Avalara-defined system nexus object. You can retrieve a list of Avalara-defined system nexus objects
      by calling `ListNexus`. If any data does not match, AvaTax may not recognize your nexus declaration.
      Please note that nexus changes may not take effect immediately and you should plan to update your nexus settings in advance
      of calculating tax for a location.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this nexus.
      :param model [NexusModel] The nexus you wish to create.
      :return NexusModel
    """
    def create_nexus(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/nexus'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Creates nexus for a list of addresses.
    
    This call is intended to simplify adding all applicable nexus to a company, for an address or addresses. Calling this
      API declares nexus for this company, for the list of addresses provided,
      for the date range provided. You may also use this API to extend effective date on an already-declared nexus.
      The concept of Nexus indicates a place where your company is legally obligated to collect and remit transactional
      taxes. The legal requirements for nexus may vary per country and per jurisdiction; please seek advice from your
      accountant or lawyer prior to declaring nexus.
      Note that not all fields within a nexus can be updated; Avalara publishes a list of all defined nexus at the
      '/api/v2/definitions/nexus' endpoint.
      You may only define nexus matching the official list of declared nexus.
      Please note that nexus changes may not take effect immediately and you should plan to update your nexus settings in advance
      of calculating tax for a location.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that will own this nexus.
      :param model [DeclareNexusByAddressModel] The nexus you wish to create.
      :return NexusByAddressModel
    """
    def declare_nexus_by_address(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/nexus/byaddress'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single nexus
    
    Marks the existing nexus object at this URL as deleted.
      The concept of Nexus indicates a place where your company is legally obligated to collect and remit transactional
      taxes. The legal requirements for nexus may vary per country and per jurisdiction; please seek advice from your
      accountant or lawyer prior to declaring nexus.
      Please note that nexus changes may not take effect immediately and you should plan to update your nexus settings in advance
      of calculating tax for a location.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this nexus.
      :param id_ [int] The ID of the nexus you wish to delete.
      :return ErrorDetail
    """
    def delete_nexus(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/nexus/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single nexus
    
    Get the nexus object identified by this URL.
      The concept of Nexus indicates a place where your company is legally obligated to collect and remit transactional
      taxes. The legal requirements for nexus may vary per country and per jurisdiction; please seek advice from your
      accountant or lawyer prior to declaring nexus.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns this nexus object
      :param id_ [int] The primary key of this nexus
      :return NexusModel
    """
    def get_nexus(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/nexus/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List company nexus related to a tax form
    
    Retrieves a list of nexus related to a tax form.
      The concept of Nexus indicates a place where your company is legally obligated to collect and remit transactional
      taxes. The legal requirements for nexus may vary per country and per jurisdiction; please seek advice from your
      accountant or lawyer prior to declaring nexus.
      This API is intended to provide useful information when examining a tax form. If you are about to begin filing
      a tax form, you may want to know whether you have declared nexus in all the jurisdictions related to that tax
      form in order to better understand how the form will be filled out.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns this nexus object
      :param formCode [string] The form code that we are looking up the nexus for
      :return NexusByTaxFormModel
    """
    def get_nexus_by_form_code(self, companyId, formCode):
        return requests.get('{}/api/v2/companies/{}/nexus/byform/{}'.format(self.base_url, companyId, formCode),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve nexus for this company
    
    List all nexus objects defined for this company.
      The concept of Nexus indicates a place where your company is legally obligated to collect and remit transactional
      taxes. The legal requirements for nexus may vary per country and per jurisdiction; please seek advice from your
      accountant or lawyer prior to declaring nexus.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns these nexus objects
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* streamlinedSalesTax, isSSTActive, taxAuthorityId
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_nexus_by_company(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/nexus'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all nexus
    
    Get multiple nexus objects across all companies.
      The concept of Nexus indicates a place where your company is legally obligated to collect and remit transactional
      taxes. The legal requirements for nexus may vary per country and per jurisdiction; please seek advice from your
      accountant or lawyer prior to declaring nexus.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* streamlinedSalesTax, isSSTActive, taxAuthorityId
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_nexus(self, include=None):
        return requests.get('{}/api/v2/nexus'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single nexus
    
    Replace the existing nexus declaration object at this URL with an updated object.
      The concept of Nexus indicates a place where your company is legally obligated to collect and remit transactional
      taxes. The legal requirements for nexus may vary per country and per jurisdiction; please seek advice from your
      accountant or lawyer prior to declaring nexus.
      To create a nexus declaration for your company, you must first call the Definitions API `ListNexus` to obtain a
      list of Avalara-defined nexus. Once you have determined which nexus you wish to declare, you should customize
      only the user-selectable fields in this object.
      The user selectable fields for the nexus object are `companyId`, `effectiveDate`, `endDate`, `localNexusTypeId`,
      `taxId`, `nexusTypeId`, `hasPermanentEstablishment`, and `isSellerImporterOfRecord`.
      When calling `CreateNexus` or `UpdateNexus`, all values in your nexus object except for the user-selectable fields
      must match an Avalara-defined system nexus object. You can retrieve a list of Avalara-defined system nexus objects
      by calling `ListNexus`. If any data does not match, AvaTax may not recognize your nexus declaration.
      Please note that nexus changes may not take effect immediately and you should plan to update your nexus settings in advance
      of calculating tax for a location.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that this nexus belongs to.
      :param id_ [int] The ID of the nexus you wish to update
      :param model [NexusModel] The nexus object you wish to update.
      :return NexusModel
    """
    def update_nexus(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/nexus/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Mark a single notification as dismissed.
    
    Marks the notification identified by this URL as dismissed.
      A notification is a message from Avalara that may have relevance to your business. You may want
      to regularly review notifications and then dismiss them when you are certain that you have addressed
      any relevant concerns raised by this notification.
      An example of a notification would be a message about new software, or a change to AvaTax that may
      affect you, or a potential issue with your company's tax profile.
      When you dismiss a notification, the notification will track the user and time when it was
      dismissed. You can then later review which employees of your company dismissed notifications to
      determine if they were resolved appropriately.
      A Global notification with null accountId and companyId cannot be dismissed and will expire within a given time span.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The id of the notification you wish to mark as dismissed.
      :return NotificationModel
    """
    def dismiss_notification(self, id_):
        return requests.put('{}/api/v2/notifications/{}/dismiss'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single notification.
    
    Retrieve a single notification by its unique ID number.
      A notification is a message from Avalara that may have relevance to your business. You may want
      to regularly review notifications and then dismiss them when you are certain that you have addressed
      any relevant concerns raised by this notification.
      An example of a notification would be a message about new software, or a change to AvaTax that may
      affect you, or a potential issue with your company's tax profile.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The id of the notification to retrieve.
      :return NotificationModel
    """
    def get_notification(self, id_):
        return requests.get('{}/api/v2/notifications/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all notifications.
    
    List all notifications.
      A notification is a message from Avalara that may have relevance to your business. You may want
      to regularly review notifications and then dismiss them when you are certain that you have addressed
      any relevant concerns raised by this notification.
      An example of a notification would be a message about new software, or a change to AvaTax that may
      affect you, or a potential issue with your company's tax profile.
      You may search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_notifications(self, include=None):
        return requests.get('{}/api/v2/notifications'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Request a new Avalara account
    
    This API is for use by partner onboarding services customers only.
      Avalara invites select partners to refer new customers to the AvaTax service using the onboarding features
      of AvaTax. These partners can create accounts for new customers using this API.
      Calling this API creates an account with the specified product subscriptions, but does not configure billing.
      The customer will receive information from Avalara about how to configure billing for their account.
      You should call this API when a customer has requested to begin using Avalara services.
      If the newly created account owner wishes, they can confirm that they have read and agree to the Avalara
      terms and conditions. If they do so, they can receive a license key as part of this API and their
      API will be created in `Active` status. If the customer has not yet read and accepted these terms and
      conditions, the account will be created in `New` status and they can receive a license key by logging
      onto the AvaTax website and reviewing terms and conditions online.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API is available by invitation only.
      * This API is available by invitation only. To request access to this feature, please speak to a business development manager and request access to [Onboarding:RequestNewAccount].
    
      :param model [NewAccountRequestModel] Information about the account you wish to create and the selected product offerings.
      :return NewAccountModel
    """
    def request_new_account(self, model):
        return requests.post('{}/api/v2/accounts/request'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Request a new entitilement to an existing customer
    
    This API is for use by partner onboarding services customers only. This will allow the partners to allow
      the add new entitlement to an existing customer
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API is available by invitation only.
      * This API is available by invitation only. To request access to this feature, please speak to a business development manager and request access to [Onboarding:RequestNewAccount].
    
      :param id_ [int] The avatax account id of the customer
      :param offer [string] The offer to be added to an already existing customer
      :return OfferModel
    """
    def request_new_entitlement(self, id_, offer):
        return requests.post('{}/api/v2/accounts/{}/entitlements/{}'.format(self.base_url, id_, offer),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new account
    
    # For Registrar Use Only
      This API is for use by Avalara Registrar administrative users only.
      Create a single new account object.
      When creating an account object you may attach subscriptions and users as part of the 'Create' call.
      ### Security Policies
      * This API requires one of the following user roles: FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param model [AccountModel] The account you wish to create.
      :return AccountModel
    """
    def create_account(self, model):
        return requests.post('{}/api/v2/accounts'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create new notifications.
    
    This API is available by invitation only.
      Create a single notification.
      A notification is a message from Avalara that may have relevance to your business. You may want
      to regularly review notifications and then dismiss them when you are certain that you have addressed
      any relevant concerns raised by this notification.
      A Global notification is a message which is directed to all the accounts and is set to expire within
      a certain time and cannot be dismissed by the user. Make accountId and companyId null to create a global notification.
      An example of a notification would be a message about new software, or a change to AvaTax that may
      affect you, or a potential issue with your company's tax profile.
      ### Security Policies
      * This API requires one of the following user roles: FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API is available by invitation only. To request access to this feature, please speak to a business development manager and request access to [NotificationsAPI:Create].
    
      :param model [NotificationModel] The notifications you wish to create.
      :return NotificationModel
    """
    def create_notifications(self, model):
        return requests.post('{}/api/v2/notifications'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new subscription
    
    This API is for use by Avalara Registrar administrative users only.
      Create one or more new subscription objects attached to this account.
      A 'subscription' indicates a licensed subscription to a named Avalara service.
      To request or remove subscriptions, please contact Avalara sales or your customer account manager.
      ### Security Policies
      * This API requires one of the following user roles: Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param accountId [int] The ID of the account that owns this subscription.
      :param model [SubscriptionModel] The subscription you wish to create.
      :return SubscriptionModel
    """
    def create_subscriptions(self, accountId, model):
        return requests.post('{}/api/v2/accounts/{}/subscriptions'.format(self.base_url, accountId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single account
    
    # For Registrar Use Only
      This API is for use by Avalara Registrar administrative users only.
      Delete an account.
      Deleting an account will delete all companies and all account level users attached to this account.
      ### Security Policies
      * This API requires the user role SystemAdmin.
    
      :param id_ [int] The ID of the account you wish to delete.
      :return ErrorDetail
    """
    def delete_account(self, id_):
        return requests.delete('{}/api/v2/accounts/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single notification.
    
    This API is available by invitation only.
      Delete the existing notification identified by this URL.
      A notification is a message from Avalara that may have relevance to your business. You may want
      to regularly review notifications and then dismiss them when you are certain that you have addressed
      any relevant concerns raised by this notification.
      An example of a notification would be a message about new software, or a change to AvaTax that may
      affect you, or a potential issue with your company's tax profile.
      ### Security Policies
      * This API requires one of the following user roles: FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API is available by invitation only. To request access to this feature, please speak to a business development manager and request access to [NotificationsAPI:Create].
    
      :param id_ [int] The id of the notification you wish to delete.
      :return ErrorDetail
    """
    def delete_notification(self, id_):
        return requests.delete('{}/api/v2/notifications/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single subscription
    
    # For Registrar Use Only
      This API is for use by Avalara Registrar administrative users only.
      Mark the existing account identified by this URL as deleted.
      ### Security Policies
      * This API requires one of the following user roles: Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param accountId [int] The ID of the account that owns this subscription.
      :param id_ [int] The ID of the subscription you wish to delete.
      :return ErrorDetail
    """
    def delete_subscription(self, accountId, id_):
        return requests.delete('{}/api/v2/accounts/{}/subscriptions/{}'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Reset a user's password programmatically
    
    # For Registrar Use Only
      This API is for use by Avalara Registrar administrative users only.
      Allows a system admin to reset the password for a specific user via the API.
      This API is only available for Avalara Registrar Admins, and can be used to reset the password of any
      user based on internal Avalara business processes.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
      * This API is available to Avalara system-level (registrar-level) users only.
    
      :param userId [int] The unique ID of the user whose password will be changed
      :param unmigrateFromAi [boolean] If user's password was migrated to AI, undo this.
      :param model [SetPasswordModel] The new password for this user
      :return string
    """
    def reset_password(self, userId, model, include=None):
        return requests.post('{}/api/v2/passwords/{}/reset'.format(self.base_url, userId),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single account
    
    # For Registrar Use Only
      This API is for use by Avalara Registrar administrative users only.
      Replace an existing account object with an updated account object.
      ### Security Policies
      * This API requires one of the following user roles: FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param id_ [int] The ID of the account you wish to update.
      :param model [AccountModel] The account object you wish to update.
      :return AccountModel
    """
    def update_account(self, id_, model):
        return requests.put('{}/api/v2/accounts/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single notification.
    
    This API is available by invitation only.
      Replaces the notification identified by this URL with a new notification.
      A notification is a message from Avalara that may have relevance to your business. You may want
      to regularly review notifications and then dismiss them when you are certain that you have addressed
      any relevant concerns raised by this notification.
      An example of a notification would be a message about new software, or a change to AvaTax that may
      affect you, or a potential issue with your company's tax profile.
      ### Security Policies
      * This API requires one of the following user roles: FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
      * This API is available by invitation only. To request access to this feature, please speak to a business development manager and request access to [NotificationsAPI:Create].
    
      :param id_ [int] The id of the notification you wish to update.
      :param model [NotificationModel] The notification object you wish to update.
      :return NotificationModel
    """
    def update_notification(self, id_, model):
        return requests.put('{}/api/v2/notifications/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single subscription
    
    # For Registrar Use Only
      This API is for use by Avalara Registrar administrative users only.
      Replace the existing subscription object at this URL with an updated object.
      A 'subscription' indicates a licensed subscription to a named Avalara service.
      To request or remove subscriptions, please contact Avalara sales or your customer account manager.
      All data from the existing object will be replaced with data in the object you PUT.
      To set a field's value to null, you may either set its value to null or omit that field from the object you post.
      ### Security Policies
      * This API requires one of the following user roles: Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param accountId [int] The ID of the account that this subscription belongs to.
      :param id_ [int] The ID of the subscription you wish to update
      :param model [SubscriptionModel] The subscription you wish to update.
      :return SubscriptionModel
    """
    def update_subscription(self, accountId, id_, model):
        return requests.put('{}/api/v2/accounts/{}/subscriptions/{}'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Download a report
    
    This API downloads the file associated with a report.
      If the report is not yet complete, you will receive a `ReportNotFinished` error. To check if a report is complete,
      use the `GetReport` API.
      Reports are run as asynchronous report tasks on the server. When complete, the report file will be available for download
      for up to 30 days after completion. To run an asynchronous report, you should follow these steps:
      * Begin a report by calling the report's Initiate API. There is a separate initiate API call for each report type.
      * In the result of the Initiate API, you receive back a report's `id` value.
      * Check the status of a report by calling `GetReport` and passing in the report's `id` value.
      * When a report's status is `Completed`, call `DownloadReport` to retrieve the file.
      This API works for all report types.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param id_ [int] The unique ID number of this report
      :return String
    """
    def download_report(self, id_):
        return requests.get('{}/api/v2/reports/{}/attachment'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single report
    
    Retrieve a single report by its unique ID number.
      Reports are run as asynchronous report tasks on the server. When complete, the report file will be available for download
      for up to 30 days after completion. To run an asynchronous report, you should follow these steps:
      * Begin a report by calling the report's Initiate API. There is a separate initiate API call for each report type.
      * In the result of the Initiate API, you receive back a report's `id` value.
      * Check the status of a report by calling `GetReport` and passing in the report's `id` value.
      * When a report's status is `Completed`, call `DownloadReport` to retrieve the file.
      This API call returns information about any report type.
    
      :param id_ [int] The unique ID number of the report to retrieve
      :return ReportModel
    """
    def get_report(self, id_):
        return requests.get('{}/api/v2/reports/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Initiate an ExportDocumentLine report task
    
    Begins running an `ExportDocumentLine` report task and returns the identity of the report.
      Reports are run as asynchronous report tasks on the server. When complete, the report file will be available for download
      for up to 30 days after completion. To run an asynchronous report, you should follow these steps:
      * Begin a report by calling the report's Initiate API. There is a separate initiate API call for each report type.
      * In the result of the Initiate API, you receive back a report's `id` value.
      * Check the status of a report by calling `GetReport` and passing in the report's `id` value.
      * When a report's status is `Completed`, call `DownloadReport` to retrieve the file.
      The `ExportDocumentLine` report produces information about invoice lines recorded within your account.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The unique ID number of the company to report on.
      :param model [ExportDocumentLineModel] Options that may be configured to customize the report.
      :return ReportModel
    """
    def initiate_export_document_line_report(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/reports/exportdocumentline/initiate'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all report tasks for account
    
    List all report tasks for your account.
      Reports are run as asynchronous report tasks on the server. When complete, the report file will be available for download
      for up to 30 days after completion. To run an asynchronous report, you should follow these steps:
      * Begin a report by calling the report's Initiate API. There is a separate initiate API call for each report type.
      * In the result of the Initiate API, you receive back a report's `id` value.
      * Check the status of a report by calling `GetReport` and passing in the report's `id` value.
      * When a report's status is `Completed`, call `DownloadReport` to retrieve the file.
      This API call returns information about all report types across your entire account.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The id of the company for which to get reports.
      :param pageKey [string] Provide a page key to retrieve the next page of results.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :return FetchResult
    """
    def list_reports(self, include=None):
        return requests.get('{}/api/v2/reports'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new setting
    
    Create one or more new setting objects attached to this company.
      The company settings system is a metadata system that you can use to store extra information
      about a company. Your integration or connector could use this data storage to keep track of
      preference information, reminders, or any other storage that would need to persist even if
      the customer uninstalls your application.
      A setting can refer to any type of data you need to remember about this company object.
      When creating this object, you may define your own `set`, `name`, and `value` parameters.
      To define your own values, please choose a `set` name that begins with `X-` to indicate an extension.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this setting.
      :param model [SettingModel] The setting you wish to create.
      :return SettingModel
    """
    def create_settings(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/settings'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single setting
    
    Mark the setting object at this URL as deleted.
      The company settings system is a metadata system that you can use to store extra information
      about a company. Your integration or connector could use this data storage to keep track of
      preference information, reminders, or any other storage that would need to persist even if
      the customer uninstalls your application.
      A setting can refer to any type of data you need to remember about this company object.
      When creating this object, you may define your own `set`, `name`, and `value` parameters.
      To define your own values, please choose a `set` name that begins with `X-` to indicate an extension.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, FirmAdmin, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this setting.
      :param id_ [int] The ID of the setting you wish to delete.
      :return ErrorDetail
    """
    def delete_setting(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/settings/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single setting
    
    Get a single setting object by its unique ID.
      The company settings system is a metadata system that you can use to store extra information
      about a company. Your integration or connector could use this data storage to keep track of
      preference information, reminders, or any other storage that would need to persist even if
      the customer uninstalls your application.
      A setting can refer to any type of data you need to remember about this company object.
      When creating this object, you may define your own `set`, `name`, and `value` parameters.
      To define your own values, please choose a `set` name that begins with `X-` to indicate an extension.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns this setting
      :param id_ [int] The primary key of this setting
      :return SettingModel
    """
    def get_setting(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/settings/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all settings for this company
    
    List all setting objects attached to this company.
      The company settings system is a metadata system that you can use to store extra information
      about a company. Your integration or connector could use this data storage to keep track of
      preference information, reminders, or any other storage that would need to persist even if
      the customer uninstalls your application.
      A setting can refer to any type of data you need to remember about this company object.
      When creating this object, you may define your own `set`, `name`, and `value` parameters.
      To define your own values, please choose a `set` name that begins with `X-` to indicate an extension.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns these settings
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_settings_by_company(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/settings'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all settings
    
    Get multiple setting objects across all companies.
      The company settings system is a metadata system that you can use to store extra information
      about a company. Your integration or connector could use this data storage to keep track of
      preference information, reminders, or any other storage that would need to persist even if
      the customer uninstalls your application.
      A setting can refer to any type of data you need to remember about this company object.
      When creating this object, you may define your own `set`, `name`, and `value` parameters.
      To define your own values, please choose a `set` name that begins with `X-` to indicate an extension.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_settings(self, include=None):
        return requests.get('{}/api/v2/settings'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single setting
    
    Replace the existing setting object at this URL with an updated object.
      The company settings system is a metadata system that you can use to store extra information
      about a company. Your integration or connector could use this data storage to keep track of
      preference information, reminders, or any other storage that would need to persist even if
      the customer uninstalls your application.
      A setting can refer to any type of data you need to remember about this company object.
      When creating this object, you may define your own `set`, `name`, and `value` parameters.
      To define your own values, please choose a `set` name that begins with `X-` to indicate an extension.
      All data from the existing object will be replaced with data in the object you `PUT`.
      To set a field's value to `null`, you may either set its value to `null` or omit that field from the object when calling update.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that this setting belongs to.
      :param id_ [int] The ID of the setting you wish to update
      :param model [SettingModel] The setting you wish to update.
      :return SettingModel
    """
    def update_setting(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/settings/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single subscription
    
    Get the subscription object identified by this URL.
      A 'subscription' indicates a licensed subscription to a named Avalara service.
      To request or remove subscriptions, please contact Avalara sales or your customer account manager.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param accountId [int] The ID of the account that owns this subscription
      :param id_ [int] The primary key of this subscription
      :return SubscriptionModel
    """
    def get_subscription(self, accountId, id_):
        return requests.get('{}/api/v2/accounts/{}/subscriptions/{}'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve subscriptions for this account
    
    List all subscription objects attached to this account.
      A 'subscription' indicates a licensed subscription to a named Avalara service.
      To request or remove subscriptions, please contact Avalara sales or your customer account manager.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param accountId [int] The ID of the account that owns these subscriptions
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* subscriptionDescription
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_subscriptions_by_account(self, accountId, include=None):
        return requests.get('{}/api/v2/accounts/{}/subscriptions'.format(self.base_url, accountId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all subscriptions
    
    Get multiple subscription objects across all accounts.
      A 'subscription' indicates a licensed subscription to a named Avalara service.
      To request or remove subscriptions, please contact Avalara sales or your customer account manager.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* subscriptionDescription
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_subscriptions(self, include=None):
        return requests.get('{}/api/v2/subscriptions'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new tax code
    
    Create one or more new taxcode objects attached to this company.
      A 'TaxCode' represents a uniquely identified type of product, good, or service.
      Avalara supports correct tax rates and taxability rules for all TaxCodes in all supported jurisdictions.
      If you identify your products by tax code in your 'Create Transacion' API calls, Avalara will correctly calculate tax rates and
      taxability rules for this product in all supported jurisdictions.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this tax code.
      :param model [TaxCodeModel] The tax code you wish to create.
      :return TaxCodeModel
    """
    def create_tax_codes(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/taxcodes'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single tax code
    
    Marks the existing TaxCode object at this URL as deleted.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this tax code.
      :param id_ [int] The ID of the tax code you wish to delete.
      :return ErrorDetail
    """
    def delete_tax_code(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/taxcodes/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single tax code
    
    Get the taxcode object identified by this URL.
      A 'TaxCode' represents a uniquely identified type of product, good, or service.
      Avalara supports correct tax rates and taxability rules for all TaxCodes in all supported jurisdictions.
      If you identify your products by tax code in your 'Create Transacion' API calls, Avalara will correctly calculate tax rates and
      taxability rules for this product in all supported jurisdictions.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns this tax code
      :param id_ [int] The primary key of this tax code
      :return TaxCodeModel
    """
    def get_tax_code(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/taxcodes/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve tax codes for this company
    
    List all taxcode objects attached to this company.
      A 'TaxCode' represents a uniquely identified type of product, good, or service.
      Avalara supports correct tax rates and taxability rules for all TaxCodes in all supported jurisdictions.
      If you identify your products by tax code in your 'Create Transacion' API calls, Avalara will correctly calculate tax rates and
      taxability rules for this product in all supported jurisdictions.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns these tax codes
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_tax_codes_by_company(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/taxcodes'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all tax codes
    
    Get multiple taxcode objects across all companies.
      A 'TaxCode' represents a uniquely identified type of product, good, or service.
      Avalara supports correct tax rates and taxability rules for all TaxCodes in all supported jurisdictions.
      If you identify your products by tax code in your 'Create Transacion' API calls, Avalara will correctly calculate tax rates and
      taxability rules for this product in all supported jurisdictions.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_tax_codes(self, include=None):
        return requests.get('{}/api/v2/taxcodes'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single tax code
    
    Replace the existing taxcode object at this URL with an updated object.
      A 'TaxCode' represents a uniquely identified type of product, good, or service.
      Avalara supports correct tax rates and taxability rules for all TaxCodes in all supported jurisdictions.
      If you identify your products by tax code in your 'Create Transacion' API calls, Avalara will correctly calculate tax rates and
      taxability rules for this product in all supported jurisdictions.
      All data from the existing object will be replaced with data in the object you PUT.
      To set a field's value to null, you may either set its value to null or omit that field from the object you post.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that this tax code belongs to.
      :param id_ [int] The ID of the tax code you wish to update
      :param model [TaxCodeModel] The tax code you wish to update.
      :return TaxCodeModel
    """
    def update_tax_code(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/taxcodes/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Build a multi-location tax content file
    
    Builds a tax content file containing information useful for a retail point-of-sale solution.
      Since tax rates may change based on decisions made by a variety of tax authorities, we recommend
      that users of this tax content API download new data every day. Many tax authorities may finalize
      decisions on tax changes at unexpected times and may make changes in response to legal issues or
      governmental priorities. Any tax content downloaded for future time periods is subject to change
      if tax rates or tax laws change.
      A TaxContent file contains a matrix of the taxes that would be charged when you sell any of your
      Items at any of your Locations. To create items, use `CreateItems()`. To create locations, use
      `CreateLocations()`. The file is built by looking up the tax profile for your location and your
      item and calculating taxes for each in turn. To include a custom `TaxCode` in this tax content
      file, first create the custom tax code using `CreateTaxCodes()` to create the custom tax code,
      then use `CreateItems()` to create an item that uses the custom tax code.
      This data file can be customized for specific partner devices and usage conditions.
      The result of this API is the file you requested in the format you requested using the `responseType` field.
      This API builds the file on demand, and is limited to files with no more than 7500 scenarios. To build a tax content
      file for a single location at a time, please use `BuildTaxContentFileForLocation`.
      NOTE: This API does not work for Tennessee tax holiday scenarios.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param model [PointOfSaleDataRequestModel] Parameters about the desired file format and report format, specifying which company, locations and TaxCodes to include.
      :return String
    """
    def build_tax_content_file(self, model):
        return requests.post('{}/api/v2/pointofsaledata/build'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Build a tax content file for a single location
    
    Builds a tax content file containing information useful for a retail point-of-sale solution.
      Since tax rates may change based on decisions made by a variety of tax authorities, we recommend
      that users of this tax content API download new data every day. Many tax authorities may finalize
      decisions on tax changes at unexpected times and may make changes in response to legal issues or
      governmental priorities. Any tax content downloaded for future time periods is subject to change
      if tax rates or tax laws change.
      A TaxContent file contains a matrix of the taxes that would be charged when you sell any of your
      Items at any of your Locations. To create items, use `CreateItems()`. To create locations, use
      `CreateLocations()`. The file is built by looking up the tax profile for your location and your
      item and calculating taxes for each in turn. To include a custom `TaxCode` in this tax content
      file, first create the custom tax code using `CreateTaxCodes()` to create the custom tax code,
      then use `CreateItems()` to create an item that uses the custom tax code.
      This data file can be customized for specific partner devices and usage conditions.
      The result of this API is the file you requested in the format you requested using the `responseType` field.
      This API builds the file on demand, and is limited to files with no more than 7500 scenarios. To build a tax content
      file for a multiple locations in a single file, please use `BuildTaxContentFile`.
      NOTE: This API does not work for Tennessee tax holiday scenarios.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyId [int] The ID number of the company that owns this location.
      :param id_ [int] The ID number of the location to retrieve point-of-sale data.
      :param date [datetime] The date for which point-of-sale data would be calculated (today by default)
      :param format [PointOfSaleFileType] The format of the file (JSON by default) (See PointOfSaleFileType::* for a list of allowable values)
      :param partnerId [PointOfSalePartnerId] If specified, requests a custom partner-formatted version of the file. (See PointOfSalePartnerId::* for a list of allowable values)
      :param includeJurisCodes [boolean] When true, the file will include jurisdiction codes in the result.
      :return String
    """
    def build_tax_content_file_for_location(self, companyId, id_, include=None):
        return requests.get('{}/api/v2/companies/{}/locations/{}/pointofsaledata'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Download a file listing tax rates by postal code
    
    Download a CSV file containing all five digit postal codes in the United States and their sales
      and use tax rates for tangible personal property.
      Since tax rates may change based on decisions made by a variety of tax authorities, we recommend
      that users of this tax content API download new data every day. Many tax authorities may finalize
      decisions on tax changes at unexpected times and may make changes in response to legal issues or
      governmental priorities. Any tax content downloaded for future time periods is subject to change
      if tax rates or tax laws change.
      This rates file is intended to be used as a default for tax calculation when your software cannot
      call the `CreateTransaction` API call. When using this file, your software will be unable to
      handle complex tax rules such as:
      * Zip+4 - This tax file contains five digit zip codes only.
      * Different product types - This tax file contains tangible personal property tax rates only.
      * Mixed sourcing - This tax file cannot be used to resolve origin-based taxes.
      * Threshold-based taxes - This tax file does not contain information about thresholds.
      If you use this file to provide default tax rates, please ensure that your software calls `CreateTransaction`
      to reconcile the actual transaction and determine the difference between the estimated general tax
      rate and the final transaction tax.
      The file provided by this API is in CSV format with the following columns:
      * ZIP_CODE - The five digit zip code for this record.
      * STATE_ABBREV - A valid two character US state abbreviation for this record. Zip codes may span multiple states.
      * COUNTY_NAME - A valid county name for this record. Zip codes may span multiple counties.
      * CITY_NAME - A valid city name for this record. Zip codes may span multiple cities.
      * STATE_SALES_TAX - The state component of the sales tax rate.
      * STATE_USE_TAX - The state component of the use tax rate.
      * COUNTY_SALES_TAX - The county component of the sales tax rate.
      * COUNTY_USE_TAX - The county component of the use tax rate.
      * CITY_SALES_TAX - The city component of the sales tax rate.
      * CITY_USE_TAX - The city component of the use tax rate.
      * TOTAL_SALES_TAX - The total tax rate for sales tax for this postal code. This value may not equal the sum of the state/county/city due to special tax jurisdiction rules.
      * TOTAL_USE_TAX - The total tax rate for use tax for this postal code. This value may not equal the sum of the state/county/city due to special tax jurisdiction rules.
      * TAX_SHIPPING_ALONE - This column contains 'Y' if shipping is taxable.
      * TAX_SHIPPING_AND_HANDLING_TOGETHER - This column contains 'Y' if shipping and handling are taxable when sent together.
      For more detailed tax content, please use the `BuildTaxContentFile` API which allows usage of exact items and exact locations.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param date [datetime] The date for which point-of-sale data would be calculated (today by default). Example input: 2016-12-31
      :param region [string] A two character region code which limits results to a specific region.
      :return String
    """
    def download_tax_rates_by_zip_code(self, date, include=None):
        return requests.get('{}/api/v2/taxratesbyzipcode/download/{}'.format(self.base_url, date),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new tax rule
    
    Create one or more custom tax rules attached to this company.
      A tax rule represents a rule that changes the default AvaTax behavior for a product or jurisdiction. Custom tax rules
      can be used to change the taxability of an item, to change the tax base of an item, or to change the tax rate
      charged when selling an item. Tax rules can also change tax behavior depending on the `entityUseCode` value submitted
      with the transaction.
      You can create custom tax rules to customize the behavior of AvaTax to match specific rules that are custom to your
      business. If you have obtained a ruling from a tax auditor that requires custom tax calculations, you can use
      custom tax rules to redefine the behavior for your company or item.
      Please use custom tax rules carefully and ensure that these tax rules match the behavior agreed upon with your
      auditor, legal representative, and accounting team.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this tax rule.
      :param model [TaxRuleModel] The tax rule you wish to create.
      :return TaxRuleModel
    """
    def create_tax_rules(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/taxrules'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single tax rule
    
    Mark the custom tax rule identified by this URL as deleted.
      A tax rule represents a rule that changes the default AvaTax behavior for a product or jurisdiction. Custom tax rules
      can be used to change the taxability of an item, to change the tax base of an item, or to change the tax rate
      charged when selling an item. Tax rules can also change tax behavior depending on the `entityUseCode` value submitted
      with the transaction.
      You can create custom tax rules to customize the behavior of AvaTax to match specific rules that are custom to your
      business. If you have obtained a ruling from a tax auditor that requires custom tax calculations, you can use
      custom tax rules to redefine the behavior for your company or item.
      Please use custom tax rules carefully and ensure that these tax rules match the behavior agreed upon with your
      auditor, legal representative, and accounting team.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that owns this tax rule.
      :param id_ [int] The ID of the tax rule you wish to delete.
      :return ErrorDetail
    """
    def delete_tax_rule(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/taxrules/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single tax rule
    
    Get the taxrule object identified by this URL.
      A tax rule represents a rule that changes the default AvaTax behavior for a product or jurisdiction. Custom tax rules
      can be used to change the taxability of an item, to change the tax base of an item, or to change the tax rate
      charged when selling an item. Tax rules can also change tax behavior depending on the `entityUseCode` value submitted
      with the transaction.
      You can create custom tax rules to customize the behavior of AvaTax to match specific rules that are custom to your
      business. If you have obtained a ruling from a tax auditor that requires custom tax calculations, you can use
      custom tax rules to redefine the behavior for your company or item.
      Please use custom tax rules carefully and ensure that these tax rules match the behavior agreed upon with your
      auditor, legal representative, and accounting team.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns this tax rule
      :param id_ [int] The primary key of this tax rule
      :return TaxRuleModel
    """
    def get_tax_rule(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/taxrules/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve tax rules for this company
    
    List all taxrule objects attached to this company.
      A tax rule represents a rule that changes the default AvaTax behavior for a product or jurisdiction. Custom tax rules
      can be used to change the taxability of an item, to change the tax base of an item, or to change the tax rate
      charged when selling an item. Tax rules can also change tax behavior depending on the `entityUseCode` value submitted
      with the transaction.
      You can create custom tax rules to customize the behavior of AvaTax to match specific rules that are custom to your
      business. If you have obtained a ruling from a tax auditor that requires custom tax calculations, you can use
      custom tax rules to redefine the behavior for your company or item.
      Please use custom tax rules carefully and ensure that these tax rules match the behavior agreed upon with your
      auditor, legal representative, and accounting team.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param companyId [int] The ID of the company that owns these tax rules
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* taxCode, rateTypeCode, taxTypeGroup, taxSubType
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_tax_rules(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/taxrules'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all tax rules
    
    Get multiple taxrule objects across all companies.
      A tax rule represents a rule that changes the default AvaTax behavior for a product or jurisdiction. Custom tax rules
      can be used to change the taxability of an item, to change the tax base of an item, or to change the tax rate
      charged when selling an item. Tax rules can also change tax behavior depending on the `entityUseCode` value submitted
      with the transaction.
      You can create custom tax rules to customize the behavior of AvaTax to match specific rules that are custom to your
      business. If you have obtained a ruling from a tax auditor that requires custom tax calculations, you can use
      custom tax rules to redefine the behavior for your company or item.
      Please use custom tax rules carefully and ensure that these tax rules match the behavior agreed upon with your
      auditor, legal representative, and accounting team.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* taxCode, rateTypeCode, taxTypeGroup, taxSubType
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_tax_rules(self, include=None):
        return requests.get('{}/api/v2/taxrules'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single tax rule
    
    Replace the existing custom tax rule object at this URL with an updated object.
      A tax rule represents a rule that changes the default AvaTax behavior for a product or jurisdiction. Custom tax rules
      can be used to change the taxability of an item, to change the tax base of an item, or to change the tax rate
      charged when selling an item. Tax rules can also change tax behavior depending on the `entityUseCode` value submitted
      with the transaction.
      You can create custom tax rules to customize the behavior of AvaTax to match specific rules that are custom to your
      business. If you have obtained a ruling from a tax auditor that requires custom tax calculations, you can use
      custom tax rules to redefine the behavior for your company or item.
      Please use custom tax rules carefully and ensure that these tax rules match the behavior agreed upon with your
      auditor, legal representative, and accounting team.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyId [int] The ID of the company that this tax rule belongs to.
      :param id_ [int] The ID of the tax rule you wish to update
      :param model [TaxRuleModel] The tax rule you wish to update.
      :return TaxRuleModel
    """
    def update_tax_rule(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/taxrules/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Add lines to an existing unlocked transaction
    
    Add lines to an existing unlocked transaction.
       The `AddLines` API allows you to add additional transaction lines to existing transaction, so that customer will
       be able to append multiple calls together and form an extremely large transaction. If customer does not specify line number
       in the lines to be added, a new random Guid string will be generated for line number. If customer are not satisfied with
       the line number for the transaction lines, they can turn on the renumber switch to have REST v2 automatically renumber all
       transaction lines for them, in this case, the line number becomes: "1", "2", "3", ...
       A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
       sales, purchases, inventory transfer, and returns (also called refunds).
       You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
       * Lines
       * Details (implies lines)
       * Summary (implies details)
       * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
       If you omit the `$include` parameter, the API will assume you want `Summary,Addresses`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param include [string] Specifies objects to include in the response after transaction is created
      :param model [AddTransactionLineModel] information about the transaction and lines to be added
      :return TransactionModel
    """
    def add_lines(self, model, include=None):
        return requests.post('{}/api/v2/companies/transactions/lines/add'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Correct a previously created transaction
    
    Replaces the current transaction uniquely identified by this URL with a new transaction.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      When you adjust a committed transaction, the original transaction will be updated with the status code `Adjusted`, and
      both revisions will be available for retrieval based on their code and ID numbers.
      Only transactions in `Committed` status are reported by Avalara Managed Returns.
      Transactions that have been previously reported to a tax authority by Avalara Managed Returns are considered `locked` and are
      no longer available for adjustments.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to adjust
      :param documentType [DocumentType] (Optional): The document type of the transaction to adjust. (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :param model [AdjustTransactionModel] The adjustment you wish to make
      :return TransactionModel
    """
    def adjust_transaction(self, companyCode, transactionCode, model, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/adjust'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Get audit information about a transaction
    
    Retrieve audit information about a transaction stored in AvaTax.
      The `AuditTransaction` API retrieves audit information related to a specific transaction. This audit
      information includes the following:
      * The `CompanyId` of the company that created the transaction
      * The server timestamp representing the exact server time when the transaction was created
      * The server duration - how long it took to process this transaction
      * Whether exact API call details were logged
      * A reconstructed API call showing what the original CreateTransaction call looked like
      This API can be used to examine information about a previously created transaction.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The code identifying the company that owns this transaction
      :param transactionCode [string] The code identifying the transaction
      :return AuditTransactionModel
    """
    def audit_transaction(self, companyCode, transactionCode):
        return requests.get('{}/api/v2/companies/{}/transactions/{}/audit'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Get audit information about a transaction
    
    Retrieve audit information about a transaction stored in AvaTax.
      The `AuditTransaction` API retrieves audit information related to a specific transaction. This audit
      information includes the following:
      * The `CompanyId` of the company that created the transaction
      * The server timestamp representing the exact server time when the transaction was created
      * The server duration - how long it took to process this transaction
      * Whether exact API call details were logged
      * A reconstructed API call showing what the original CreateTransaction call looked like
      This API can be used to examine information about a previously created transaction.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The code identifying the company that owns this transaction
      :param transactionCode [string] The code identifying the transaction
      :param documentType [DocumentType] The document type of the original transaction (See DocumentType::* for a list of allowable values)
      :return AuditTransactionModel
    """
    def audit_transaction_with_type(self, companyCode, transactionCode, documentType):
        return requests.get('{}/api/v2/companies/{}/transactions/{}/types/{}/audit'.format(self.base_url, companyCode, transactionCode, documentType),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Lock a set of documents
    
    This API is available by invitation only.
      Lock a set of transactions uniquely identified by DocumentIds provided. This API allows locking multiple documents at once.
      After this API call succeeds, documents will be locked and can't be voided.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      ### Security Policies
      * This API requires the user role Compliance Root User.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
      * This API is available by invitation only.<br />*Exempt security roles*: ComplianceRootUser, ComplianceAdmin, ComplianceUser, TechnicalSupportAdmin, TechnicalSupportUser.
    
      :param model [BulkLockTransactionModel] bulk lock request
      :return BulkLockTransactionResult
    """
    def bulk_lock_transaction(self, model):
        return requests.post('{}/api/v2/transactions/lock'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Change a transaction's code
    
    Renames a transaction uniquely identified by this URL by changing its `code` value.
      This API is available as long as the transaction is in `saved` or `posted` status. When a transaction
      is `committed`, it can be modified by using the [AdjustTransaction](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Transactions/AdjustTransaction/) method.
      After this API call succeeds, the transaction will have a new URL matching its new `code`.
      If you have more than one document with the same `code`, specify the `documentType` parameter to choose between them.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, ProStoresOperator, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro, AvaTaxST.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to change
      :param documentType [DocumentType] (Optional): The document type of the transaction to change document code. If not provided, the default is SalesInvoice. (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :param model [ChangeTransactionCodeModel] The code change request you wish to execute
      :return TransactionModel
    """
    def change_transaction_code(self, companyCode, transactionCode, model, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/changecode'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Commit a transaction for reporting
    
    Marks a transaction by changing its status to `Committed`.
      Transactions that are committed are available to be reported to a tax authority by Avalara Managed Returns.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      If you have more than one document with the same `code`, specify the `documentType` parameter to choose between them.
      Any changes made to a committed transaction will generate a transaction history.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, ProStoresOperator, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to commit
      :param documentType [DocumentType] (Optional): The document type of the transaction to commit. If not provided, the default is SalesInvoice. (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :param model [CommitTransactionModel] The commit request you wish to execute
      :return TransactionModel
    """
    def commit_transaction(self, companyCode, transactionCode, model, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/commit'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create or adjust a transaction
    
    Records a new transaction or adjust an existing transaction in AvaTax.
      The `CreateOrAdjustTransaction` endpoint is used to create a new transaction or update an existing one. This API
      can help you create an idempotent service that creates transactions
      If there exists a transaction identified by code, the original transaction will be adjusted by using the meta data
      in the input transaction.
      The `CreateOrAdjustTransaction` API cannot modify any transaction that has been reported to a tax authority using
      the Avalara Managed Returns Service or any other tax filing service. If you call this API to attempt to modify
      a transaction that has been reported on a tax filing, you will receive the error `CannotModifyLockedTransaction`.
      To generate a refund for a transaction, use the `RefundTransaction` API.
      If you don't specify the field `type` in your request, you will get an estimate of type `SalesOrder`, which will not be recorded in the database.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * ForceTimeout - Simulates a timeout. This adds a 30 second delay and error to your API call. This can be used to test your code to ensure it can respond correctly in the case of a dropped connection.
      If you omit the `$include` parameter, the API will assume you want `Summary,Addresses`.
      NOTE: Avoid using the following strings in your transaction codes as they are encoding strings and will be interpreted differently:
      * \_-ava2f-\_
      * \_-ava2b-\_
      * \_-ava3f-\_
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param include [string] Specifies objects to include in the response after transaction is created
      :param model [CreateOrAdjustTransactionModel] The transaction you wish to create or adjust
      :return TransactionModel
    """
    def create_or_adjust_transaction(self, model, include=None):
        return requests.post('{}/api/v2/transactions/createoradjust'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new transaction
    
    Records a new transaction in AvaTax.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      The `CreateTransaction` endpoint uses the tax profile of your company to identify the correct tax rules
      and rates to apply to all line items in this transaction. The end result will be the total tax calculated by AvaTax based on your
      company's configuration and the data provided in this API call.
      The `CreateTransaction` API will report an error if a committed transaction already exists with the same `code`. To
      avoid this error, use the `CreateOrAdjustTransaction` API - it will create the transaction if it does not exist, or
      update it if it does exist.
      To generate a refund for a transaction, use the `RefundTransaction` API.
      The field `type` identifies the kind of transaction - for example, a sale, purchase, or refund. If you do not specify
      a `type` value, you will receive an estimate of type `SalesOrder`, which will not be recorded.
      The origin and destination locations for a transaction must be identified by either address or geocode. For address-based transactions, please
      provide addresses in the fields `line`, `city`, `region`, `country` and `postalCode`. For geocode-based transactions, please provide the geocode
      information in the fields `latitude` and `longitude`. If either `latitude` or `longitude` or both are null, the transaction will be calculated
      using the best available address location information.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * ForceTimeout - Simulates a timeout. This adds a 30 second delay and error to your API call. This can be used to test your code to ensure it can respond correctly in the case of a dropped connection.
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      If you omit the `$include` parameter, the API will assume you want `Summary,Addresses`.
      NOTE: Avoid using the following strings in your transaction codes as they are encoding strings and will be interpreted differently:
      * \_-ava2f-\_
      * \_-ava2b-\_
      * \_-ava3f-\_
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param include [string] Specifies objects to include in the response after transaction is created
      :param model [CreateTransactionModel] The transaction you wish to create
      :return TransactionModel
    """
    def create_transaction(self, model, include=None):
        return requests.post('{}/api/v2/transactions/create'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Remove lines from an existing unlocked transaction
    
    Remove lines to an existing unlocked transaction.
       The `DeleteLines` API allows you to remove transaction lines from existing unlocked transaction, so that customer will
       be able to delete transaction lines and adjust original transaction the way they like
       A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
       sales, purchases, inventory transfer, and returns (also called refunds).
       You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
       * Lines
       * Details (implies lines)
       * Summary (implies details)
       * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
       If you omit the `$include` parameter, the API will assume you want `Summary,Addresses`.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param include [string] Specifies objects to include in the response after transaction is created
      :param model [RemoveTransactionLineModel] information about the transaction and lines to be removed
      :return TransactionModel
    """
    def delete_lines(self, model, include=None):
        return requests.post('{}/api/v2/companies/transactions/lines/delete'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single transaction by code
    
    Get the current transaction identified by this company code, transaction code, and document type.
      A transaction is uniquely identified by `companyCode`, `code` (often called Transaction Code), and `documentType`.
      For compatibility purposes, when this API finds multiple transactions with the same transaction code, and if you have not specified
      the `type` parameter to this API, it will default to selecting the `SalesInvoices` transaction. To change this behavior, use the
      optional `documentType` parameter to specify the specific document type you wish to find.
      If this transaction was adjusted, the return value of this API will be the current transaction with this code.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to retrieve
      :param documentType [DocumentType] (Optional): The document type of the transaction to retrieve (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :return TransactionModel
    """
    def get_transaction_by_code(self, companyCode, transactionCode, include=None):
        return requests.get('{}/api/v2/companies/{}/transactions/{}'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single transaction by code
    
    DEPRECATED: Please use the `GetTransactionByCode` API instead.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to retrieve
      :param documentType [DocumentType] The transaction type to retrieve (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :return TransactionModel
    """
    def get_transaction_by_code_and_type(self, companyCode, transactionCode, documentType, include=None):
        return requests.get('{}/api/v2/companies/{}/transactions/{}/types/{}'.format(self.base_url, companyCode, transactionCode, documentType),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single transaction by ID
    
    Get the unique transaction identified by this URL.
      This endpoint retrieves the exact transaction identified by this ID number even if that transaction was later adjusted
      by using the `AdjustTransaction` endpoint.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param id_ [int] The unique ID number of the transaction to retrieve
      :param include [string] Specifies objects to include in this fetch call
      :return TransactionModel
    """
    def get_transaction_by_id(self, id_, include=None):
        return requests.get('{}/api/v2/transactions/{}'.format(self.base_url, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all transactions
    
    List all transactions attached to this company.
      This endpoint is limited to returning 1,000 transactions at a time maximum.
      When listing transactions, you must specify a `date` range filter. If you do not specify a `$filter` that includes a `date` field
      criteria, the query will default to looking at only those transactions with `date` in the past 30 days.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, ProStoresOperator, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param dataSourceId [int] Optionally filter transactions to those from a specific data source.
      :param include [string] Specifies objects to include in this fetch call
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).<br />*Not filterable:* totalDiscount, lines, addresses, locationTypes, summary, taxDetailsByTaxType, parameters, messages, invoiceMessages, isFakeTransaction
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_transactions_by_company(self, companyCode, include=None):
        return requests.get('{}/api/v2/companies/{}/transactions'.format(self.base_url, companyCode),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Lock a single transaction
    
    Lock a transaction uniquely identified by this URL.
      This API is mainly used for connector developer to simulate what happens when Returns product locks a document.
      After this API call succeeds, the document will be locked and can't be voided or adjusted.
      This API is only available to customers in Sandbox with AvaTaxPro subscription. On production servers, this API is available by invitation only.
      If you have more than one document with the same `code`, specify the `documentType` parameter to choose between them.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Returns* (at least one of): Mrs, MRSComplianceManager, AvaTaxCsp.<br />*Firm Managed* (for accounts managed by a firm): ARA, ARAManaged.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to lock
      :param documentType [DocumentType] (Optional): The document type of the transaction to lock. If not provided, the default is SalesInvoice. (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :param model [LockTransactionModel] The lock request you wish to execute
      :return TransactionModel
    """
    def lock_transaction(self, companyCode, transactionCode, model, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/lock'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a refund for a transaction
    
    Create a refund for a transaction.
      The `RefundTransaction` API allows you to quickly and easily create a `ReturnInvoice` representing a refund
      for a previously created `SalesInvoice` transaction. You can choose to create a full or partial refund, and
      specify individual line items from the original sale for refund.
      The `RefundTransaction` API ensures that the tax amount you refund to the customer exactly matches the tax that
      was calculated during the original transaction, regardless of any changes to your company's configuration, rules,
      nexus, or any other setting.
      This API is intended to be a shortcut to allow you to quickly and accurately generate a refund for the following
      common refund scenarios:
      * A full refund of a previous sale
      * Refunding the tax that was charged on a previous sale, when the customer provides an exemption certificate after the purchase
      * Refunding one or more items (lines) from a previous sale
      * Granting a customer a percentage refund of a previous sale
      For more complex scenarios than the ones above, please use `CreateTransaction` with document type `ReturnInvoice` to
      create a custom refund transaction.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      If you omit the `$include` parameter, the API will assume you want `Summary,Addresses`.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The code of the company that made the original sale
      :param transactionCode [string] The transaction code of the original sale
      :param include [string] Specifies objects to include in the response after transaction is created
      :param documentType [DocumentType] (Optional): The document type of the transaction to refund. If not provided, the default is SalesInvoice. (See DocumentType::* for a list of allowable values)
      :param useTaxDateOverride [boolean] (Optional): If set to true, processes refund using taxDateOverride rather than taxAmountOverride (Note: taxAmountOverride is not allowed for SST states).
      :param model [RefundTransactionModel] Information about the refund to create
      :return TransactionModel
    """
    def refund_transaction(self, companyCode, transactionCode, model, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/refund'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Perform multiple actions on a transaction
    
    Performs one or more actions against the current transaction uniquely identified by this URL.
      The `SettleTransaction` API call can perform the work of `ChangeCode`, `VerifyTransaction`, and `CommitTransaction`.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      If you have more than one document with the same `code`, specify the `documentType` parameter to choose between them.
      This API is available for users who want to execute more than one action at a time.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, ProStoresOperator, SSTAdmin, TechnicalSupportAdmin.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to settle
      :param documentType [DocumentType] (Optional): The document type of the transaction to settle. If not provided, the default is SalesInvoice. (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :param model [SettleTransactionModel] The data from an external system to reconcile against AvaTax
      :return TransactionModel
    """
    def settle_transaction(self, companyCode, transactionCode, model, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/settle'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Uncommit a transaction for reporting
    
    Adjusts a transaction by changing it to an uncommitted status.
      Transactions that have been previously reported to a tax authority by Avalara Managed Returns are considered `locked` and are
      no longer available to be uncommitted.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to Uncommit
      :param documentType [DocumentType] (Optional): The document type of the transaction to Uncommit. If not provided, the default is SalesInvoice. (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :return TransactionModel
    """
    def uncommit_transaction(self, companyCode, transactionCode, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/uncommit'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Unvoids a transaction
    
    Unvoids a voided transaction
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to commit
      :param documentType [DocumentType] (Optional): The document type of the transaction to commit. If not provided, the default is SalesInvoice. (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :return TransactionModel
    """
    def unvoid_transaction(self, companyCode, transactionCode, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/unvoid'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Verify a transaction
    
    Verifies that the transaction uniquely identified by this URL matches certain expected values.
      If the transaction does not match these expected values, this API will return an error code indicating which value did not match.
      If you have more than one document with the same `code`, specify the `documentType` parameter to choose between them.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, CSPTester, ProStoresOperator, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to settle
      :param documentType [DocumentType] (Optional): The document type of the transaction to verify. If not provided, the default is SalesInvoice. (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :param model [VerifyTransactionModel] The data from an external system to reconcile against AvaTax
      :return TransactionModel
    """
    def verify_transaction(self, companyCode, transactionCode, model, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/verify'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Void a transaction
    
    Voids the current transaction uniquely identified by this URL.
      A transaction represents a unique potentially taxable action that your company has recorded, and transactions include actions like
      sales, purchases, inventory transfer, and returns (also called refunds).
      When you void a transaction, that transaction's status is recorded as `DocVoided`.
      If you have more than one document with the same `code`, specify the `documentType` parameter to choose between them.
      Transactions that have been previously reported to a tax authority by Avalara Managed Returns are no longer available to be voided.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * Lines
      * Details (implies lines)
      * Summary (implies details)
      * Addresses
      * SummaryOnly (omit lines and details - reduces API response size)
      * LinesOnly (omit details - reduces API response size)
      * TaxDetailsByTaxType - Includes the aggregated tax, exempt tax, taxable and non-taxable for each tax type returned in the transaction summary.
      NOTE: If your companyCode or transactionCode contains any of these characters /, + or ? please use the following encoding before making a request:
      * Replace '/' with '\_-ava2f-\_' For example: document/Code becomes document_-ava2f-_Code
      * Replace '+' with '\_-ava2b-\_' For example: document+Code becomes document_-ava2b-_Code
      * Replace '?' with '\_-ava3f-\_' For example: document?Code becomes document_-ava3f-_Code
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, CompanyAdmin, CSPTester, ProStoresOperator, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaTaxPro.
    
      :param companyCode [string] The company code of the company that recorded this transaction
      :param transactionCode [string] The transaction code to void
      :param documentType [DocumentType] (Optional): The document type of the transaction to void. If not provided, the default is SalesInvoice. (See DocumentType::* for a list of allowable values)
      :param include [string] Specifies objects to include in this fetch call
      :param model [VoidTransactionModel] The void request you wish to execute. To void a transaction the code must be set to 'DocVoided'
      :return TransactionModel
    """
    def void_transaction(self, companyCode, transactionCode, model, include=None):
        return requests.post('{}/api/v2/companies/{}/transactions/{}/void'.format(self.base_url, companyCode, transactionCode),
                               auth=self.auth, headers=self.client_header, params=include, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create a new UPC
    
    Create one or more new UPC objects attached to this company.
      A UPC represents a single UPC code in your catalog and matches this product to the tax code identified by this UPC.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaUpc.
    
      :param companyId [int] The ID of the company that owns this UPC.
      :param model [UPCModel] The UPC you wish to create.
      :return UPCModel
    """
    def create_u_p_cs(self, companyId, model):
        return requests.post('{}/api/v2/companies/{}/upcs'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single UPC
    
    Marks the UPC object identified by this URL as deleted.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaUpc.
    
      :param companyId [int] The ID of the company that owns this UPC.
      :param id_ [int] The ID of the UPC you wish to delete.
      :return ErrorDetail
    """
    def delete_u_p_c(self, companyId, id_):
        return requests.delete('{}/api/v2/companies/{}/upcs/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single UPC
    
    Get the UPC object identified by this URL.
      A UPC represents a single UPC code in your catalog and matches this product to the tax code identified by this UPC.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaUpc.
    
      :param companyId [int] The ID of the company that owns this UPC
      :param id_ [int] The primary key of this UPC
      :return UPCModel
    """
    def get_u_p_c(self, companyId, id_):
        return requests.get('{}/api/v2/companies/{}/upcs/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve UPCs for this company
    
    List all UPC objects attached to this company.
      A UPC represents a single UPC code in your catalog and matches this product to the tax code identified by this UPC.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaUpc.
    
      :param companyId [int] The ID of the company that owns these UPCs
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_u_p_cs_by_company(self, companyId, include=None):
        return requests.get('{}/api/v2/companies/{}/upcs'.format(self.base_url, companyId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all UPCs
    
    Get multiple UPC objects across all companies.
      A UPC represents a single UPC code in your catalog and matches this product to the tax code identified by this UPC.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, CSPAdmin, CSPTester, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser.
      * This API depends on the following active services<br />*Required* (all): AvaUpc.
    
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param include [string] A comma separated list of additional data to retrieve.
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_u_p_cs(self, include=None):
        return requests.get('{}/api/v2/upcs'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single UPC
    
    Replace the existing UPC object at this URL with an updated object.
      A UPC represents a single UPC code in your catalog and matches this product to the tax code identified by this UPC.
      All data from the existing object will be replaced with data in the object you PUT.
      To set a field's value to null, you may either set its value to null or omit that field from the object you post.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, CSPTester, SSTAdmin, TechnicalSupportAdmin.
      * This API depends on the following active services<br />*Required* (all): AvaUpc.
    
      :param companyId [int] The ID of the company that this UPC belongs to.
      :param id_ [int] The ID of the UPC you wish to update
      :param model [UPCModel] The UPC you wish to update.
      :return UPCModel
    """
    def update_u_p_c(self, companyId, id_, model):
        return requests.put('{}/api/v2/companies/{}/upcs/{}'.format(self.base_url, companyId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Change Password
    
    Allows a user to change their password via an API call.
      This API allows an authenticated user to change their password via an API call. This feature is only available
      for accounts that do not use SAML integrated password validation.
      This API only allows the currently authenticated user to change their password; it cannot be used to apply to a
      different user than the one authenticating the current API call.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param model [PasswordChangeModel] An object containing your current password and the new password.
      :return string
    """
    def change_password(self, model):
        return requests.put('{}/api/v2/passwords'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Create new users
    
    Create one or more new user objects attached to this account.
      A user represents one person with access privileges to make API calls and work with a specific account.
      Users who are account administrators or company users are permitted to create user records to invite
      additional team members to work with AvaTax.
      A newly created user will receive an email inviting them to create their password. This means that you
      must provide a valid email address for all user accounts created.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param accountId [int] The unique ID number of the account where these users will be created.
      :param model [UserModel] The user or array of users you wish to create.
      :return UserModel
    """
    def create_users(self, accountId, model):
        return requests.post('{}/api/v2/accounts/{}/users'.format(self.base_url, accountId),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Delete a single user
    
    Mark the user object identified by this URL as deleted.
      This API is available for use by account and company administrators only.
      Account and company administrators may only delete users within the appropriate organizations
      they control.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, CompanyAdmin, Compliance Root User, CSPTester, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TreasuryAdmin.
    
      :param id_ [int] The ID of the user you wish to delete.
      :param accountId [int] The accountID of the user you wish to delete.
      :return ErrorDetail
    """
    def delete_user(self, id_, accountId):
        return requests.delete('{}/api/v2/accounts/{}/users/{}'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve a single user
    
    Get the user object identified by this URL.
      A user represents one person with access privileges to make API calls and work with a specific account.
       You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * FetchDeleted
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The ID of the user to retrieve.
      :param accountId [int] The accountID of the user you wish to get.
      :param include [string] Optional fetch commands.
      :return UserModel
    """
    def get_user(self, id_, accountId, include=None):
        return requests.get('{}/api/v2/accounts/{}/users/{}'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all entitlements for a single user
    
    Return a list of all entitlements to which this user has rights to access.
      Entitlements are a list of specified API calls the user is permitted to make, a list of identifier numbers for companies the user is
      allowed to use, and an access level identifier that indicates what types of access roles the user is allowed to use.
      This API call is intended to provide a validation endpoint to determine, before making an API call, whether this call is likely to succeed.
      For example, if user 567 within account 999 is attempting to create a new child company underneath company 12345, you could preview the user's
      entitlements and predict whether this call would succeed:
      * Retrieve entitlements by calling '/api/v2/accounts/999/users/567/entitlements' . If the call fails, you do not have accurate
       credentials for this user.
      * If the 'accessLevel' field within entitlements is 'None', the call will fail.
      * If the 'accessLevel' field within entitlements is 'SingleCompany' or 'SingleAccount', the call will fail if the companies
       table does not contain the ID number 12345.
      * If the 'permissions' array within entitlements does not contain 'AccountSvc.CompanySave', the call will fail.
      For a full list of defined permissions, please use '/api/v2/definitions/permissions' .
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The ID of the user to retrieve.
      :param accountId [int] The accountID of the user you wish to get.
      :return UserEntitlementModel
    """
    def get_user_entitlements(self, id_, accountId):
        return requests.get('{}/api/v2/accounts/{}/users/{}/entitlements'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve users for this account
    
    List all user objects attached to this account.
      A user represents one person with access privileges to make API calls and work with a specific account.
      When an API is called using a legacy AvaTax License Key, the API log entry is recorded as being performed by a special user attached to that license key.
      By default, this API will not return a listing of license key users. Users with registrar-level security may call this API to list license key users.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * FetchDeleted
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param accountId [int] The accountID of the user you wish to list.
      :param include [string] Optional fetch commands.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def list_users_by_account(self, accountId, include=None):
        return requests.get('{}/api/v2/accounts/{}/users'.format(self.base_url, accountId),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Retrieve all users
    
    Get multiple user objects across all accounts.
      A user represents one person or set of credentials with access privileges to make API calls and work with a specific account. A user can be authenticated
      via either username / password authentication, an OpenID / OAuth Bearer Token, or a legacy AvaTax License Key.
      When an API is called using a legacy AvaTax License Key, the API log entry is recorded as being performed by a special user attached to that license key.
      By default, this API will not return a listing of license key users. Users with registrar-level security may call this API to list license key users.
      Search for specific objects using the criteria in the `$filter` parameter; full documentation is available on [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/) .
      Paginate your results using the `$top`, `$skip`, and `$orderby` parameters.
      You may specify one or more of the following values in the `$include` parameter to fetch additional nested data, using commas to separate multiple values:
      * FetchDeleted
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountOperator, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPAdmin, CSPTester, FirmAdmin, FirmUser, ProStoresOperator, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, SystemOperator, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param include [string] Optional fetch commands.
      :param filter [string] A filter statement to identify specific records to retrieve. For more information on filtering, see [Filtering in REST](http://developer.avalara.com/avatax/filtering-in-rest/).
      :param top [int] If nonzero, return no more than this number of results. Used with `$skip` to provide pagination for large datasets. Unless otherwise specified, the maximum number of records that can be returned from an API call is 1,000 records.
      :param skip [int] If nonzero, skip this number of results before returning data. Used with `$top` to provide pagination for large datasets.
      :param orderBy [string] A comma separated list of sort statements in the format `(fieldname) [ASC|DESC]`, for example `id ASC`.
      :return FetchResult
    """
    def query_users(self, include=None):
        return requests.get('{}/api/v2/users'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=include, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Update a single user
    
    Replace the existing user object at this URL with an updated object.
      A user represents one person with access privileges to make API calls and work with a specific account.
      All data from the existing object will be replaced with data in the object you PUT.
      To set a field's value to null, you may either set its value to null or omit that field from the object you post.
      ### Security Policies
      * This API requires one of the following user roles: AccountAdmin, AccountUser, CompanyAdmin, CompanyUser, Compliance Root User, ComplianceAdmin, ComplianceUser, CSPTester, FirmAdmin, FirmUser, Registrar, SiteAdmin, SSTAdmin, SystemAdmin, TechnicalSupportAdmin, TechnicalSupportUser, TreasuryAdmin, TreasuryUser.
    
      :param id_ [int] The ID of the user you wish to update.
      :param accountId [int] The accountID of the user you wish to update.
      :param model [UserModel] The user object you wish to update.
      :return UserModel
    """
    def update_user(self, id_, accountId, model):
        return requests.put('{}/api/v2/accounts/{}/users/{}'.format(self.base_url, accountId, id_),
                               auth=self.auth, headers=self.client_header, json=model, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Checks if the current user is subscribed to a specific service
    
    Returns a subscription object for the current account, or 404 Not Found if this subscription is not enabled for this account.
      This API will return an error if it is called with invalid authentication credentials.
      This API is intended to help you determine whether you have the necessary subscription to use certain API calls
      within AvaTax. You can examine the subscriptions returned from this API call to look for a particular product
      or subscription to provide useful information to the current user as to whether they are entitled to use
      specific features of AvaTax.
    
      :param serviceTypeId [ServiceTypeId] The service to check (See ServiceTypeId::* for a list of allowable values)
      :return SubscriptionModel
    """
    def get_my_subscription(self, serviceTypeId):
        return requests.get('{}/api/v2/utilities/subscriptions/{}'.format(self.base_url, serviceTypeId),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    List all services to which the current user is subscribed
    
    Returns the list of all subscriptions enabled for the currently logged in user.
      This API will return an error if it is called with invalid authentication credentials.
      This API is intended to help you determine whether you have the necessary subscription to use certain API calls
      within AvaTax. You can examine the subscriptions returned from this API call to look for a particular product
      or subscription to provide useful information to the current user as to whether they are entitled to use
      specific features of AvaTax.
    
      :return FetchResult
    """
    def list_my_subscriptions(self):
        return requests.get('{}/api/v2/utilities/subscriptions'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)

    r"""
    Tests connectivity and version of the service
    
    Check connectivity to AvaTax and return information about the AvaTax API server.
      This API is intended to help you verify that your connection is working. This API will always succeed and will
      never return a error. It provides basic information about the server you connect to:
      * `version` - The version number of the AvaTax API server that responded to your request. The AvaTax API version number is updated once per month during Avalara's update process.
      * `authenticated` - A boolean flag indicating whether or not you sent valid credentials with your API request.
      * `authenticationType` - If you provided valid credentials to the API, this field will tell you whether you used Bearer, Username, or LicenseKey authentication.
      * `authenticatedUserName` - If you provided valid credentials to the API, this field will tell you the username of the currently logged in user.
      * `authenticatedUserId` - If you provided valid credentials to the API, this field will tell you the user ID of the currently logged in user.
      * `authenticatedAccountId` - If you provided valid credentials to the API, this field will contain the account ID of the currently logged in user.
      This API helps diagnose connectivity problems between your application and AvaTax; you may call this API even
      if you do not have verified connection credentials. If this API fails, either your computer is not connected to
      the internet, or there is a routing problem between your office and Avalara, or the Avalara server is not available.
      For more information on the uptime of AvaTax, please see [Avalara's AvaTax Status Page](https://status.avalara.com/).
      ### Security Policies
      * This API may be called without providing authentication credentials.
    
      :return PingResultModel
    """
    def ping(self):
        return requests.get('{}/api/v2/utilities/ping'.format(self.base_url),
                               auth=self.auth, headers=self.client_header, params=None, 
                               timeout=self.timeout_limit if self.timeout_limit else 1200)
 
