import numpy as np
import pandas as pd
import xlrd
from geopy.geocoders import Nominatim


df_ad = pd.read_excel(r'C:\Users\usiqu\PycharmProjects\SitelTaxi\endereço.xlsx')
chave = int(input('Digite o seu código da empresa: '))

while chave not in df_ad.ID.array:
    chave = int(input('Digite o seu código da empresa: '))

print(df_ad.loc[df_ad['ID'] == chave])
print('\n.-.-. Address validated .-.-.\n')


A = df_ad.loc[df_ad['ID'] == chave]
B = np.array(A)

for c in B:
    address = c[2]
    geolocator = Nominatim(user_agent='myGeocoder')
    location = geolocator.geocode(address)
    print((location.latitude, location.longitude))







'''for a in df_ad.ID.array:
    if a == chave:
        print('Yes', 'available in dataframe')
        print(df_ad.loc[df_ad['ID'] == a, 'endereço'])
    else:
        print('Código invalido')'''
