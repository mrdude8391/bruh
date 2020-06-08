import folium
import pandas

data = pandas.read_csv("volcano.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])

map = folium.Map(location=[40.960525, -102.106570], zoom_start=5)

fg = folium.FeatureGroup(name="boys")

for lt, ln, nm in zip(lat, lon, name):
    fg.add_child(folium.Marker(location=[lt, ln], popup=nm, icon=folium.Icon(color='red')))


fg.add_child(folium.Marker(location=[45.230996, -80.197866], popup="Hassan HQ", icon=folium.Icon(color='red')))
fg.add_child(folium.Marker(location=[45.231011, -80.198107], popup="Aidan INC", icon=folium.Icon(color='red')))

map.add_child(fg)

map.save("Map1.html")