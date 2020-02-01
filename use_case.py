import pandas as pd
import folium as fl

dataset=pd.read_csv('/home/hindu/Desktop/python/ml learn/vehicles.csv')

# print(dataset)

print('dataset shape',dataset.shape)

print('dataset description',dataset.describe())

print(dataset.ndim)


map=fl.Map(location=[10.23654,99.62535],zoom_start=2)

fg=fl.FeatureGroup(name='Volacano')

for coordinate in ([38.2,-99.1],[33.58,-98.09]):
    fg.add_child(fl.Marker(location=coordinate,popup='I M marker ',icon=fl.Icon(color='red')))


map.add_child(fg)
map.save('First_folium.html')
print(map)