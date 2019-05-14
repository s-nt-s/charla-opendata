#!/usr/bin/env python3

import json
import os

import requests
import urllib3
from bunch import Bunch
from charts import save_pie

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

def mkBunch(data):
    if isinstance(data, str):
        data = read_data(data)
    r = {}
    keys={}
    for i in data:
        for k, val in i.items():
            tps = keys.get(k, set())
            tps.add(type(val))
            keys[k]=tps
    list_keys=set()
    l_type = type([])
    for k, tps in keys.items():
        if len(tps)>1 and l_type in tps:
            list_keys.add(k)
    for i in data:
        for k in list_keys:
            v = i.get(k, None)
            if v is None:
                i[k]=[]
            elif not isinstance(v, list):
                i[k]=[v]
        i = Bunch(**i)
        i._count=0
        i.id = i._about.split("/")[-1]
        r[i._about]=i
    return r

data = Bunch(**{
    s: mkBunch(s) for s in ("dataset", "distribution", "publisher", "spatial", "theme")
})
for i, v in data.items():
    print("%6s %s" % (len(v), i))



types = set()
for dataset in data.dataset.values():
    publisher = data.publisher[dataset.publisher]
    publisher._count = publisher._count + 1
    for spatial in dataset.spatial:
        spatial = data.spatial[spatial]
        spatial._count = spatial._count + 1

total = len(data.dataset.values())
save_pie("fig/total.png", "Datos por publicador", data.publisher, key=("agricultura", "yellowgreen"), minimo=92)
items = [d for d in data.publisher.values() if d["notation"][0]=="E"]
save_pie("fig/estatal.png", "Datos por publicador (estado)", items, key=("agricultura", "yellowgreen"), total=10)
