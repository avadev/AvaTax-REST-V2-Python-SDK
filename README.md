# Avalara AvaTax Python SDK
[![Build Status](https://travis-ci.org/avadev/AvaTax-REST-V2-Python-SDK.svg?branch=master)](https://travis-ci.org/avadev/AvaTax-REST-V2-Python-SDK)
[![PyPI](https://img.shields.io/pypi/v/Avalara.svg)](https://pypi.python.org/pypi/Avalara)

This GitHub repository is the Python SDK for Avalara's world-class tax service, AvaTax.  It uses the AvaTax REST v2 API, which is a fully REST implementation and provides a single client for all AvaTax functionality.  For more information about AvaTax REST v2, please visit [Avalara's Developer Network](http://developer.avalara.com/) or view the [online Swagger documentation](https://sandbox-rest.avatax.com/swagger/ui/index.html).


## Installation:

Install simply with pip.
```pip install Avalara```

**OR**

1. Clone this repository to your local machine.
```
$ git clone https://github.com/avadev/AvaTax-REST-V2-Python-SDK.git
```
2. Once downloaded, cd into the ```AvaTax-REST-V2-Python-SDK``` directory.
```
$ cd AvaTax-REST-V2-Python-SDK
```
3. Begin a new virtual environment with Python 3 and activate it.
```
AvaTax-REST-V2-Python-SDK $ python3 -m venv ENV
AvaTax-REST-V2-Python-SDK $ source ENV/bin/activate
```
4. [pip](https://pip.pypa.io/en/stable) install this package as well as the testing set of extras into your virtual enviroment.
```
(ENV) AvaTax-REST-V2-Python-SDK $ pip install -e .
(ENV) AvaTax-REST-V2-Python-SDK $ pip install -e .[testing]
```

## Usage:

### Create a transaction


**Import the AvataxClient from the avalara module**

First thing to do is to import the AvataxClient constructor module to your name space, or your python script.

```
from avalara import AvataxClient
```

**Now we are ready to construct a client object**

Create a new AvaTaxClient object:
```
    client = AvataxClient('my test app',
                          'ver 0.0',
                          'my test machine',
                          'sandbox')
```
The client constructor takes four string parameters, in squence they are `app_name(required)`, `app_version(required)`, `machine_name(optional)`, and `environment(required)`.
The app_name, app_version, machine_name will be used to construct the [Client Header](https://developer.avalara.com/avatax/client-headers/) associated with each call made by this client. It will be returned within the response object to help you keep track of the API calls.
The `environment` variable can be either `"sandbox"` or `production`, they correspond to the two different environments for AvaTax service.
If you are a regular or free trial customer please use `"production"`. If you don't have an account, you can sign up for a free trail account on our [developer site](https://developer.avalara.com/avatax/signup/), this will be a production account as well.
If you wish to obtain a Sandbox account, please contact your [Customer Account Manager](https://help.avalara.com/Frequently_Asked_Questions/Avalara_AvaTax_FAQ/How_do_I_get_access_to_our_development%2F%2Fsandbox_account%3F)


**Ping the service**

Now we have a client object, we can ping the AvaTax REST V2 server to ensure connectivity.
```
  response = client.ping()

  # to view respnse text
  print(response.text())

  # to view json version of the response
  print(response.json())

  # to view the status code
  print(response.status_code())

  # to view the raw response
  print(response.raw())
```
Note that the response from all REST calls made using this SDK will be [Request](http://docs.python-requests.org/en/master/user/quickstart/#response-content) object, which contains status code, response text, raw josn, and more information on the respnse.


**Add credentials to your client object**

Unlike `ping`, most methods in our REST V2 API requires you to be authenticated in order to associate those information provided by you with your account.
To find out if a method requires authentication, visit our [API Reference](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Transactions/) page.
To add credential on the current client object:
```
  client = client.add_credentials('USERNAME/ACCOUNT_ID', 'PASSWORD/LICENSE_KEY')
```
The `add_credential` method will hash your username/password, or account_id/license_key pair and attach to every call made by your client object, meaning you only have to add credential once to each client you prepare to use.

To verify that you have added a valid credential, simply call the `ping` method again, this time in the response text you should see `"authenticated": true`.


**To create a transaction using your client object**

Now our client object is authenticated, we can call the create_transaction method which calls the [CreateTransaction API](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Transactions/CreateTransaction/)
```
  transaction_response = client.create_transaction(tax_document)
  print(transaction_response.text())

  tax_document = {
      'addresses': {'SingleLocation': {'city': 'Irvine',
                                       'country': 'US',
                                       'line1': '123 Main Street',
                                       'postalCode': '92615',
                                       'region': 'CA'}},
      'commit': False,
      'companyCode': 'DEFAULT',
      'currencyCode': 'USD',
      'customerCode': 'ABC',
      'date': '2017-04-12',
      'description': 'Yarn',
      'lines': [{'amount': 100,
                'description': 'Yarn',
                 'itemCode': 'Y0001',
                 'number': '1',
                 'quantity': 1,
                 'taxCode': 'PS081282'}],
      'purchaseOrderNo': '2017-04-12-001',
      'type': 'SalesInvoice'}

```  
The create_transaction method takes in a model, in python it's a dictionary type object. Which you will fill out to include all of your transaction information. In this case, we are using the [TransactionModel](https://developer.avalara.com/api-reference/avatax/rest/v2/models/TransactionModel/)
For information on other models use by AvaTax APIs, visit our information page [here](https://developer.avalara.com/api-reference/avatax/rest/v2/models)


### Use other methods

Like our SDKs in other languages, the Python SDK includes all methods offered by the AvaTax REST V2 API. To find a mehtod corresponding to a specific API endpoint, simply visit this [code page](https://github.com/avadev/AvaTax-REST-V2-Python-SDK/blob/master/src/client_methods.py)
To learn more about integrating our REST API into your system, visit our [developer guide](https://developer.avalara.com/avatax/dev-guide/getting-started-with-avatax/) that contains information on using the powerful features offered by our API.


### Use transaction builder

We realize that having to format the TransactionModel can be complicated and time consuming, thus we created a tool called Transaction Builder to help you put together a transaction model, and create it!
First import the transaction builder constructor into your name space:
```from avalara.transaction_builder import TransactionBuilder```

Then, let's create a transaction builder object:
```
  tb = TransactionBuilder(client, "DEFAULT", "SalesInvoice", "ABC")
```
The builder takes four required parameters, in sequence they are
- The client object
- Company name(created through AvaTax portal or by calling [CreateCompany API](https://developer.avalara.com/api-reference/avatax/rest/v2/methods/Companies/CreateCompanies/))
- The type of transaction, a [full list](https://developer.avalara.com/api-reference/avatax/rest/v2/models/enums/DocumentType/) of options. 
- The customer code, an unique code identifying the customer that requested this transaction.

Now you are free to add transaction details to this object, by using methods like `with_address`, `with_line`, `with_parameter`.
For a fulll list of transaction builder methods available and the parameters they take in, visit the [code page](https://github.com/avadev/AvaTax-REST-V2-Python-SDK/blob/master/src/transaction_builder_methods.py)
In the end, you may call the `create` method on your builder object, which will call the CreateTransaction API with the transaction model you have build so far, and return back the response.


### Setup Test Credentials

If you wish to run the integration and unit testings, you must store a pair of credentials in the current enviroment.
Add the following to the ```activate``` file in your environment, and restart bash.
OR simply ```export``` them directly:

```
export SANDBOX_USERNAME='your_sandbox_username'
export SANDBOX_PASSWORD='your_sandbox_password'

# OR
SANDBOX_ACCOUNTID='your_sandbox_account_id'
SANDBOX_LICENSEKEY='your_sandbox_license_key'
```
Note: Only *Sandbox credentials* should be used for testing, as the test case will commit/adjust/void dummy transactions on the account to verify functionalities.  

### Logging

Logging is implemented using standard Python logging framework.

1. All relevant methods from `AvataxClient` class are decorated with `ava_log` decorator.(This is achieved using another decorator at class level, `decorate_all_methods`)
2. `ava_log` decorator collects relevant request data, response data useful for instrumentation and logs error data in case of exception.
3. `AvataxClient` constructor is modified with optional parameter, `is_log_req_resp_allowed` (defaulted to False), to control if log entry should contain request and response objects.
4. SDK Consumer code can also set logger property of `AvataxClient` to use already configured logger instance. e.g. 
```
from logging import config 

# configure logging using file config or dictConfig 
# or by setting basicConfig (this is default in case no logger is set)
config.fileConfig("logger_config.conf")

logger = logging.getLogger()

# set logger property
client.logger = logger
```
    

## Issue or suggestion

User feedbacks are highly valued here at Avalara, we want to ensure the best experience for every customer using our services. If you have any concern with this SDK or AvaTax in general, please post your queston/suggestion on our [Developer Relation Forum](https://community.avalara.com/avalara/category_sets/developers) as we will reply to you in a timely manner.
If you wish to contribute to this SDK, please fork the [repository](https://github.com/avadev/AvaTax-REST-V2-Python-SDK) and submit your pull request from the forked version. We are happy to review your contribution, and merge them if all checks has passed!


## Original Contributors

[Han Bao](https://www.linkedin.com/in/hbao2016)

[Philip Werner](https://www.linkedin.com/in/philip-werner-421aa66a)

[Robert Bronson](https://www.linkedin.com/in/robert-bronson)

[Adrienne Karnoski](https://www.linkedin.com/in/adrienne-karnoski)
