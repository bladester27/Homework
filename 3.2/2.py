from xml.etree import ElementTree as ET

tree = ET.parse('test.xml')
root = tree.getroot()

name = root.findall('./person/first_name')
surname = root.findall('./person/last_name')

for values in zip(name, surname):
    row = {value.text for value in values}
    print(row)


