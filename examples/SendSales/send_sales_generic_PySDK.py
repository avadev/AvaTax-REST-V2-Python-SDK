"""Generates a tax file for each zip code.

This script calls the AvaTax API to pull a list of all zip codes
with addresses and creates locations based on that list.
Then it generates a tax file based on the locations and given
list of tax codes.

Writing the files requires a folder named "taxfiles" to be
created prior to running this script.
"""
from client import AvataxClient
from tax_code_list import sample_codes as tax_codes
import os
import sys
import time
import datetime

# Creates a client object using dummy company "tugboat"
tugboat = AvataxClient(None, None, None, "sandbox")
tugboat.add_credentials(os.environ["USERNAME"], os.environ["PASSWORD"])

comp_id = os.environ["COMPANY"]
comp_code = tugboat.get_company(comp_id).json()["companyCode"]
# get list of all zip codes with address by date
address_gen = tugboat.download_tax_rates_by_zip_code(
    datetime.date.today().isoformat())

# List comprehension to create array of all addresses from generator
#  slicing only address information
address_array = [item.decode("utf-8").split(",")[:4]
                 for item in address_gen.iter_lines()][1:]

# create variables for analytic data to be sent to
analytics = []
analysis = open("./taxfiles/analytics.txt", "a")
location_list = []
iter_count = 0
skip_count = 0

total_start_time = time.time()

# for each address array create a location - slice used for testing
for entry in address_array[200:250]:  # take out the slice to use all addr
    iter_count += 1
    duration = 0
    start = time.time()

    # if address has information, create a location model with it.
    if entry[0]:
        location_model = [
            {
                "id": iter_count,
                "locationCode": "Location{}".format(iter_count),
                "addressTypeId": "Location",
                "addressCategoryId": "Warehouse",
                "line1": "1 Main St",
                "postalCode": entry[0],
                "country": "US"
            }]
        location_model[0]["city"] = entry[3]
        location_model[0]["region"] = entry[1]
    else:  # if not skip that location in the array of addresses
        skip_count += 1
        continue

    duration += time.time() - start

# establish variables to log how long the process takes
    start = time.time()
    new_location = tugboat.create_locations(comp_id, location_model)
    duration += time.time() - start
# set up the model with the tax codes imported on ln 9
    tax_model = {
        "companyCode": comp_code,  # change this to take customer's company
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
    file = open("./taxfiles/{}_{}.txt".format(
        datetime.datetime.now().date(), tax_model["locationCodes"][0]), "w")

    file.write(str(new_file.json()) + ", ")
    file.close()
# write the analytics to a file
    analysis.write("{}: Time: {}(s)\n".format(
        tax_model["locationCodes"][0], duration))

    sys.stdout.write("\rProg:  {}".format(location_model[0]["locationCode"]))
final_time = time.time() - total_start_time

print("\nCOMPLETE")
analysis.write("Total Time: {}(s)".format(final_time))
analysis.close()
