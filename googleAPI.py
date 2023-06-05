import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False

# in here it work on py4e json file because it has same json file like in real google api
# if you want to check it with google API you need to get API key from google and place it here
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    # http://py4e-data.dr-chuck.net/json?address=South+Federal+University&key=42
    # make new url with user entered location and api key

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    # using urlopen open newly create file on web

    data = uh.read().decode()
    # read all data nad decode it.
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
        # properly make json file help form inbuild libries
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    pid = js['results'][0]['place_id']
    print('Place id ', pid)
