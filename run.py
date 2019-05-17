#!/usr/bin/env python3

from data import mkData, get_egif, get_examples
from fig import save_pie, save_quality, save_pie2
from bunch import Bunch
from util import get_formats, get_format


import os
import json

#egif = get_egif()
#save_quality("fig/egif.png", "% de calidad", egif)

data = mkData()

examples=get_examples()
print(len(examples))
save_pie2("fig/examples.png", "Aplicaciones por sector", examples)

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
    mimetype, url = distribution.format["value"], distribution.accessURL
    frmt = get_format(mimetype, url)
    if frmt is None:
        ts = set(t_format.get(mimetype, []))
        ts = get_formats(mimetype, url, ts)
        t_format[mimetype]=list(ts)
        frmt = mimetype
    formats[frmt] = formats.get(frmt, 0) + 1

with open("data/format.json", "w") as f:
    json.dump(t_format, f, indent=4)

formats=[Bunch(label=k, _count=v) for k, v in formats.items()]

total = len(data.dataset.values())
print(total)
save_pie("fig/publisher.png", "Datos por publicador", data.publisher, key=("agricultura", "yellowgreen"), minimo=92)
items = [d for d in data.publisher.values() if d["notation"][0]=="E"]
save_pie("fig/publisher_E.png", "Datos por publicador (estado)", items, key=("agricultura", "yellowgreen"), total=10)

save_pie("fig/spatial.png", "Ámbito geográfico", data.spatial, key=("españa", "yellowgreen"), total=15)
save_pie("fig/theme.png", "Temas", data.theme)

save_pie("fig/format.png", "Formatos", formats, total=30)
