# -*- coding: utf-8 -*-
import requests

toDelete = 10
URL = "http://127.0.0.1:5000/employees/"+str(toDelete)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.delete(URL, headers=headers)
print(r.json())