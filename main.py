#import required libraries
import pandas as pd
import folium
# autoviz for automated exploratory data analysis
from autoviz import AutoViz_Class

#reading the file using pandas and cleaning it
data= pd.read_csv("Meteorite_Landings.csv")
target=data.GeoLocation[0:20000]
locations=target.dropna()

#creating a blank world map
m=folium.Map()

# pointin the location markers:
for location in locations:
    location=location[1:-2].split(',')
    lat=location[0]
    lon=location[1]
    folium.CircleMarker([lat,lon],radius=1,fill=True,opticity=1.0,color='red').add_to(m)
    
# get the map

m

# for EDA using  autoviz library
AV = AutoViz_Class()
df = AV.AutoViz("Meteorite_Landings.csv")
