#!/usr/bin/env python3

import json
import os

import requests
import urllib3
from bunch import Bunch

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()


def get_size(url):
    try:
        d = requests.head(url, verify=False)
        return d.headers.get('content-length', None)
    except:
        return None


def get_json(url):
    r = requests.get(url, verify=False)
    js = r.json()
    return js["result"]


def get_data(name):
    url = "https://datos.gob.es/apidata/catalog/%s.json?_pageSize=999&_page=" % name
    count = 0
    page = -1
    items = []
    line = "> %s: %s %s"
    while True:
        page = page + 1
        _url = url+str(page)
        js = get_json(_url)
        items.extend(js["items"])
        print(line % (name, len(items), _url), end="\r")
        if len(js["items"]) < js["itemsPerPage"]:
            print(line % (name, len(items), _url))
            return items


def read_data(name):
    file = "data/%s.json" % name
    if os.path.isfile(file):
        with open(file, "r") as f:
            return json.load(f)
    data = get_data(name)
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
    return data


data = Bunch(**{
    s: read_data(s) for s in ("dataset", "distribution", "publisher", "spatial", "theme")
})
for i, v in data.items():
    print("%6s %s" % (len(v), i))

types = set()
for dataset in data.dataset:
    distribution = dataset.get("distribution", None)
    if distribution:
        print(dataset["title"])
        if isinstance(distribution, dict):
            distribution = [distribution]
        for dis in distribution:
            byteSize = dis.get("byteSize", None)
            if byteSize is None:
                dis["byteSize"] = get_size(dis["accessURL"])
            if byteSize:
                print(dis["format"]["value"], byteSize)
