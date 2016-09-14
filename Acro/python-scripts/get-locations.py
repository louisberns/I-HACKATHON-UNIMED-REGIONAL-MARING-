import requests

base_url = 'http://maps.googleapis.com/maps/api/geocode/json'
my_params = {'address': 'Maringá',
             'language': 'pt-br'}
response = requests.get(base_url, params=my_params)
results = response.json()['results']
x_geo = results[0]['geometry']['location']

print(x_geo['lng'], x_geo['lat'])
