import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

sum = 0
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
address = input('Enter location: ')

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
tree = ET.fromstring(data)

results = (tree.findall('comments/comment/count'))
for rt in results:
    count = count + 1
    sum = sum + int(rt.text)
print('Count:',count)
print('Sum:',sum)
