import requests
url = 'https://api.chucknorris.io/jokes/random'
data = requests.get(url).json()
print (data['value'])

