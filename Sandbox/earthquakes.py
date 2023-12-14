import json

filename = 'earthquakes.json'

with open(filename, encoding='utf-8') as f:

    data = json.load(f)

    for earthquake in data['features']:
        print(earthquake['properties']['place'],
              earthquake['properties']['type'],
              earthquake['properties']['mag'])
