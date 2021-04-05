# -*- coding: utf-8 -*-
import requests

# EmployeeID to get Details of
toGet = 1
URL = "http://127.0.0.1:5000/employees/"+str(toGet)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# use GET
r = requests.get(URL, headers=headers)
print(r.json())