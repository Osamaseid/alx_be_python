import xml.etree.ElementTree as ET

# Sample XML data
xml_data = '''<data>
                  <item>
                    <name>Alice</name>
                    <age>30</age>
                  </item>
                </data>'''

# Parse XML
root = ET.fromstring(xml_data)
for item in root.findall('item'):
    name = item.find('name').text
    age = item.find('age').text
    print(f"Name: {name}, Age: {age}")