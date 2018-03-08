"""Test app for sendsales."""

# from client import AvataxClient
import os
import requests
import time
import pdb

# os.environ['USERNAME']
# response.elapsed.total_seconds()
# codes.json()["value"][0] --> yields one postal code model

# test_client = AvataxClient(None, None, None, "Sandbox")

# test_client.add_credentials(os.environ["USERNAME"], os.environ["PASSWORD"])

# response = test_client.ping()

# def get_zones():
#     return requests.get('https://sandbox-rest.avatax.com/api/v2/definitions/postalcodes',
#                         auth=(os.environ["USERNAME"], os.environ["PASSWORD"]))

# codes = get_zones()
user_auth = (os.environ["USERNAME"], os.environ["PASSWORD"])
codes = requests.get('https://sandbox-rest.avatax.com/api/v2/definitions/postalcodes',
                     auth=user_auth)
loc_list = []
tax_codes = ["P0000000"]
id_count = 1
total_start_time = time.time()
for entry in codes.json()["value"]:
    # call CreateLocations on each one
    duration = 0
    start = time.time()
    addr_data = {"Address": {"PostalCode": "{}".format(entry["postalCode"])}}
    temp_address = requests.post("http://dev.address-service.avalara.net/AddressService/api/address/resolve",
                                 json=addr_data)
    # temp_address.json()["NormalizedAddress"]
    duration += time.time() - start

    loc = [{"id": id_count,
            "locationCode": "Location {}".format(id_count),
            "addressTypeId": "Location",
            "addressCategoryId": "Warehouse",
            "line1": temp_address.json()["NormalizedAddress"]["Line1"],
            # "city": temp_address.json()["NormalizedAddress"]["City"],
            "county": temp_address.json()["NormalizedAddress"]["County"],
            "region": temp_address.json()["NormalizedAddress"]["State"],
            "postalCode": "{}".format(entry["postalCode"]),
            "country": "US"}]
    start = time.time()
    # pdb.set_trace()
    pdb.set_trace()
    new_loc = requests.post("https://sandbox-rest.avatax.com/api/v2/companies/{}/locations".format(os.environ["COMPANY"]),
                            auth=user_auth, json=loc)

    duration += time.time() - start
    # new_loc.json()[0]["id"]
    model = {
        "companyCode": "TUGBOAT",
        "responseType": "Json",
        "taxCodes": tax_codes
    }
    start = time.time()
    tax_file = requests.post("https://sandbox-rest.avatax.com/api/v2/pointofsaledata/build", auth=user_auth, json=model)
    duration += time.time() - start
    # call BuildTaxContentFile() for each location
    # collect total time elapsed.
    loc_list.append([tax_file, duration])
    id_count += 1
final_time = time.time() - total_start_time

print (final_time)
