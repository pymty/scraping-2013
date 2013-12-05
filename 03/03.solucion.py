import requests
import lxml.html

def get(url):
    r = requests.get(url)
    return r.text.encode(r.encoding)

def get_earthquakes(tree):
    rows = tree.xpath('//div[@id="marcoTabla"]')
    earthquakes = []
    for row in rows:
        number = row.find('./div[@class="row1"]/a')
        if number is not None:
            fields = ["num", "date", "time", "lat", "lon", "deep", "mag", "place"]
            row = {field: row.find('./div[%d]' % index).text_content().strip() for index, field in enumerate(fields, start=1)}
            earthquakes.append(row)
    return earthquakes

def fancy(earthquake):
    formato = """
        Numero:      {num}
        Fecha:       {date}
        Hora:        {time}
        Latitud:     {lat}
        Longitud:    {lon}
        Profundidad: {deep}
        Magnitud:    {mag}
        Lugar:       {place}
    """
    return formato.format(**earthquake)

url = 'http://www.ssn.unam.mx/ultimos.html'
html = get(url)
tree = lxml.html.fromstring(html)
earthquakes = get_earthquakes(tree)
for earthquake in earthquakes:
    print fancy(earthquake)
