import geocoder as gc # for coverting lat/long to country
import pandas as pd # to read excel files

# store data to variable
dataFile = pd.read_csv("Meteorite_Landings.csv", header=0)

reclat = list(dataFile.reclat)
reclong = list(dataFile.reclong)

# define country array
countryVar = []

for i in range(10):
    g = gc.osm([reclat[i], reclong[i]], method='reverse')
    temp = g.json['country']
    countryVar.append(temp)

print(countryVar)