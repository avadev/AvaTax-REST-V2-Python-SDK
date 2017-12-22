# Avalara AvaTax Python SDK
[![Build Status](https://travis-ci.org/RJB888/Python_Final.svg?branch=master)](https://travis-ci.org/RJB888/Python_Final)

### About Our Product:
This GitHub repository is the Python SDK for Avalara's world-class tax service, AvaTax.  It uses the AvaTax REST v2 API, which is a fully REST implementation and provides a single client for all AvaTax functionality.  For more information about AvaTax REST v2, please visit [Avalara's Developer Network](http://developer.avalara.com/) or view the [online Swagger documentation](https://sandbox-rest.avatax.com/swagger/ui/index.html).


### **Meet the Team:**

[Han Bao](https://www.linkedin.com/in/hbao2016)

[Philip Werner](https://www.linkedin.com/in/philip-werner-421aa66a)

[Robert Bronson](https://www.linkedin.com/in/robert-bronson)

[Adrienne Karnoski](https://www.linkedin.com/in/adrienne-karnoski)

## **Set Up and Installation:**

Clone this repository to your local machine.
```
$ git clone https://github.com/RJB888/Python_Final.git
```
Once downloaded, cd into the ```Python_Final``` directory.
```
$ cd Python_Final
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

// Python import
// from client import AvaTaxClient

// Inside ENV/bin/activate export your credentials:
```
export USERNAME='<your-username>'
export PASSWORD='<your-password>'
export ACCOUNT_ID='<your-account-id>'
export LICENSE_KEY='<your-license-key>'

client = new AvaTaxClient('<app-name>', '<app-version>', '<your-machine-name>', '<your-desired-environment>').add_credentials('<Your-credentials>')
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