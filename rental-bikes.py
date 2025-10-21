import requests
import json
from datetime import datetime

def get_stations():
    url = 'https://api.wstw.at/gateway/WL_WIENMOBIL_API/1/station_information.json'

    response = requests.get(url, timeout=2)
    content = json.loads(response.content)

    stations = []

    for station in content['data']['stations']:
        stations.append(station)

    return stations

s = get_stations()
now = datetime.now()
now_formatted = now.strftime('%d.%m.%Y_%H:%M:%S')

with open('stations_' + now_formatted + '.json', 'w') as file:
    json.dump(s, file, indent=4)