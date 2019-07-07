import re
import requests
import base64
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree as ET
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

osd_set_text = """\
<?xml version="1.0" encoding="UTF-8" ?>
<VideoOverlay>
    <attribute>
    	<transparent>false</transparent>
    	<flashing>false</flashing>
    </attribute>
    	<fontSize>2</fontSize>
    <TextOverlayList>
        <TextOverlay>
            <id>1</id>
            <enabled>true</enabled>
            <positionX>500.000000</positionX>
            <positionY>32.000000</positionY>
            <displayText>01</displayText>
        </TextOverlay>
        <TextOverlay>
            <id>2</id>
            <enabled>true</enabled>
            <positionX>0.000000</positionX>
            <positionY>32.000000</positionY>
            <displayText>02</displayText>
        </TextOverlay>
        <TextOverlay>
            <id>3</id>
            <enabled>true</enabled>
            <positionX>500.000000</positionX>
            <positionY>160.000000</positionY>
            <displayText>03</displayText>
        </TextOverlay>
        <TextOverlay>
            <id>4</id>
            <enabled>true</enabled>
            <positionX>500.000000</positionX>
            <positionY>320.000000</positionY>
            <displayText>04</displayText>
        </TextOverlay>
        <TextOverlay>
            <id>5</id>
            <enabled>true</enabled>
            <positionX>200.000000</positionX>
            <positionY>64.000000</positionY>
            <displayText>05</displayText>
        </TextOverlay>
        <TextOverlay>
            <id>6</id>
            <enabled>true</enabled>
            <positionX>400.000000</positionX>
            <positionY>176.000000</positionY>
            <displayText>06</displayText>
        </TextOverlay>
    </TextOverlayList>
</VideoOverlay>"""

ntp_set_request = """\
<?xml version="1.0" encoding="UTF-8"?>
<NTPServerList>
    <NTPServer>
        <id>1</id>
        <addressingFormatType>ipaddress</addressingFormatType>
        <ipAddress>1.1.1.1</ipAddress>
        <portNo>123</portNo>
        <synchronizeInterval>60</synchronizeInterval>
    </NTPServer>
</NTPServerList>
"""

"""

request = ElementTree.fromstring(osd_set_text)


master_element = request.find('TextOverlayList')
print(master_element)

text_element = master_element.find('TextOverlay')
id_element = text_element.find('id')
print(id_element)
id_element='10'

a =request.iter(id)
print(a)
"""

tree = ET.parse('xml.xml')
root = tree.getroot()
print (root)


for text in root.iter('displayText'):
    print (text)
    text.text = 'novo texto'
    print (text)



b"<?xml version='1.0' encoding='utf8'?>\n<VideoOverlay>\n    <attribute>\n    \t<transparent>false</transparent>\n    \t<flashing>false</flashing>\n    </attribute>\n    \t<fontSize>4</fontSize>\n    <TextOverlayList>\n        <TextOverlay>\n            <id>1</id>\n            <enabled>true</enabled>\n            <positionX>0.000000</positionX>\n            <positionY>560.000000</positionY>\n            <displayText>texto</displayText>\n        </TextOverlay>\n        <TextOverlay>\n            <id>2</id>\n            <enabled>true</enabled>\n            <positionX>0.000000</positionX>\n            <positionY>500.000000</positionY>\n            <displayText>texto</displayText>\n        </TextOverlay>\n        <TextOverlay>\n            <id>3</id>\n            <enabled>true</enabled>\n            <positionX>0.000000</positionX>\n            <positionY>460.000000</positionY>\n            <displayText>texto</displayText>\n        </TextOverlay>\n        <TextOverlay>\n            <id>4</id>\n            <enabled>true</enabled>\n            <positionX>0.000000</positionX>\n            <positionY>410.000000</positionY>\n            <displayText>texto</displayText>\n        </TextOverlay>\n        <TextOverlay>\n            <id>5</id>\n            <enabled>true</enabled>\n            <positionX>0.000000</positionX>\n            <positionY>360.000000</positionY>\n            <displayText>texto</displayText>\n        </TextOverlay>\n        <TextOverlay>\n            <id>6</id>\n            <enabled>true</enabled>\n            <positionX>0.000000</positionX>\n            <positionY>310.000000</positionY>\n            <displayText>texto</displayText>\n        </TextOverlay>\n    </TextOverlayList>\n</VideoOverlay>"



"""
for video in root.findall('TextOverlayList'):
    rank = video.find('id').text
    #name = rank.get('TextOverlay')
    print(rank)


"""