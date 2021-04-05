# -*- coding: utf-8 -*-
import requests
import json

URL = "http://127.0.0.1:5000/employees"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

newData = {
    'Address': '11120 Jasper Ave NW',
    'BirthDate': '1962-02-18 00:00:00',
    'City': 'Edmonton',
    'Country': 'Canada',
    'Email': 'andrew@chinookcorp.com',
    'EmployeeId': None,
    'Fax': '+1 (780) 428-3457',
    'FirstName': '123Andrew',
    'LastName': 'Adamsssss',
    'HireDate': '2002-08-14 00:00:00',
    'Phone': '+1 (780) 428-9482',
    'PostalCode': 'T5K 2N1',
    'ReportsTo': None,
    'State': 'AB',
    'Title': 'General Manager'
    }

r = requests.post(URL, data = json.dumps(newData), headers=headers)
print(r.json())