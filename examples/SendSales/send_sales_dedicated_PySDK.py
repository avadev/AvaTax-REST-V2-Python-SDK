"""Generates a tax file for each location in a company.

This script generates a tax file for each location in a
company, based on a supplied tax code list.

Writing the files requires a folder named "taxfiles" to be
created prior to running this script.
"""
from client import AvataxClient
from tax_code_list import sample_codes as tax_codes
import os
import sys
import time
import datetime

# Creates a client object using dummy company "new_client"
new_client = AvataxClient(None, None, None, "sandbox")
new_client.add_credentials(os.environ["USERNAME"], os.environ["PASSWORD"])

# create variables for analytic data to be sent to
analytics = []
analysis = open("./taxfiles/analytics.txt", "a")
iter_count = 0
total_start_time = time.time()
tax_file_list = []
comp_id = os.environ["COMPANY"]

# get all the locations belonging to the target company.
location_list = new_client.list_locations_by_company(
    comp_id).json()["value"]
# get the company code for the target company.
comp_code = new_client.get_company(comp_id).json()["companyCode"]

# go through the zip code list and generate an address
for entry in location_list:
    iter_count += 1
    duration = 0
    loc_id = entry["id"]
# set up the model with the tax codes imported on ln 9
    tax_model = {
        "companyCode": comp_code,
        "responseType": "Json",
        "taxCodes": tax_codes,  # imported from tax_codes file
        "locationCodes": [entry["locationCode"]]
    }

    start = time.time()

# build the tax file with imported set of tax codes
    new_file = new_client.build_tax_content_file(tax_model)
    duration += time.time() - start
    tax_file_list.append([new_file, duration])

# Build the tax file with default company established tax information,
# Need to have tax codes set up within the company and locations.

    # new_file = new_client.build_tax_content_file_for_location(comp_id,
    #                                                           loc_id)
    # duration += time.time() - start
    # tax_file_list.append([new_file, duration])

# write the tax file data to a new file
    file = open("./taxfiles/{}_{}.txt".format(
        datetime.datetime.now().date(), entry["locationCode"]), "w")
    file.write(str(new_file.json()))
    file.close()
# write the analytics to a file
    analysis.write("{}: time elapsed: {}(s)\n".format(
        entry["locationCode"], duration))
    # print(entry["locationCode"])
    sys.stdout.write("\rProgress: {}".format(entry["locationCode"]))

final_time = time.time() - total_start_time
analysis.write("Total Time: {}(s)".format(final_time))
analysis.close()
