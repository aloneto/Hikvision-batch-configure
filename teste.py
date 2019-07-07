import re
import requests
import base64
from requests.auth import HTTPDigestAuth
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

osd_set_text = """\
<?xml version="1.0" encoding="UTF-8"?>
<VideoOverlay>
   <TextOverlayList>
        <TextOverlay>
            <id>1</id>
            <enabled>true</enabled>
            <positionX>0</positionX>
            <positionY>0</positionY>
            <displayText>teste 01</displayText>
        </TextOverlay>
    </TextOverlayList>
</VideoOverlay>
"""

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



request = ElementTree.fromstring(osd_set_text)
requestntp = ElementTree.fromstring(ntp_set_request)
#print(request)

server_element = requestntp.find('NTPServer')
ip_element = server_element.find('ipAddress')
print(ip_element)
ip_element.text = '1010101'
print (ip_element)
print ("proxima fase")



master_element = request.find('TextOverlayList')
print(master_element)

text_element = master_element.find('TextOverlay')
id_element = text_element.find('id')
print(id_element)
id_element='10'

# master_element.text = '1'


