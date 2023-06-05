import urllib.request
import urllib.parse
import urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter url: ')
print('Retrieving', url)

total = 0
count = 0

openURL = urllib.request.urlopen(url, context=ctx)
openURL = openURL.read().decode()

info = json.loads(openURL)
print(f'Retrieved { len(info)} characters: ')

data = info.get("comments")

for item in range(len(data)):

    value = data[item].get("count")
    count = count + 1
    total = total + int(value)

print("Count: ", count)
print("Total: ", total)
