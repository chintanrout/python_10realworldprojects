import folium
import pandas as pd

df = pd.read_csv("Volcanoes.txt")
df = pd.DataFrame(df)
print(df.head())
lat = list(df['LAT'])
lon = list(df["LON"])
elev =list(df["ELEV"])

def color_produce(elevation):
    if elevation <1000:
          return'green'
    elif 1000<=elevation <3000:
        return 'orange'
    else:
        return'red'
   


map = folium.Map(location =[38.58, -99.00], zoom_start= 6 )

fgv = folium.FeatureGroup(name = 'Volcanoes')

for lt,ln,el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location = [lt,ln], popup = str(el)+"m" ,  fill_color =  color_produce(el), radius =6,color = 'grey', fill_opacity = 0.7, fill = True))

fg = folium.FeatureGroup(name = 'Population')

fg.add_child(folium.GeoJson(data= open('world.json', 'r', encoding='utf-8-sig' ).read(),
style_function= lambda x: {'fillColor':'green' if x["properties"]['POP2005']<10000000 
else 'orange' if 10000000<= x["properties"]['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("Map1.html")


