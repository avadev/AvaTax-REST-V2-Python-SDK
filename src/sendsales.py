"""Test app for sendsales."""

# from client import AvataxClient
import os
import requests
import time
import pdb

user_auth = (os.environ["USERNAME"], os.environ["PASSWORD"])
codes = requests.get('https://sandbox-rest.avatax.com/api/v2/definitions/postalcodes',
                     auth=user_auth)
test_codes = codes.json()["value"][0:10]  # small sample of codes to generate reports with to make sure its working
loc_list = []
tax_codes = ["P0000000", "FR020100", "SF096370"]
id_count = 1
total_start_time = time.time()
for entry in test_codes:  # codes.json()["value"]:
    # call CreateLocations on each one
    duration = 0
    start = time.time()

    addr_data = {"Address": {"PostalCode": "{}".format(entry["postalCode"])},
                 "UseCache": False}

    temp_address = requests.post("http://dev.address-service.avalara.net/AddressService/api/address/resolve",
                                 json=addr_data)
    if "NormalizedAddress" not in temp_address.json():
        continue
    else:
        addr = temp_address.json()["NormalizedAddress"]
    duration += time.time() - start

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
        continue
    if "State" in addr:
        loc[0]["region"] = addr["State"]
    else:
        continue

    start = time.time()
    # pdb.set_trace()
    # pdb.set_trace()
    new_loc = requests.post("https://sandbox-rest.avatax.com/api/v2/companies/{}/locations".format(os.environ["COMPANY"]),
                            auth=user_auth, json=loc)
    # print (new_loc.json())
    duration += time.time() - start
    # new_loc.json()[0]["id"]
    model = {
        "companyCode": "TUGBOAT",
        "responseType": "Json",
        "taxCodes": tax_codes,
        "locationCodes": [new_loc.json()[0]["locationCode"]]
    }
    # pdb.set_trace()
    start = time.time()
    # call BuildTaxContentFile() for each location
    tax_file = requests.post("https://sandbox-rest.avatax.com/api/v2/pointofsaledata/build", auth=user_auth, json=model)
    duration += time.time() - start
    # collect total time elapsed.
    loc_list.append([tax_file, duration])
    # send tax file to file
    file = open("./taxfiles/taxfile_{}.txt".format(model["locationCodes"][0]), "w")
    file.write(str(tax_file.json()) + ", ")
    file.close()
    print("Yes, I'm working: {}".format(id_count), "ET: {}".format(duration))
    id_count += 1
final_time = time.time() - total_start_time
print (final_time)

# output to file: this will write all the json tax rate info by location into a text file.

"""
file = open("taxfile_{}.txt".format(company))
for entry in loc_list:
    file.write(str(entry[0].json()[0]) + ", ")
file.close()
"""




# def main():
#     loc_file = sys.argv[1]
#     tax_codes = sys.argv[2]
#     file = open("taxFile.txt", "w")
#     file.write(build_tax_files(loc_file, tax_codes))


# if __name__ == '__main__':
#     main()
