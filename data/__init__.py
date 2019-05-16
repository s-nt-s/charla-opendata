import json
import os

import requests
import urllib3
from bunch import Bunch
import dateutil.parser

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()


me = os.path.realpath(__file__)
dr = os.path.dirname(me)

dups_organismos= (
    ("E05024401", "E04990301"), # Agricultura new -> old
    ("E05024701", "E04990301") # MITECO -> Agricultura old
)

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
    file = dr+"/%s.json" % name
    if os.path.isfile(file):
        with open(file, "r") as f:
            js = f.read()
            for old, new in dups_organismos:
                js.replace(old, new)
            return json.loads(js)
    data = get_data(name)
    with open(file, "w") as f:
        json.dump(data, f, indent=4)
    return data


def mkBunch(name):
    data = read_data(name)
    keys_list = {}
    for d in data:
        for k, v in d.items():
            tps = keys_list.get(k, set())
            tps.add(type(v))
            keys_list[k]=tps
    l_type = type([])
    keys_list = set(t for t, v in keys_list.items() if len(v) > 1 and l_type in v)
    dict_data={}
    for d in data:
        for k in keys_list:
            v = d.get(k, None)
            if v is None:
                d[k]=[]
            elif not isinstance(v, list):
                d[k]=[v]
        _about = d["_about"]
        d = Bunch(**d)
        d._count = 0
        d.id = _about.split("/")[-1]
        dict_data[_about] = d
    return dict_data


def mkData():
    data = Bunch(**{
        s: mkBunch(s) for s in ("dataset", "distribution", "publisher", "spatial", "theme")
    })
    return data

def get_egif():
    with open(dr+"/egif.json", "r") as f:
        js = json.load(f)
    js = list(sorted(js, key= lambda x: x["fecha"]))
    l = len(js) -1
    for i, o in reversed(list(enumerate(js))):
        o = Bunch(**o)
        if i<l:
            o.total = o.total + js[i+1].total
            o.ok = o.ok + js[i+1].ok
        o.fecha = dateutil.parser.parse(o.fecha)
        js[i] = o
    return js
