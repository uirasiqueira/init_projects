import numpy as np
import pandas as pd

file1 = pd.read_excel(r'INSIRA AQUI O CAMINHO DO ARQUIVO EM SUA MÁQUINA')
A = np.array(file1)#Library Numpy utilizada para transformar os dados dos arquivo em Excel em um array

chave = int(input('Digite o seu código da empresa: '))

y=0
while chave not in A[0]:
    chave = int(input('Código inválido. Digite novamente: '))
    y+=1

print('ID válido.')
