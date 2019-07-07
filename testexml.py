import xml.etree.ElementTree as ET
import xml



tree = ET.parse('xml.xml')
root = tree.getroot()

print (root)

for child in root:
    print(child.tag, child.attrib,child.text)

    for textoverlay in child:
        print (textoverlay.tag,textoverlay.attrib,textoverlay.text)

        for itens in textoverlay:
            print(itens)
            id = itens.find('id')
            print (id)



