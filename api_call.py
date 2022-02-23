# this script is meant to get user input and send a API request to generate a invoice
# at the end there is a example of all the fields available

import datetime
from datetime import date
import requests
import re

url = "http://192.168.1.7:5000/"  # the server url here, in this case is the local ip with the port


# ---------------------------- functions for input validation --------------------------------------

def get_invoice_number(filename="invoice_number.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        number = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(number))
        return number

def duedate_validation():

    dateRE=re.compile(r"""
        ^([1-9] | 0[1-9] | 1[0-9]| 2[0-9]| 3[0-1]) # match the day
        (\s) # match the delimiter
        ([1-9] | 0[1-9] | 1[0-2]) # match the month
        (\s) # match the delimiter
        20[0-9][0-9]$""" # match the year (limiting it for years after 2000 for convenience)
        , re.VERBOSE)
    
    while True:
        try:
            duedate = input("\nDue date (day month year):  ")
            date_check = dateRE.search(duedate)
            if date_check == None:
                print("\nInvalid date, please try again.\nUse the format day month year, delimited with a space. Ex: 23 04 2022")
                continue
            else:
                duedate = date_check.group()
                date_object = datetime.datetime.strptime(duedate, "%d %m %Y")
                return date_object.strftime("%-d %B %Y")

        except ValueError:
            print("\nInvalid date, please try again.\nUse the format day month year, delimited with a space. Ex: 23 04 2022")
            continue

def items_validation():
    items = []

    print("\n\nAdd the items to charge")

    add_more = "y"

    while add_more == "y":
        item = {}
        item["title"] = str(input("\nItem name:  "))
        item["charge"] = float(input("\nPrice:  "))

        items.append(item)
        add_more = str(input("\nAdd another item? [y/n]  "))

    return items

# ---------------------------- filling the invoice --------------------------------------

print("Fill the information of the invoice\n\n")

#1 invoice number

number = get_invoice_number()
year = date.today().strftime("%Y")
invoice_number = f"{number}/{year}"

#2 due date

duedate = duedate_validation()

#at this point I won't validate both from and to addresses, maybe in the future 
# if I decide to use this project further

#3 from address

from_addr = {
    "company_name": input("\n\nFrom: "),
    "addr1": input("\nAddress Line 1 (Street, Number):  "),
    "addr2": input("\nAddress Line 2 (Postal-Code City):  "),
}

#4 to address

to_addr = {
    "company_name": input("\n\t\t\t\t\t\t\tTo:  "),
    "client_name": input("\n\t\t\t\t\t\t\tClient Name:  "),
    "client_email": input("\n\t\t\t\t\t\t\tClient Email:  "),
}

#5 items

items = items_validation()

#6 add everything to the dictionary that we will send on the API call

user_data = {
    "duedate": duedate,
    "invoice_number": invoice_number,
    "from_addr": from_addr,
    "to_addr": to_addr,
    "items": items,
}

#7 send the request with the user data

try:
    today = date.today().strftime("%-d_%m_%Y")
    html = requests.post(url, json=user_data)
    with open(f"invoice_{today}.pdf", "wb") as f:
        f.write(html.content)
except:
    print("Connection failed")


# below is a example of all the items available thru the API

# data = {
#     'invoice_number': 111,
#     'duedate': 'day Month year',
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