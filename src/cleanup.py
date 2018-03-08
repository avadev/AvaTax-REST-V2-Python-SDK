"""remove all the locations."""

import os
import requests
import pdb

"""
cleanup:
get locations ListLocationsByCompany (GET)
(https://sandbox-rest.avatax.com/api/v2/companies/{companyId}/locations)

for each location (response.json()["value"][0]["id"])
delete (DELETE verb)
("https://sandbox-rest.avatax.com/api/v2/companies/{companyId}/locations/{id}")
"""

base_url = "https://sandbox-rest.avatax.com/api/v2"
user_auth = (os.environ["USERNAME"], os.environ["PASSWORD"])
comp_id = os.environ["COMPANY"]
comp_name = "TUGBOAT"

locs_for_company = requests.get("{}/companies/{}/locations".format(base_url, comp_id), auth=user_auth)
# pdb.set_trace()
# locs_for_company.json()["value"][0]["id"]
for loc in locs_for_company.json()["value"]:
    if loc["locationCode"] == "DEFAULT":
        continue
    else:
        requests.delete("{}/companies/{}/locations/{}".format(base_url, comp_id, loc["id"]), auth=user_auth)
