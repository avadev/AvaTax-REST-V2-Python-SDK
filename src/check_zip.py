"""Gather and check zip code address creation."""

import requests
import os
import time

bad_zips = []
id_count = 1
user_auth = (os.environ["USERNAME"], os.environ["PASSWORD"])
codes = requests.get('https://sandbox-rest.avatax.com/api/v2/definitions/postalcodes',
                     auth=user_auth)
for entry in codes.json()["value"]:
    duration = 0
    start = time.time()

    addr_data = {"Address": {"PostalCode": "{}".format(entry["postalCode"])},
                 "UseCache": False}

    temp_address = requests.post("http://dev.address-service.avalara.net/AddressService/api/address/resolve",
                                 json=addr_data)
    if "NormalizedAddress" not in temp_address.json():
        bad_zips.append(entry["postalCode"])
        continue
    else:
        addr = temp_address.json()["NormalizedAddress"]

    loc = [{"id": id_count,
            "locationCode": "Location {}".format(id_count),
            "addressTypeId": "Location",
            "addressCategoryId": "Warehouse",
            "line1": temp_address.json()["NormalizedAddress"]["Line1"],
            "postalCode": "{}".format(entry["postalCode"]),
            "country": "US"}]
    if "City" in addr:
        loc[0]["city"] = addr["City"]
    else:
        bad_zips.append(entry["postalCode"])
        continue
    if "State" in addr:
        loc[0]["state"] = addr["State"]
    else:
        bad_zips.append(entry["postalCode"])

        continue

    id_count += 1
    print (bad_zips, id_count)
