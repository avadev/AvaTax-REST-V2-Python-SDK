"""Generates a tax file for each zip code.

This script calls the Avatax API for a list of zip codes,
then generates dummy locations based on those zip codes,
and finally generates a tax file based on the locations and given
list of tax codes.

Writing the files requires a folder named "taxfiles" to be
created prior to running this script.
"""
from client import AvataxClient
from tax_code_list import sample_codes as tax_codes
import requests
import os
import time
import datetime

# Creates a client object using dummy company "tugboat"
tugboat = AvataxClient(None, None, None, "sandbox")

tugboat.add_credentials(os.environ["USERNAME"], os.environ["PASSWORD"])

# Get list of all zip codes
zip_codes = tugboat.list_postal_codes()

# For testing purposes - slice the zip code list to a usable quantity
test_zip_codes = zip_codes.json()["value"][0:50]

# create variables for analytic data to be sent to
analytics = []
analysis = open("./taxfiles/analytics.txt", "a")
location_list = []
iter_count = 0
total_start_time = time.time()

# go through the zip code list and generate an address
for entry in test_zip_codes:
    iter_count += 1
    duration = 0
    start = time.time()
    addr_data = {
        "Address": {"PostalCode": "{}".format(entry["postalCode"])},
        "UseCache": False
    }

    new_address = requests.post(
        "http://dev.address-service.avalara.net/AddressService/api/address/resolve",
        json=addr_data)

    if "NormalizedAddress" not in new_address.json():
        continue
    else:
        addr = new_address.json()["NormalizedAddress"]
    duration += time.time() - start

    location_model = [
        {
            "id": iter_count,
            "locationCode": "Location{}".format(iter_count),
            "addressTypeId": "Location",
            "addressCategoryId": "Warehouse",
            "line1": new_address.json()["NormalizedAddress"]["Line1"],
            "postalCode": "{}".format(entry["postalCode"]),
            "country": "US"
        }]
    if "City" in addr:
        location_model[0]["city"] = addr["City"]
    else:
        continue
    if "State" in addr:
        location_model[0]["region"] = addr["State"]
    else:
        continue

# establish variables to log how long the process takes
    start = time.time()
    new_location = tugboat.create_locations(os.environ["COMPANY"],
                                            location_model)
    duration += time.time() - start
# set up the model with the tax codes imported on ln 9
    tax_model = {
        "companyCode": "TUGBOAT",  # change this to take customer's company
        "responseType": "Json",
        "taxCodes": tax_codes,
        "locationCodes": [new_location.json()[0]["locationCode"]]
    }

    start = time.time()
# build the tax file
    new_file = tugboat.build_tax_content_file(tax_model)
    duration += time.time() - start

    location_list.append([new_file, duration])
# write the tax file data to a new file
    file = open("./taxfiles/{}_{}.txt".format(datetime.datetime.now().date(),
                                              tax_model["locationCodes"][0]),
                "w")
    file.write(str(new_file.json()) + ", ")
    file.close()
# write the analytics to a file
    analysis.write("{}: time elapsed: {}(s)\n".format(tax_model["locationCodes"][0],
                                                      duration))

final_time = time.time() - total_start_time
analysis.write("Total Time: {}(s)".format(final_time))
analysis.close()
