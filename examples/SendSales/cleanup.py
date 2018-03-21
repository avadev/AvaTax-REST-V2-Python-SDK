""".

Use this script to remove ALL locations from your company
except for the one with locationCode = "DEFAULT"

"""

import os
import requests

"""
cleanup:
get locations by calling ListLocationsByCompany (GET)
(https://sandbox-rest.avatax.com/api/v2/companies/{companyId}/locations)

for each location (response.json()["value"][0]["id"])
delete the location (DELETE verb)
("https://sandbox-rest.avatax.com/api/v2/companies/{companyId}/locations/{id}")
"""

base_url = "https://sandbox-rest.avatax.com/api/v2"
user_auth = (os.environ["USERNAME"], os.environ["PASSWORD"])
comp_id = os.environ["COMPANY"]
comp_name = "TUGBOAT"

locs_for_company = requests.get("{}/companies/{}/locations".format(
                                base_url, comp_id), auth=user_auth)

for loc in locs_for_company.json()["value"]:
    if loc["locationCode"] == "DEFAULT":
        continue
    else:
        requests.delete("{}/companies/{}/locations/{}".format(
                        base_url, comp_id, loc["id"]), auth=user_auth)
