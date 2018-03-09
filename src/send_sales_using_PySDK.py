"""."""
from client import AvataxClient
from tax_code_list import sample_codes as tax_codes
import requests
import os
import time
import datetime
import pdb


tugboat = AvataxClient(None, None, None, "sandbox")

tugboat.add_credentials(os.environ["USERNAME"], os.environ["PASSWORD"])

zip_codes = tugboat.list_postal_codes()

test_zip_codes = zip_codes.json()["value"][0:50]

analytics = []
analysis = open("./taxfiles/analytics.txt", "a")

location_list = []
iter_count = 0
total_start_time = time.time()

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

    start = time.time()
    new_location = tugboat.create_locations(os.environ["COMPANY"],
                                            location_model)
    duration += time.time() - start

    tax_model = {
        "companyCode": "TUGBOAT",  # change this to take customer's company
        "responseType": "Json",
        "taxCodes": tax_codes,
        "locationCodes": [new_location.json()[0]["locationCode"]]
    }

    start = time.time()
    new_file = tugboat.build_tax_content_file(tax_model)
    duration += time.time() - start

    location_list.append([new_file, duration])

    file = open("./taxfiles/{}_{}.txt".format(datetime.datetime.now().date(),
                                              tax_model["locationCodes"][0]),
                "w")
    file.write(str(new_file.json()) + ", ")
    file.close()

    analysis.write("{}: time elapsed: {}(s)\n".format(tax_model["locationCodes"][0],
                                                      duration))

final_time = time.time() - total_start_time
analysis.write("Total Time: {}(s)".format(final_time))
analysis.close()
