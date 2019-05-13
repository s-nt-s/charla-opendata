#!/usr/bin/env python3

import json

import requests
import urllib3

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()

url = "https://datos.gob.es/apidata/catalog/dataset.json?_pageSize=999"


def catalog(page=0):
    print(page, end="\r")
    r = requests.get(url+"&_page="+str(page), verify=False)
    js = r.json()
    items = js["result"]["items"]
    size = js["result"]["itemsPerPage"]
    if len(items) == size:
        items.extend(catalog(page+1))
    return items


items = catalog()

with open("catalog.json", "w") as f:
    f.write(json.dumps(items, indent=4))
