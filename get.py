# -*- coding: utf-8 -*-
import requests

URL = "http://127.0.0.1:5000/employees/1"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.get(URL, headers=headers)
print(r.json())