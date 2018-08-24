import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# xsize = np.array([100, 1000, 10000])
# ytime = np.array([0, 0.005, 0.01])

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

def plota_grafico(result_binary, result_indexed, result_sentinel, result_simple):
    plt.ylabel('time')
    plt.xlabel('size')
    plt.plot(result_simple, color='pink')
    plt.plot(result_sentinel, color='blue')
    plt.plot(result_indexed, color='red')
    plt.plot(result_binary, color='green')
    plt.show()

"""
Escolha um contexto:

1. Análise de tempo entre algoritmos (definir algoritmos)
2. Análise de vídeo mais requisitado (definir algoritmos) SÒ SE DER TEMPO
0. Sair

"""
