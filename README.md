# Avalara AvaTax Python SDK
[![Build Status](https://travis-ci.org/avadev/AvaTax-REST-V2-Python-SDK.svg?branch=master)](https://travis-ci.org/avadev/AvaTax-REST-V2-Python-SDK)
[![PyPI](https://img.shields.io/pypi/v/Avalara.svg)](https://pypi.python.org/pypi/Avalara-Python-SDK)

### About Our Product:
This GitHub repository is the Python SDK for Avalara's world-class tax service, AvaTax.  It uses the AvaTax REST v2 API, which is a fully REST implementation and provides a single client for all AvaTax functionality.  For more information about AvaTax REST v2, please visit [Avalara's Developer Network](http://developer.avalara.com/) or view the [online Swagger documentation](https://sandbox-rest.avatax.com/swagger/ui/index.html).


## **Set Up and Installation:**

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
Python_Final $ python3 -m venv ENV
Python_Final $ source ENV/bin/activate
```
[pip](https://pip.pypa.io/en/stable) install this package as well as the testing set of extras into your virtual enviroment.
```
(ENV) Python_Final $ pip install -e .
(ENV) Python_Final $ pip install -e .[testing]
```

## **Usage:**

### **Configuration**

**Environment**

Avalara provides two different environments for AvaTax: **Sandbox** and **Production**.

The **Sandbox** environment is meant to help you test your software without the risk of accidentally affecting production data or reporting transactions. 

In **Production**, transactions that are marked Committed can be reported on a tax filing using the Avalara Managed Returns Service.

Each environment is completely separate, and each has its own credentials.

If you have a Sandbox account, you cannot use that account to log onto Production; and vice versa.

### **Setup Test Credentials**

For testing, your credentials are accessed as environment varibales through os.environ.
Add the following to the ```activate``` file in your environment:

```
  bash
# Username and password
SANDBOX_USERNAME='your_sandbox_username'
SANDBOX_PASSWORD='your_sandbox_password'

# Or account id and license key
SANDBOX_ACCOUNTID='your_sandbox_account_id'
SANDBOX_LICENSEKEY='your_sandbox_license_key'
```
Note: Only *Sandbox credentials* should be used for testing, as the test case will commit/adjust/void dummy transactions on the account to verify functionalities.  
You may store testing credentials onto the `activate` script within your `ENV/bin`:  
```
export SANDBOX_USERNAME='<your-username>'
export SANDBOX_PASSWORD='<your-password>'
export SANDBOX_ACCOUNTID='<your-account-id>'
export SANDBOX_LICENSEKEY='<your-license-key>'
```
**Import the python AvaTaxClient from the client module:**

```
from client import AvaTaxClient
```
Create a new AvaTaxClient object:
```
client = new AvaTaxClient("app-name", 'app-version', 'your-machine-name', 'your-desired-environment').add_credentials('<Your-credentials>')
```

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
return print(client.createTransaction(tax_document))
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

### **Contributors:**

[Han Bao](https://www.linkedin.com/in/hbao2016)

[Philip Werner](https://www.linkedin.com/in/philip-werner-421aa66a)

[Robert Bronson](https://www.linkedin.com/in/robert-bronson)

[Adrienne Karnoski](https://www.linkedin.com/in/adrienne-karnoski)
