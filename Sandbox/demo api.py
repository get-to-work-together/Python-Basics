
import requests

# or if that does not work

#import urllib.request

# or if you have Python 2.7

#import urllib2

city = 'Tokyo'

url = 'https://api.openweathermap.org/data/2.5/weather'
url += '?appid=d1526a9039658a6f76950cff21823aff'
url += '&mode=json'
url += '&units=metric'
url += '&q=' + city

print(url)

response = requests.get(url)

d = response.json()



#site = urllib.request.urlopen(url)
#response = str(site.read(), encoding = 'utf-8')
#
#import json
#d = json.loads(response)



#site = urllib2.urlopen(url)
#response = site.read().decode('utf-8')
#
#import json
#d = json.loads(response)


print('In Tokyo it is', d['main']['temp'])




