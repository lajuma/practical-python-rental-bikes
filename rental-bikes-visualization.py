import folium
import rental_bikes

data = rental_bikes.get_stations()

m = folium.Map(
    location = (48.210033, 16.363449),
    zoom_start = 12,
    min_zoom = 10,
    max_zoom = 18,
)

stations = folium.FeatureGroup('Bike Rental Stations')

for station in data:

    longitude=station['lon']
    latitude=station['lat']
    name=station['name']
    popup = 'name: ' + name + '\n' + 'longitude: ' + str(longitude) + '\n' + 'latitude: ' + str(latitude)

    folium.Marker(
        location=[latitude, longitude],
        tooltip=name,
        popup=popup,
        icon=folium.Icon(color='darkblue', icon='bike', prefix='fa')
    ).add_to(stations)

stations.add_to(m)

m.save("map/stations_map.html")