import urllib.request, urllib.parse, urllib.error
import ssl
import json

sum = 0
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
address = input('Enter location: ')

uh = urllib.request.urlopen(address, context=ctx)
data = uh.read()
info = json.loads(data)

for item in info['comments']:
    count = count + 1
    sum = sum + item['count']
print('Count:',count)
print('Sum:',sum)
