import requests

city = 'Eindhoven'

url  = 'http://api.openweathermap.org/data/2.5/weather'
url += '?appid=d1526a9039658a6f76950cff21823aff'
url += '&units=metric'
url += '&mode=json'
url += '&lang=nl'
url += '&q=' + city

#print(url)

r = requests.get(url)

#print(r.status_code)

data = r.json()

#print(data)

temperature = data['main']['temp']

print(f'In {city} it is now {temperature} degrees.')
