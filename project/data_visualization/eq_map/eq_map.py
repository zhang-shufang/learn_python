import plotly.express as px
import pandas as pd
from pathlib import Path
import json

# Read data as string and convert it to dictionary
path = Path("eq_data/eq_data_30_day_m1.geojson")
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding='utf-8')    
all_eq_data = json.loads(contents)

# View the earthquake data of data set
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# Extract data we need
mags, titles, lons, lats = [], [], [], []
for dic in all_eq_dicts:
    mag = dic['properties']['mag']
    title = dic['properties']['title']
    lon = dic['geometry']['coordinates'][0]
    lat = dic['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])

# Zip data as panda data frame
data = pd.DataFrame(
    data=zip(lons, lats, titles, mags), columns=['经度', '纬度', '位置', '震级']
)

# Draw the scatter plot of earthquake
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    labels={'x': '经度', 'y':'纬度'},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title='全球地震散点图',
    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置'
)
fig.write_html('global_earthquakes.html')
fig.show()