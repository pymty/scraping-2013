import requests
import lxml.html

def get(url):
    r = requests.get(url)
    return r.text.encode(r.encoding)

def get_earthquakes(tree):
    # TODO: Implementar
    return []

def fancy(earthquake):
    # TODO: Implementar
    return ""

url = 'http://www.ssn.unam.mx/ultimos.html'
html = get(url)
tree = lxml.html.fromstring(html)
earthquakes = get_earthquakes(tree)
for earthquake in earthquakes:
    print fancy(earthquake)
