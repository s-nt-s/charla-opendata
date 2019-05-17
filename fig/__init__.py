import numpy as np

import matplotlib.pyplot as plt
import re
import datetime

re_min =  re.compile(r"^[0123]\.")

# https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f

plt_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
lb_es = ("Medio ambiente", "Sector público", "Sociedad y bienestar",
    "Cultura y ocio", "Educación", "Hacienda", "Salud",
    "Turismo", "Transporte", "Economia", "Demografía",
    "Ciencia y tecnología", "Medio rural", "Comercio", "Empleo",
    "Legislación y justicia", "Energía", "Seguridad", "Deporte")

void = lambda x: x
def cond(val, lnt=4, r1=void, r2=void):
    print(val)
    if val<lnt:
        return r1(val)
    return r2(val)

def get_label(i):
    if "label" in i:
        return i.label
    if isinstance(i.prefLabel, list):
        count=1
        label=None
        for l in i.prefLabel:
            if l in lb_es:
                i.prefLabel = l
                return l
            if i.prefLabel.count(l)>count:
                count = i.prefLabel.count(l)
                label = l
        i.prefLabel = l if l else i.prefLabel[0]
    return i.prefLabel

def get_pct(pct, max):
    #absolute = int(pct/100.*np.sum(allvals))
    if pct<max:
        return ""
    return "{:.1f}%".format(pct)

def get_counts(items, minimo=None, total=None, key=None):
    if not isinstance(items, list):
        items = items.values()
    color_key = None
    if key is not None:
        if isinstance(key, str):
            color_key="red"
        else:
            key, color_key = key
    labels=[]
    values=[]
    c_otros=0
    m_otros=0
    data = {}
    i_key = None
    for i in items:
        if minimo and i._count<minimo:
            c_otros = c_otros + i._count
            m_otros = m_otros + 1
            continue
        label = get_label(i)
        data[label]=i._count
    i = 0
    line = "%"+str(len(str(len(data))))+"sº %s"
    for label, value in sorted(data.items(), key=lambda x: (-x[1], x[0])):
        if total and i>=total:
            c_otros = c_otros + value
            m_otros = m_otros + 1
            continue
        if key and key in label.lower():
            i_key = i
        i = i + 1
        labels.append(line % (i, label))
        values.append(value)
    colors = plt_colors[:]
    if len(colors)<len(labels):
        colors = colors * (int(len(labels)/len(colors))+1)
    colors = colors[0:len(labels)]
    if c_otros:
        labels.append("Otros (%s)" %(m_otros))
        values.append(c_otros)
        colors.append("black")
    explode = (0.0, ) * len(labels)
    if i_key:
        colors[i_key]=color_key
        explode = list(explode)
        explode[i_key]=0.1
        explode = tuple(explode)
    return labels, values, colors, explode, i_key

