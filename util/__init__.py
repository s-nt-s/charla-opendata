import mimetypes

from urllib.parse import urlparse
import os

no_formato=set('''
aspx
php
asp
jsp
do
_Zaragoza
cgi
faces
action
dll
search
detalleDepartamento
'''.lower().split())

ok_formats=("pdf", "json", "csv", "xml", "ics")
fr_zip=("zip", "7z", "rar", "bz2", "gz")
key_fromats={
    "xls": "Microsoft Excel",
    "xlsx": "Microsoft Excel",
    "excel": "Microsoft Excel",
    "xlb": "Microsoft Excel",
    "mdb": "Microsoft Access",
    "geojson": "JSON",
    "jsonld": "JSON",
    "texto-plano": "Texto plano",
    "txt": "Texto plano",
    "bat": "Texto plano",
    "dgn": "AutoCAD",
    "dwg": "AutoCAD",
    "dxf": "AutoCAD",
    "jpg": "Imagen",
    "gif": "Imagen",
    "png": "Imagen",
    "jpe": "Imagen",
    "tif": "Imagen",
    "tiff": "Imagen",
    "ecw": "Imagen",
    "djvu": "Imagen",
    "vcf": "vCard",
    "csv_c": "CSV",
    "csv_sc": "CSV",
    "cvs": "CSV",
    "tsv": "CSV",
    "xlm": "XML",
    "outros": "XML",
    "atom": "XML",
    "rss": "XML",
    "tmx": "XML",
    "tbx": "XML",
    "xbrl": "XML",
    "marc": "XML",
    "mrc": "XML",
    "rdf": "RDF",
    "n3": "RDF",
    "rdf-xml": "RDF",
    "ttl": "RDF",
    "turtle": "RDF",
    "odt": "OpenDocument",
    "ods": "OpenDocument",
    "kmz": "Mapa",
    "kml": "Mapa",
    "gml": "Mapa",
    "wms": "Mapa",
    "wcs": "Mapa",
    "wfs": "Mapa",
    "gpx": "Mapa",
    "csw": "Mapa",
    "gdb": "Mapa",
    "las": "Mapa",
    "dbf": "dBase",
    "px": "PC-Axis",
    "docx": "Microsoft Word",
    "doc": "Microsoft Word",
    "sparql-xml": "SparQL",
    "rtf": "Rich Text Format",
    "shp": "ESRI Shapefile",
    "epub": "ePub",
    "elp": "eXeLearning",

}
mime_extension={
    "application/gml+xml": "gml",
    "text/plain": "txt",
    "text/ascii": "txt",
    "application/vnd.ms-excel": "xls",
    "application/x-zipped-shp": "shp",
    "application/pdf": "pdf",
    "application/sparql-results+json": "sparql-xml",
    "application/sparql-query": "sparql-xml",
    "application/sparql-results+xml": "sparql-xml",
    "application/vnd.geo+json": "json",
    "application/rss+xml": "rss",
    "application/vnd.ogc.wms_xml": "wms",
    "text/calendar": "ics",
    "application/ld+json": "json",
    "text/pc-axis": "px",
    "application/soap+xml": "xml",
    "text/xml+georss": "rss",
    "application/scorm": "elp",
    "application/x-tmx+xml": "tmx",
    "text/rdf+n3": "rdf",
    "application/x-turtle": "turtle",
    "x-lml/x-gdb": "gdb"
}

def parseExt(ext):
    if ext is None or len(ext)<3:
        return None
    ext = ext[1:].lower()
    if ext in no_formato:
        return None

    return ext

def get_ext(url):
    path = urlparse(url).path
    ext = os.path.splitext(path)[1]
    return ext.split("&")[0]

def get_format(mimetype, url, formats=None):
    if formats is None:
        formats = set()
    ext1 = get_ext(url)
    ext1 = parseExt(ext1)
    ext2 = \
        parseExt(mimetypes.guess_extension(mimetype)) or \
        mime_extension.get(mimetype, None) or \
        mimetype.split("/")[-1]
    if ext1 is None or ext1 in fr_zip:
        ext1 = ext2
    for ext in (ext1, ext2):
        if ext in ok_formats:
            return ext.upper()
        if ext in key_fromats:
            return key_fromats[ext]
    if mimetype.startswith("image/"):
        return "Imagen"
    return "<Indeterminado>" #mimetypes

def get_formats(mimetype, url, formats=None):
    if formats is None:
        formats = set()
    ext = parseExt(get_ext(url))
    if ext:
        formats.add(ext)
    ext = parseExt(mimetypes.guess_extension(mimetype))
    if ext:
        formats.add(ext)
    if mimetype == "application/pdf" and ext=="xls":
        print (url)
    return formats
