# Avalara AvaTax Python SDK


### About Our Product:
This GitHub repository is the Python SDK for Avalara's world-class tax service, AvaTax.  It uses the AvaTax REST v2 API, which is a fully REST implementation and provides a single client for all AvaTax functionality.  For more information about AvaTax REST v2, please visit [Avalara's Developer Network](http://developer.avalara.com/) or view the [online Swagger documentation](https://sandbox-rest.avatax.com/swagger/ui/index.html).



### Meet the Team:

[Han Bao](https://github.com/han8909227)

[Philip Werner](https://github.com/philipwerner)

[Robert Bronson](https://github.com/RJB888)

[Adrienne Karnoski](https://github.com/adriennekarnoski)

### Set Up and Installation:

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