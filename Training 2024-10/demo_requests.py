import requests

city = input('Which city? : ')

url = 'http://api.openweathermap.org/data/2.5/weather?appid=d1526a9039658a6f76950cff21823aff&units=metric&mode=json&q=' + city

response = requests.get(url)

if response.status_code == 200:

    d = response.json()

    temperature = d['main']['temp']

    print(f'It is {temperature} in {city}')

else:
    print('Cannot open url')