def save_pie(file, title, *agrv, **kargv):
    labels, values, colors, explode, i_key = get_counts(*agrv, **kargv)
    fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)
    patches, texts, autotexts = ax.pie(
        values,
        autopct='%1.1f%%',
        #autopct=lambda pct: get_pct(pct, 4),
        #pctdistance=cond,
        #pctdistance=0.7,
        labeldistance=1.2,
        #textprops=dict(color="b"),
        textprops=dict(color="w"),
        colors=colors,
        startangle=90,
        explode=explode
    )
    lgd = ax.legend(patches, labels, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    for i, t in enumerate(autotexts):
        if re_min.search(t.get_text()):
            if i==i_key:
                d=1.7
                xi, yi = t.get_position()
                ri = np.sqrt(xi**2+yi**2)
                phi = np.arctan2(yi,xi)
                x = d*ri*np.cos(phi)
                y = d*ri*np.sin(phi)
                t.set_position((x,y))
                t.set_color("black")
            else:
                t.set_text("")
    plt.setp(autotexts, size=10, weight=700)
    ax.set_title(title, y=-0.01)
    # plt.axis('equal')
    #plt.tight_layout()
    plt.savefig(file, bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.clf()


def save_quality(file, title, data):
    dates = []
    values = []
    for o in data:
        dates.append(o.fecha)
        values.append(o.ok*100/o.total)

    plt.plot(dates,values)
    plt.title(title)
    #plt.ylabel("%")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(file)
    plt.clf()


def bar_compare(file, title, labels, ori, res, legend=None):
    if legend is None:
        legend = ('Original', 'HTML')
    ind = np.arange(len(labels))

    width = 0.35

    plt.rcdefaults()
    fig, ax = plt.subplots()
    rects1 = ax.barh(ind - width / 2, ori, width, color='b')
    rects2 = ax.barh(ind + width / 2, res, width, color='r')

    ax.set_title(title)
    ax.set_yticks(ind)
    ax.set_yticklabels(labels)
    plt.xlabel("% sobre el total")

    ax.legend((rects1[0], rects2[0]), legend)

    plt.tight_layout()
    plt.savefig(file)
    plt.clf()

def save_pie2(file, title, data):
    sectors={}
    total_es = sum(1 if d["country"]=="Spain" else 0 for d in data)
    total_eu = len(data)
    for d in data:
        if not d.get("sector", None):
            continue
        for sector in d["sector"]:
            sector = get_es(sector)
            total, spa = sectors.get(sector, (0, 0))
            total = total + 1
            if d["country"]=="Spain":
                spa = spa + 1
            sectors[sector]=(total, spa)

    vals_eu = []
    vals_es = []
    labels = []
    otros = 0
    otros_es = 0
    for sector, ts in sorted(sectors.items(), key=lambda x: (-x[1][0], -x[1][1], x[0])):
        total, spa = ts
        if total<4 and False:
            otros = otros + 1
            otros_es = otros_es + 1
            continue
        labels.append(sector)
        vals_eu.append(total*100/total_eu)
        vals_es.append(spa*100/total_es)
        print(total, spa, sector)

    if otros and False:
        labels.append("Otros")
        vals.append((otros, otros_es))
        vals_eu.append(otros)
        vals_es.append(otros_es)
        print(otros, otros_es)

    bar_compare(file, title, labels, vals_eu, vals_es, legend=("Europa", "España"))

    return

    fig, ax = plt.subplots()

    size = 0.3
    vals = np.array(vals)

    cmap = plt.get_cmap("tab20c")
    outer_colors = cmap(np.arange(3)*4)
    inner_colors = cmap(np.array([1, 2, 5, 6, 9, 10]))

    #patches, texts, autotexts =
    patches, texts = ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
           wedgeprops=dict(width=size, edgecolor='w'),
           startangle=90,
           #autopct='%1.1f%%',
           labels=labels)

    ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
           wedgeprops=dict(width=size, edgecolor='w'),
           startangle=90,
           #autopct='%1.1f%%'
           )

    ax.set(aspect="equal", title=title)

    #lgd = ax.legend(patches, labels, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    plt.tight_layout()
    plt.savefig(file, bbox_extra_artists=(texts,), bbox_inches='tight')#, bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.clf()

def get_es(s):
    if s=="Government & Public Sector":
        return "Gobierno y sector público"
    if s=="Transport":
        return "Transporte"
    if s=="Science & Technology":
        return "Ciencia y tecnología"
    if s=="Economy & Finance":
        return "Economía y finanzas"
    if s=="Environment":
        return "Medio ambiente"
    if s=="Regions & Cities":
        return "Regiones y ciudades"
    if s=="Education":
        return "Educación"
    if s=="Culture & Sport":
        return "Cultura y deporte"
    if s=="Health":
        return "Salud"
    if s=="Agriculture":
        return "Agricultura"
    if s=="Fisheries":
        return "Pesca"
    if s=="Forestry & Foods":
        return "Bosques y alimentación"
    if s=="Population & Society":
        return "Población y sociedad"
    if s=="Justice":
        return "Justicia"
    if s=="Legal System & Public Safety":
        return "Sistema legal y seguridad pública"
    if s=="Energy":
        return "Energía"
    if s=="Tourism":
        return "Turismo"
    if s=="International Issues":
        return "Asuntos internacionales"
    return s
