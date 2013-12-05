#encoding: utf-8
import requests
from lxml import etree

def get(url):
    r = requests.get(url)
    html = r.text
    return html.encode(r.encoding)

def get_pk(row):
    pk = row.find('.//span[@class="price-tax"]')
    if pk is not None:
        return pk.text[5:]

def get_description(row):
    return ''.join(row.find('.//div[@class="name"]/a').itertext()).strip().replace('\r', '\n')

def get_new_price(row):
    new_price = row.find('.//div[@class="price-new"]')
    return new_price.text

def get_old_price(row):
    old_price = row.find('.//div[@class="price-old"]')
    return old_price.text

def update_products(tree, products):
    x_rows = '//*[@id="content"]/div[5]/table/tr'
    for number, row in enumerate(tree.xpath(x_rows)):
        if number % 2 == 1: continue
        pk = get_pk(row)
        description = get_description(row)
        old_price = get_old_price(row)
        new_price = get_new_price(row)
        product = {
            'pk': pk,
            'description': description,
            'old_price': old_price,
            'new_price': new_price,
        }
        products[pk] = product

def get_next_url(tree):
    # TODO: Objetivo implementar esta funcion
    pass

def fancy(product):
    formato = u"""
        ID:              {pk}
        Descripcion:     {description}
        Precio anterior: {old_price}
        Precio nuevo:    {new_price}
    """
    return formato.format(**product)
    

next_url = 'http://pcel.com/computadoras/laptops-notebooks'
products = {}
while next_url:
    html = get(next_url)
    tree = etree.HTML(html)
    update_products(tree, products)
    next_url = get_next_url(tree)

for product in products.values():
    print fancy(product)
print "{0} productos encontrados".format(len(products))
