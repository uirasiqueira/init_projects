#Transformando endereço em coordenadas geográficas através da biblioteca geopy
import numpy as np
import pandas as pd
import xlrd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

file1 = pd.read_excel(r'INSIRA AQUI O CAMINHO DO ARQUIVO')
a = file1
A = np.array(a)
#O numpy irá transformar os dados do excel em uma lista. Cada lista também ser+a representada por uma outra lista Ex.:[[]]

for c in A:
    address = c[2]
    geolocator = Nominatim(user_agent='myGeocoder')
    location = geolocator.geocode(address)
    print((location.latitude, location.longitude))

