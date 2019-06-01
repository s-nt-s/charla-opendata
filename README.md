<p class="nota" style="text-align: right;">Este es el guión de una charla
sobre `Open Data` impartida en el `Ministerio de agricultura, pesca y alimentación`</p>

# ¿Cómo ha de ser un dato abierto y por qué?

## ¿Qué es un dato abierto?

<blockquote cite="http://opendefinition.org">
<p>Un dato abierto es aquel que puede ser usado, modificado y compartido libremente por cualquiera y para cualquier propósito.</p>
<footer>
-- <cite> <a href="http://opendefinition.org/od/2.1/es/">opendefinition</a></cite>
</footer>
</blockquote>

Esto significa muchas cosas, pero si tuviera que elegir me quedaría con que:

* ha de ser de fácil acceso
* ha de ser legible por máquina
* ha de estar en un formato abierto
* no se debe incurrir en ningún coste por su uso

## ¿Por qué?

Los motivos éticos son los que encuentro más interesantes, pero como creo que es obvio
porque un dato creado con fondos públicos ha de ser abierto saltaré directamente
a los motivos económicos, que quizá son menos obvios.

Han de recordar que todo lo que llevamos hablado en estas jornadas depende no solo de una gran cantidad de datos para realizarse si no también de la combinación de diversas fuentes. El coste asociado a tener que tratar con datos cerrados, yendo caso por caso buscando su acceso, adecuándolo para que sea legible, comprando licencias, etc, etc, conlleva una barrera que impediría muchos de los proyectos posibles con datos abiertos.

Proyectos que crean riqueza. ¿Cuánta? Según la consultora McKinsey estamos hablando de entre 3 y 5 billones (millón de millones) de dolares al año.

<figure class="withCaption">
  <img src="https://www.mckinsey.com/~/media/McKinsey/Business%20Functions/McKinsey%20Digital/Our%20Insights/Open%20data%20Unlocking%20innovation%20and%20performance%20with%20liquid%20information/SVG_Open_data_Exhibit.ashx" alt="Open data can help unlock $3 trillion to $5 trillion in economic value annually across seven sectors" title="Open data can help unlock $3 trillion to $5 trillion in economic value annually across seven sectors">
  <figcaption>Open data can help unlock $3 trillion to $5 trillion in economic value annually across seven sectors<br/>
  <a href="https://www.mckinsey.com/business-functions/digital-mckinsey/our-insights/open-data-unlocking-innovation-and-performance-with-liquid-information">mckinsey.com</a></figcaption>
</figure>

Incluso podríamos decir que esta es una estimación a la baja ya que no incluye todos los tipos de datos abiertos, lo que nos lleva a:

## ¿Qué tipos de datos abiertos hay?

