# this script is meant to test the API to request a invoice

import requests

url = 'http://192.168.1.7:5000/' #your server url here

data = {
    'duedate': 'September 1, 2014',
    'from_addr': {
        'addr1': 'Hamilton, New York',
        'addr2': 'Sunnyville, CA 12345',
        'company_name': 'Python Tip'
    },
    'invoice_number': 156,
    'items': [{
            'charge': 500.0,
            'title': 'Brochure design'
        },
        {
            'charge': 85.0,
            'title': 'Hosting (6 months)'
        },
        {
            'charge': 10.0,
            'title': 'Domain name (1 year)'
        }
    ],
    'to_addr': {
        'company_name': 'hula hoop',
        'client_email': 'john@example.com',
        'client_name': 'Yasoob Khalid'
    }
}

html = requests.post(url, json=data)
with open('invoice.pdf', 'wb') as f:
    f.write(html.content)