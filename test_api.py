# this script is meant to test the API to request a invoice

import requests
from datetime import datetime

url = "http://192.168.1.7:5000/"  # the server url here, in this case is the local ip with the port


# below is a example of all the items available thru the API

# data = {
#     'invoice_number': 111,
#     'duedate': 'day Month, year',
#     'from_addr': {
#         'company_name': 'Company name',
#         'addr1': 'Street name, Number',
#         'addr2': 'Postal Code, City'
#     },
#     'items': [{
#             'title': 'Homepage w/ host+domain',
#             'charge': 400.50

#         },
#         {
#             'title': 'Hardware setup',
#             'charge': 200.0
#         },
#         {
#             'title': 'Network setup',
#             'charge': 150.75
#         }
#     ],
#     'to_addr': {
#         'company_name': 'Client Company Name',
#         'client_name': 'Client Name',
#         'client_email': 'client@mail.com'
#     }
# }


print("Fill the information of the invoice\n\n")


def get_invoice_number(filename="invoice_number.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val


number = get_invoice_number()
year = datetime.today().strftime("%Y")

invoice_number = f"{number}/{year}"
duedate = input("\nDue date (day month, year):  ")

from_addr = {
    "company_name": input("\n\nFrom: "),
    "addr1": input("\nAddress Line 1 (Street , Number):  "),
    "addr2": input("\nAddress Line 2 (Postal-Code City):  "),
}

to_addr = {
    "company_name": input("\n\t\t\t\t\t\t\tTo:  "),
    "client_name": input("\n\t\t\t\t\t\t\tClient Name:  "),
    "client_email": input("\n\t\t\t\t\t\t\tClient Email:  "),
}

items = []


print("\n\nAdd the items to charge")

add_more = "y"

while add_more == "y":
    item = {}
    item["title"] = str(input("\nItem name:  "))
    item["charge"] = float(input("\nPrice:  "))

    items.append(item)
    add_more = str(input("\nAdd another item? [y/n]  "))


user_data = {
    "duedate": duedate,
    "invoice_number": invoice_number,
    "from_addr": from_addr,
    "to_addr": to_addr,
    "items": items,
}


try:
    today = datetime.today().strftime("%-d_%B_%Y")
    html = requests.post(url, json=user_data)
    with open(f"invoice_{today}.pdf", "wb") as f:
        f.write(html.content)
except:
    print("Connection failed")
