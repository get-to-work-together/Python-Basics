import xml
import bs4

import xml.etree.ElementTree as ET

filename = 'group.html'

content = open(filename).read()

soup = bs4.BeautifulSoup(content, "html.parser")

names = [name.getText() for name in soup.findAll('span')]

for name in names:
    print(name)
