import numpy as np
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_excel(r'File pathway')
dfp = np.array(df)#Transformando os dados em uma matriz

kmeans = KMeans(n_clusters=4,#Número de cluster/agrupamento
                init = 'k-means++', n_init = 10,#Definir os pontos de distribuição de maneira mais assertiva
                max_iter=300)#Número de interação de cada loja
exec = kmeans.fit_predict(dfp)#Execução
plt.scatter(dfp[:,0], dfp[:,1], c=exec)#Definindo a posição de cada eixo [X e Y] dentro do arquivo Excel

plt.xlim(30, 60)#Definição do range de cada eixo
plt.ylim(-15,15)
plt.ylabel('Latitude')#Nomeando cada eixo
plt.xlabel('Longitude')
plt.grid()#Inserindo as grades do back do chart
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s=70, c='red')
#Posicionamento do centro de distruição
plt.show()#Mostrar o gráfico