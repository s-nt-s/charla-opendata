#!/usr/bin/env python3

from data import mkData
from fig import save_pie
from bunch import Bunch
import mimetypes

from urllib.parse import urlparse
import os
import json


data = mkData()


def get_ext(url):
    path = urlparse(url).path
    ext = os.path.splitext(path)[1]
    return ext.split("&")[0]

#print (data.publisher["http://datos.gob.es/recurso/sector-publico/org/Organismo/E04990301"])

for dataset in data.dataset.values():
    publisher = data.publisher[dataset.publisher]
    publisher._count = publisher._count + 1
    for spatial in dataset.spatial:
        spatial = data.spatial[spatial]
        spatial._count = spatial._count + 1
    for theme in dataset.theme:
        theme = data.theme[theme]
        theme._count = theme._count + 1
t_format={}
formats={}
for distribution in data.distribution.values():
    frmt = distribution.format["value"]
    ts = set(t_format.get(frmt, []))
    ext = mimetypes.guess_extension(frmt)
    if ext:
        ts.add(ext+" <-----------")
    ext = get_ext(distribution.accessURL)
    if ext:
        ts.add(ext)
    t_format[frmt]=list(ts)
    print(mimetypes.guess_type(distribution.accessURL))

    f1, f2 = frmt.split("/", 1)
    if f1 in ("text", "application", "image"):
        frmt = f2
    if frmt.endswith(".kmz"):
        frmt = "kmz"
    formats[frmt] = formats.get(frmt, 0) + 1

with open("data/format.json", "w") as f:
    json.dump(t_format, f, indent=4)

formats=[Bunch(label=k, _count=v) for k, v in formats.items()]

total = len(data.dataset.values())
save_pie("fig/publisher.png", "Datos por publicador", data.publisher, key=("agricultura", "yellowgreen"), minimo=92)
items = [d for d in data.publisher.values() if d["notation"][0]=="E"]
save_pie("fig/publisher_E.png", "Datos por publicador (estado)", items, key=("agricultura", "yellowgreen"), total=10)

save_pie("fig/spatial.png", "Ámbito geográfico", data.spatial, key=("españa", "yellowgreen"), total=15)
save_pie("fig/theme.png", "Temas", data.theme)#, key=("españa", "yellowgreen"), total=15)

save_pie("fig/format.png", "Formatos", formats, total=30)#, key=("españa", "yellowgreen"), total=15)
