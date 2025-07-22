import folium
import pandas
my_map=folium.Map(location=[42.89175331289359, -78.83658372999396],zoom_start=6,tiles="CartoDB Dark_Matter")

#Another approach to adding childrens to map. Using feature groups.
#It makes code more modular
fg = folium.FeatureGroup(name="My Map")

my_file=pandas.read_csv("Volcanoes.txt")#Volcanoes.txt is a comma seperated file.
#my_file is a DataFrame object

lat=list(my_file['LAT']) 
lon=list(my_file.LON)
elev=list(my_file.ELEV)
name=list(my_file.NAME)

def color_choice(tall):
    if tall <= 2000.0:
        return "green"
    elif tall <= 3000.0:
        return "orange"
    else:
        return "red"

html="""Volcano:<br>
            <a href="https://www.google.com/search?q=%22{}%22",target="_blank">{}</a></br>
            Altitude: {}"""

for i,j,k,n in zip(lat,lon,elev,name):
    #iframe=folium.IFrame(html=html.format(n,n,k),width=200,height=100)
    #fg.add_child(folium.Marker(location=[i,j],popup=folium.Popup(html.format(n,n,k),width=200,height=100),icon=folium.Icon(color=color_choice(float(k)),icon='circle')))
    fg.add_child(folium.CircleMarker(location=[i,j],popup=folium.Popup(html.format(n,n,k),width=200,height=100),
                                     radius=6,fill_color=color_choice(k),color='black',fill_opacity=0.7)) 

fg2=folium.FeatureGroup("Second Layer")
file=open("world.json",'r',encoding='utf-8-sig')
fg2.add_child(folium.GeoJson(data=file.read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                                       else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                                       else 'red'}))

my_map.add_child(fg)
my_map.add_child(fg2)

#Below is Standard approach for adding markers in comments
#my_map.add_child(folium.Marker(location=[42.89175331289359, -78.83658372999396],popup="Hi I am marker",icon=folium.Icon("blue")))
my_map.add_child(folium.LayerControl())

my_map.save("Map1.html")