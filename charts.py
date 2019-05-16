
import numpy as np

import matplotlib.pyplot as plt
# https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f

plt_colors = plt.rcParams['axes.prop_cycle'].by_key()['color']


def get_pct(pct, allvals):
    #absolute = int(pct/100.*np.sum(allvals))
    if pct<4:
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
        l = i.prefLabel[0] if isinstance(i.prefLabel, list) else i.prefLabel
        data[i.prefLabel]=i._count
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
    return labels, values, colors, explode

def save_pie(file, title, *agrv, **kargv):
    labels, values, colors, explode = get_counts(*agrv, **kargv)
    fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi= 80)
    patches, texts, autotexts = ax.pie(
        values,
        autopct='%1.1f%%', #lambda pct: get_pct(pct, values),
        pctdistance=1.1, labeldistance=1.2,
        textprops=dict(color="b"),
        colors=colors,
        startangle=90,
        explode=explode
    )
    lgd = ax.legend(patches, labels, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.setp(autotexts, size=10, weight=700)
    ax.set_title(title, y=-0.01)
    # plt.axis('equal')
    #plt.tight_layout()
    plt.savefig(file, bbox_extra_artists=(lgd,), bbox_inches='tight')
    plt.clf()
