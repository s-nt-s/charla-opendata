import json
import os

import requests
import urllib3
from bunch import Bunch
import dateutil.parser
import bs4
import PyPDF2
import io
import re

urllib3.disable_warnings()
requests.packages.urllib3.disable_warnings()

re_url=re.compile(r"\bhttps?\s*://\s*\S+")
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


def read_data(name, _get_data=None, reload=False):
    file = dr+"/%s.json" % name
    if os.path.isfile(file) and not reload:
        with open(file, "r") as f:
            js = f.read()
            if _get_data is None:
                for old, new in dups_organismos:
                    js.replace(old, new)
            return json.loads(js)
    if _get_data is None:
        _get_data = get_data
    data = _get_data(name)
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

def get_pdf(url):
    r = requests.get(url, verify=False)
    with io.BytesIO(r.content) as pdf:
        read_pdf = PyPDF2.PdfFileReader(pdf)
        page = read_pdf.getPage(0)
        txt = page.extractText()
        urls=[]
        return txt, urls

        annotationList = []
        if read_pdf.annots:
            for annotation in page.annots.resolve():
                annotationDict = annotation.resolve()
                if str(annotationDict["Subtype"]) != "/Link":
                    # Skip over any annotations that are not links
                    continue
                position = annotationDict["Rect"]
                uriDict = annotationDict["A"].resolve()
                # This has always been true so far.
                assert str(uriDict["S"]) == "/URI"
                # Some of my URI's have spaces.
                uri = uriDict["URI"].replace(" ", "%20")
                annotationList.append((position, uri))
        print(annotationList)
        return txt, annotationList

def _get_examples(*args, **kargv):
    results=[]
    url = "https://www.europeandataportal.eu/es/using-data/use-cases?title=&body_value=&field_country_value=Spain&field_region_value=All&field_sector_value=All&field_type_of_use_case_value=reuse&page="
    url = "https://www.europeandataportal.eu/es/using-data/use-cases?title=&body_value=&field_country_value=All&field_region_value=All&field_sector_value=All&field_type_of_use_case_value=All&page="
    page = -1
    while True:
        page = page + 1
        r = requests.get(url+str(page), verify=False)
        soup = bs4.BeautifulSoup(r.content, "lxml")
        expls = soup.select("div.view-content div.views-row")
        if len(expls)==0:
            return results
        for ex in expls:
            data = {}
            a = ex.find("a")
            data["pdf"] = a.attrs["href"]
            title = a.get_text().strip()
            if title == "Romanian Railways":
                country, title= "Romania", "Railways"
            elif title == "Malta":
                country, title= "Malta", "Website"
            else:
                country, title = re.split(r"[\-–]", title, 1)
            data["title"]=title.strip()
            data["country"]=country.strip()
            sp = ex.select("span.date-display-single")[0]
            data["date"]=sp.attrs["content"][:10]
            data["img"]=ex.find("img").attrs["src"]
            for i in ex.select("div.views-field"):
                txt = i.get_text().strip()
                if ":" in txt:
                    f, v = txt.split(":",1)
                    f = f.strip().lower()
                    v = v.strip()
                    data[f]=v
            '''
            txt, urls = get_pdf(data["pdf"])
            m = re_url.search(txt)
            if m:
                data["url"]=m.group()
            '''
            results.append(data)

def get_examples():
    return read_data("examples", _get_data=_get_examples)

if __name__ == "__main__":
    l = len(get_examples())
    print(l)
