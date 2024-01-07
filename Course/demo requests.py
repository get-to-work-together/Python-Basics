import requests

city = input('Which city? : ')

url = 'https://api.openweathermap.org/data/2.5/weather?'
url += 'appid=d1526a9039658a6f76950cff21823aff&'
url += 'units=metric&'
url += 'mode=json&'
url += 'q=' + city

response = requests.get(url)

if response.status_code == 200:

    d = response.json()

    temperature = d['main']['temp']

    print(f'It is now {temperature} degrees in {city}.')

