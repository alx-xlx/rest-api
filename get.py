# -*- coding: utf-8 -*-
import requests

URL = "http://127.0.0.1:5002/employees/1"
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get(URL, headers=headers)
print(r.json())