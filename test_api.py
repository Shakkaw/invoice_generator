# this script is meant to test the API to request a invoice

import requests

url = 'http://192.168.1.7:5000/' #the server url here, in this case is the local ip with the port


#below is a example of all the items available thru the API

# data = {
#     'duedate': '1 September, 2014',
#     'from_addr': {
#         'company_name': 'Company ABC',
#         'addr1': 'Hamilton, New York',
#         'addr2': 'Sunnyville, CA 12345'
#     },
#     'invoice_number': 156,
#     'items': [{
#             'charge': 500.0,
#             'title': 'Brochure design'
#         },
#         {
#             'charge': 85.0,
#             'title': 'Hosting (6 months)'
#         },
#         {
#             'charge': 10.0,
#             'title': 'Domain name (1 year)'
#         }
#     ],
#     'to_addr': {
#         'company_name': 'Company DEF',
#         'client_name': 'John Smith',
#         'client_email': 'johnsmith@companydef.com'
#     }
# }

print("Fill the information of the invoice\n\n")


invoice_number = 1  #* TODO: make this a commulative number  
duedate = input("\nDue date: (day month, year)")

from_addr = {
    'company_name': input("\nFrom: "),
    'addr1': input("\nAddress Line 1: (Street, Number)"),
    'addr2': input("\nAddress Line 2: (Postal-Code City)")
}

to_addr = {
    'company_name': input("\nTo: "),
    'client_name': input("\nClient Name: "),
    'client_email': input("\nClient Email: ")
}

items = []

print("Add the items to bill")
answer = input("Add another item?")
if answer:
    pass

#! TODO: FINISH THIS PART!!

user_data = {
    'duedate': duedate,

}




try: 
    html = requests.post(url, json=user_data)
    with open('invoice.pdf', 'wb') as f:
        f.write(html.content)
except:
    print("Connection failed")