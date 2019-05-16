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
