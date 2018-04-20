# Avalara AvaTax Python SDK
[![Build Status](https://travis-ci.org/avadev/AvaTax-REST-V2-Python-SDK.svg?branch=master)](https://travis-ci.org/avadev/AvaTax-REST-V2-Python-SDK)
[![PyPI](https://img.shields.io/pypi/v/Avalara.svg)](https://pypi.python.org/pypi/Avalara)

### About Our Product:
This GitHub repository is the Python SDK for Avalara's world-class tax service, AvaTax.  It uses the AvaTax REST v2 API, which is a fully REST implementation and provides a single client for all AvaTax functionality.  For more information about AvaTax REST v2, please visit [Avalara's Developer Network](http://developer.avalara.com/) or view the [online Swagger documentation](https://sandbox-rest.avatax.com/swagger/ui/index.html).


## **Set Up and Installation:**

Install simply with pip.
```pip install Avalara```

**OR**

Clone this repository to your local machine.
```
$ git clone https://github.com/avadev/AvaTax-REST-V2-Python-SDK.git
```
Once downloaded, cd into the ```AvaTax-REST-V2-Python-SDK``` directory.
```
$ cd AvaTax-REST-V2-Python-SDK
```
Begin a new virtual environment with Python 3 and activate it.
```
AvaTax-REST-V2-Python-SDK $ python3 -m venv ENV
AvaTax-REST-V2-Python-SDK $ source ENV/bin/activate
```
[pip](https://pip.pypa.io/en/stable) install this package as well as the testing set of extras into your virtual enviroment.
```
(ENV) AvaTax-REST-V2-Python-SDK $ pip install -e .
(ENV) AvaTax-REST-V2-Python-SDK $ pip install -e .[testing]
```

## **Usage:**

### **Configuration**

**Import the AvataxClient from the client module:**

First thing to do is to import the AvataxClient constructor module to your name space, or your python script.

```
from client import AvataxClient
```

**Now we are ready to construct a client object**

Create a new AvaTaxClient object:
```
    client = AvataxClient('my test app',
                          'ver 0.0',
                          'my test machine',
                          'sandbox')
```
The client constructor takes four string parameters, in squence they are `app_name(required)`, `app_version(required)`, `achine_name(optional)`, and `environment(required)`. 
The app_name, app_version, machine_name will be use to construct the [Client Header](https://developer.avalara.com/avatax/client-headers/) associated with each calls made by this client. Which will be return within the response object to help you keep track of the API calls.
The 






**Environment**

Avalara provides two different environments for AvaTax: **Sandbox** and **Production**.

The **Sandbox** environment is meant to help you test your software without the risk of accidentally affecting production data or reporting transactions. 

In **Production**, transactions that are marked Committed can be reported on a tax filing using the Avalara Managed Returns Service.

Each environment is completely separate, and each has its own credentials.

If you have a Sandbox account, you cannot use that account to log onto Production; and vice versa.







### **Tax Calculation**
```
tax_document = {
  type: 'SalesInvoice',
  companyCode: 'abc123',
  date: '2017-04-12',
  customerCode: 'ABC',
  purchaseOrderNo: '2017-04-12-001',
  addresses: {
    SingleLocation: {
      line1: '123 Main Street',
      city: 'Irvine',
      region: 'CA',
      country: 'US',
      postalCode: '92615'
    }
  },
  lines: [
    {
      number: '1',
      quantity: 1,
      amount: 100,
      taxCode: 'PS081282',
      itemCode: 'Y0001',
      description: 'Yarn'
    }
  ],
  commit: true,
  currencyCode: 'USD',
  description: 'Yarn'
}
print(client.createTransaction(tax_document))
```

### **Address Validation**
```
address = {
  city: 'irvine',
  postalCode: '92615',
  region: 'ca',
  country: 'us'
}
return print(client.resolveAddress(address))
```


### **Setup Test Credentials**

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


### **Contributors:**

[Han Bao](https://www.linkedin.com/in/hbao2016)

[Philip Werner](https://www.linkedin.com/in/philip-werner-421aa66a)

[Robert Bronson](https://www.linkedin.com/in/robert-bronson)

[Adrienne Karnoski](https://www.linkedin.com/in/adrienne-karnoski)