Hay muchas posibles clasificaciones, pero voy a usar los tres grandes grupos que identifica el [Open Data Barometer](https://Open Databarometer.org):

* Innovación
* Política social
* Rendición de cuentas

Los proyectos de innovación son los que normalmente nos vienen a la mente: cómo mejorar la eficiencia de nuestros procesos, reducir costes, crear nuevos productos, etc. Son los que crean puestos de trabajo y crecimiento económico, pero como la propia `Open Data Barometer` reconoce eso no significa que vaya a beneficiar a toda la población, por ello son especialmente importantes los datos de Política social y Rendición de cuentas que si impactan directamente en que los beneficios lleguen a todas las capas de la sociedad.

# Open Data en España

# Open Data Barometer

Según el `Open Data Barometer` España ocupa el undécimo puesto en el ranking mundial y el quinto en el europeo:

<figure class="withCaption">
  <img src="fig/barometer1.png" alt="Los primeros de cada región en la cuarta edición del Barómetro, con sus respectivas posiciones y puntuaciones generales" title="Los primeros de cada región en la cuarta edición del Barómetro, con sus respectivas posiciones y puntuaciones generales">
  <figcaption>Los primeros de cada región en la cuarta edición del Barómetro, con sus respectivas posiciones y puntuaciones generales<br/>
  <a href="https://opendatabarometer.org/4thedition/report/?lang=es">opendatabarometer.org/4thedition/</a></figcaption>
</figure>

Este informe nos dice que tenemos un buen volumen de datos y vamos en buena dirección, pero también nos dice (a nosotros y la resto de países) que queda mucho por hacer.

No en vano solo el 7% de de los supuestos `datos abiertos` son realmente abiertos, es decir, cumplen los requisitos que apuntábamos al principio. Si entramos más al detalle podemos ver que:

<figure class="withCaption">
  <img src="fig/barometer2.png" alt="Detalle de España en Open Data Barometer" title="Detalle de España en Open Data Barometer">
  <figcaption>Detalle de España en Open Data Barometer<br/>
  <a href="https://opendatabarometer.org/4thedition/detail-country/?_year=2016&indicator=ODB&detail=ESP">opendatabarometer.org/4thedition/</a></figcaption>
</figure>

Como en la mayoría de países la asignatura pendiente son los datos referentes a la rendición de cuentas (presupuestos y gasto público) aunque hay una buena base para la innovación y la política social.

## datos.gob.es

Para ver más de cerca los datos que disponemos en España he analizado el portal de datos abiertos datos.gob.es por ser de ámbito generalista, aunque hay que tener en cuenta que hay muchos más.

En este portal tenemos 22.353 dataset, los cuales están compuestos de uno o más ficheros, en los que se abarcan las siguientes temáticas:

<figure class="withCaption">
  <img src="fig/theme.png" alt="Dataset de datos.gob.es por temas" title="Dataset de datos.gob.es por temas">
  <figcaption>Dataset de datos.gob.es por temas<br/>
  <a href="https://datos.gob.es/apidata/catalog/theme.json?_pageSize=999">datos.gob.es</a></figcaption>
</figure>

Si lo comparamos con la anterior grafica llama la atención que `Open Data Barometer` nos dice que los mejores datos están en Justicia pero en datos.gob.es no aparecen hasta el puesto 18º. Esto es por la diferencia de calidades entre distintos tipos de datos ya que `Open Data Barometer` no estará considerando como abiertos muchos
dataset que aparecen en datos.gob.es, y que posiblemente sean de otros temas.

A menudo el problema es el formato:

<figure class="withCaption">
  <img src="fig/format.png" alt="Dataset de datos.gob.es por formato" title="Dataset de datos.gob.es por formato">
  <figcaption>Dataset de datos.gob.es por formato<br/>
  <a href="https://datos.gob.es/apidata/catalog/distribution.json?_pageSize=999">datos.gob.es</a></figcaption>
</figure>

Baste ver que abundan los formatos privativos y que el según do más usado es `PDF`.

Además, a menudo los mejores datos están directamente publicados en los organismos de origen en vez de en portales como datos.gob.es

En cuanto al peso de cada organismo en el conjunto total de los datos tenemos que:

<figure class="withCaption">
  <img src="fig/publisher.png" alt="Dataset de datos.gob.es por publicador" title="Dataset de datos.gob.es por publicador">
  <figcaption>Dataset de datos.gob.es por publicador<br/>
  <a href="https://datos.gob.es/apidata/catalog/publisher.json?_pageSize=999">datos.gob.es</a></figcaption>
</figure>

el País Vasco es el líder absoluto, seguido del gobierno de Aragón y el Instituto geológico y minero de España. Mientras que el Ministerio de Agricultura se encuentra relativamente atrás, aunque hay que tener en cuenta que aún así esta en el primer tercio del ranking y que son los ayuntamientos y comunidades, mas cercanos a los ciudadanos, los que más datos están abriendo.

De hecho si juntamos todos los datos estatales el País Vasco y Aragón seguirían por delante.

<figure class="withCaption">
  <img src="fig/spatial.png" alt="Dataset de datos.gob.es por ámbito geográfico" title="Dataset de datos.gob.es por ámbito geográfico">
  <figcaption>Dataset de datos.gob.es por ámbito geográfico<br/>
  <a href="https://datos.gob.es/apidata/catalog/spatial.json?_pageSize=999">datos.gob.es</a></figcaption>
</figure>

y si solo nos fijamos en los organismos estatales vemos:

<figure class="withCaption">
  <img src="fig/publisher_E.png" alt="Dataset de datos.gob.es por publicador (solo estatal)" title="Dataset de datos.gob.es por publicado (solo estatal)">
  <figcaption>Dataset de datos.gob.es por publicador (solo estatal)<br/>
  <a href="https://datos.gob.es/apidata/catalog/publisher.json?_pageSize=999">datos.gob.es</a></figcaption>
</figure>

que Agricultura esta en el puesto 6, y es el 2º ministerio (lo demás que esta por delante son organismos autónomos).

## Nuestra experiencia

Para muestro proyecto hemos visto confirmadas muchos de los puntos que se encuentran en el informe del `Open Data Barometer`:

* Los datos demográficos (INE) y cartográficos (Fomento, Miteco, Agricultura) son probablemente los más completos y mejor estructurados. Adicionalmente también hemos visto que los datos de AEMET son muy completos y accesibles.
* Más información en los portales de los organismos que en datos.gob.es aunque este portal sigue siendo útil para de ahí saltar a otros portales.
* Una gran cantidad de datos potencialmente interesantes pero de difícil uso por no ser realmente abiertos. Especialmente por problemas de formato (`pdf`), estandarizan o falta de históricos.
* Los datos que tienen que ver con rendición de cuentas son los más difíciles de encontrar, si es que existen.

En particular quiero señalar los problemas que hemos tenido con los datos de la renta:

* La AEAT solo tienen datos de municipios de más de 1000 habitantes y no abarca País Vasco y Navarra
* El País Vasco tiene datos de todos los municipios
* Navarra solo de municipios de más de 2000 habitantes
* Todos usan unidades de medida diferentes

En la AEAT el denominador de la media es el número de declaraciones, en el País Vasco es el número de habitantes de más de 18 años, y en Navarra no esta claro pero parece que tiene que ver con el promedio de integrantes por familia.

De manera que aunque parece que podremos transformar los datos de la AEAT y el País Vasco para que sean comparables, los de Navarra tendrán que quedarse fuera.

Es por esto que no solo importan los datos, si no también los metadatos que los describen.

Hasta aquí hemos hablado de calidad objetiva, pero cuando abordemos un proyecto tambien nos interesara la calidad
subjetiva, es decir, aquello que necesitamos para nuestro negocio. Este es un ejemplo para nuestro
proyecto sobre incendios:

<figure class="withCaption">
  <img src="fig/egif.png" alt="Incendios con coordenadas geográficas" title="Incendios con coordenadas geográficas">
  <figcaption>Incendios con coordenadas geográficas<br/>
  <a href="https://www.mapa.gob.es/es/desarrollo-rural/estadisticas/Incendios_default.aspx">www.mapa.gob.es</a></figcaption>
</figure>

Aquí medimos la calidad de los datos en función de cuantos de ellos tienen coordenadas
geográficas porque es lo que interesa para nuestro proyecto, sin embargo, si nos bastará
con simplemente saber el municipio tendríamos una gráfica totalmente diferente
que rozaría el 100% en toda su extensión.

Esta gráfica se entempreta de la siguiente manera:

Si inicio mi estudio desde finales del 68, solo podre usar el 40% de los incendios, pero si tomamos como fecha de inicio 1999 tendríamos ya un dataset bastante bueno pudiendo usar hasta un 80%, y si solo tomamos desde 2009 el dataset ya sería prácticamente perfecto.

Lo cual habla muy bien de este conjunto de datos, sobretodo si tenemos en cuenta que solo hemos encontrado datos demográficos posteriores a 1996, de paro desde 2006, empresariales desde 2012 y tributarios desde 2013 (a excepción del País Vasco, que tiene desde el 97). Incluso la AEMET no proporciona históricos más allá de 1975.

Finalmente, hay que reseñar que pese a los muchos puntos a mejorar para que los datos abiertos sean abiertos de verdad, la ventaja y en enriquecimientos que proporcionan es ya evidente. Si estos datos no fueran abiertos, aunque pensáramos que eventualmente pudiéramos llegar a un acuerdo con sus propietarios para usarlos, lo más probable es que el proyecto hubiera muerto antes de poder arrancar.

En definitiva, disponer de datos abiertos supone ponerse a trabajar en crear valor desde el primer momento, sin entretenerse en:

* Adquirir licencias
* Coordinar organismos
* Esperar plazos impuestos desde fuera
* Lidiar con leyes de protección de datos u otras
* Dedicar tiempo y personal a burocracia
* Obtener permisos
* etc.

# Ejemplos de uso

Casi todos los portales abiertos incluyen una sección donde podéis ver proyectos y aplicaciones que usan sus datos, así que aquí solo daremos una pequeña muestra centrándonos en casos curiosos o que usan una abanico amplio de fuentes.

## DataM

[DataM](https://datam.jrc.ec.europa.eu/datam/public/pages/index.xhtml?rdr=1558003808561) es una iniciativa del Centro Común de Investigación de la Comisión Europea (JRC, Joint Research Centre) para difundir datos sobre aspectos económicos de la agricultura y que han sido generados a partir de sus actividades científicas.

En concreto cubre:

* agricultura
* la bioeconomía
* cambio climático
* seguridad alimentaria y nutricional
* sostenibilidad

Utiliza datos a nivel de:

* Unión europea
* Países miembros
* entidades locales

En esta herramienta podemos ver un ejemplo de como la combinación de datos puede suplir la ausencia de uno de ellos. Este seria el caso del consumo anual de productos agrarios, que Eurostat dejo de recoger y publicar, y que esta herramienta suple mediante la medición del consumo anual aparente, que es una estimación calculada a partir de otros datos disponibles.

Permite

* La descarga de los datos originales en formato reutilizable
* Filtrar y buscar entre esos datos desde la propia web
* Visualizar los datos en dashboards en la propia web

## Global Forest Watch

Global Forest Watch (GFW) es una plataforma que tiene como objetivo monitorizar los bosques de todo el planeta casi en tiempo real con el fin de protegerlos.

En concreto cubre:

* clima
* incendios
* materias primas
* agua

Usa datos de:

* la NASA (MODIS y VIIRS)
* Google
* USAID (Agencia de los Estados Unidos para el Desarrollo Internacional)
* Universidad de Maryland
* Esri (Empresa de  Sistemas de Información Geográfica)
* Vizzuality (empresa de visualización de datos y web-gis)

Permite:

* Crear dashboard para, por ejemplo, hacer seguimientos de regiones (ejemplo: [Madrid](https://www.globalforestwatch.org/dashboards/country/ESP/8?category=summary))
* Proporciona una API para construir aplicaciones que consuman sus datos
* Permite la descarga de todos sus mapas

## Más

Para hacernos una idea más general he analizado las casi 500 aplicaciones que
lista el portal de datos abiertos de la Unión Europea agrupándolas por sector:

<figure class="withCaption">
  <img src="fig/examples.png" alt="Aplicaciones por sector" title="Aplicaciones por sector">
  <figcaption>Aplicaciones por sector<br/>
  <a href="https://www.europeandataportal.eu/es/using-data/use-cases?title=&body_value=&field_country_value=All&field_region_value=All&field_sector_value=Agriculture%2C%20Fisheries%2C%20Forestry%20%26%20Foods&field_type_of_use_case_value=All">www.europeandataportal.eu</a></figcaption>
</figure>

En ella vemos el peso de cada sector en el conjunto total, siendo el azul para
Europa y el rojo para España.

Los sectores en la que la barra roja es especialmente más larga que la azul significan
que en España las empresas encuentran más datos abiertos con los que crear sus aplicaciones
sobre esos sectores de lo que encuentran en el conjunto de Europa.

En el caso contrario salta a la vista el sector Transporte, el cual es considerado
un punto muy importante para posibilitar proyectos de innovación, que como ya se
vislumbraba en los datos de `Open Data Barometer` están especialmente mal en España.

Por otro lado, a pesar de que los valores del sector Turismo son prácticamente iguales
en España y Europa, llama la atención su actual estado teniendo en cuenta el peso
de este sector en nuestro país y que en la lista de temas de datos.gob.es el Turismo
se encontraba en la primera mitad. Esto nos indica que estos datos han de tener
muy poca calidad.

# Deberes para casa

Lecturas recomendadas:

* Informes de OpenData barometer:
    * [Informe global 4º edición](https://opendatabarometer.org/4thedition/report/?lang=es)
    * [Informe de la promesa al progreso](https://opendatabarometer.org/leadersedition/report/?lang=es)
* Informe [Cómo los datos abiertos pueden impulsar el sector agrícola y forestal](https://datos.gob.es/es/documentacion/como-los-datos-abiertos-pueden-impulsar-el-sector-agricola-y-forestal) de datos.gob.es

Acciones imprescindibles:

* Aprenderse el [estándar de 5 estrellas](https://5stardata.info/es/), de Tim Berners-Lee (inventor de la Web)
* Abrir tus datos
