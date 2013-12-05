import requests
import lxml.html

url = "http://pcel.com/"
r = requests.get(url)
html = r.text.encode(r.encoding)

tree = lxml.html.fromstring(html)
box_product_list = tree.xpath('//div[@class="box-product"]')
for box_list in box_product_list:
    for box_product in box_list:
        name = box_product.find('.//div[@class="name"]/a')
        price = box_product.find('.//div[@class="price"]')

        name = name.text_content().replace('\n', ' ').replace('\r', '').strip()
        price = price.text_content().strip()
        print name, price
        print 
