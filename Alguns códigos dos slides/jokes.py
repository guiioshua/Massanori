from urllib.request import Request, urlopen
import json

req = Request(
    url='https://api.chucknorris.io/jokes/random', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
resp = urlopen(req).read()
data = json.loads(resp.decode('utf-8'))

print (data['value'])
