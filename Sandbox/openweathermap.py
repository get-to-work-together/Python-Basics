import json
import urllib.request

city = input('Which city? ')

url = 'http://api.openweathermap.org/data/2.5/weather'
url += '?appid=d1526a9039658a6f76950cff21823aff'
url += '&units=metric'
url += '&mode=json'
url += '&q=' + city

print(url)

site = urllib.request.urlopen(url)
r = str(site.read(), encoding = 'utf-8')

d = json.loads(r)

temperature = d['main']['temp']

print(f'It is now {temperature} degrees in {city}.')