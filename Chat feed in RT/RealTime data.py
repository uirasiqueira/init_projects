import matplotlib.pyplot as plt
from matplotlib import animation
import pandas as pd

fig, ax = plt.subplots()

def animar(i):
    with open(r'C:\Users\usiqu\OneDrive\Documentos\dados.txt', 'r') as f:
        dados =f.read()

    x = []
    y = []
    for linha in dados.split('\n'):
        if len(linha) == 0:
            continue
        xi, yi = linha.split(',')
        x.append(float(xi))
        y.append(float(yi))
        ax.clear()
    ax.plot(x, y)
ani = animation.FuncAnimation(fig, animar, interval = 1000)
plt.show()
