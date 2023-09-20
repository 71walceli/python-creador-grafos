
from itertools import combinations

from Ventanas import VistaGrafo
from grafo import *

if __name__ == '__main__':
    datosGrafo = [[], False, False, [], []]
    datosGrafo[CAMPO_NODOS]     = [chr(0x60+i) for i in range(1,2+1)]
    #datosGrafo[CAMPO_NODOS]     = [str(i) for i in range(1,2+1)]
    datosGrafo[CAMPO_DIRIGIDO]  = True
    datosGrafo[CAMPO_PONDERADO] = True
    datosGrafo[CAMPO_MATRIZ]    = [
        [1, 1],
        [1, 1],
    ]
    generarAristas(datosGrafo)
    #datosGrafo[CAMPO_ARISTAS]   = [
    #    ["B", "C", 100],
    #    ["A", 1C", 20],
    #]
    #1atosGrafo[CAMPO_ARISTAS]   = list(combinations(datosGrafo[CAMPO_NODOS], 2))
    #datosGrafo[CAMPO_ARISTAS]   = [list(arista)+[n +1] for n, arista in
    #                               enumerate(datosGrafo[CAMPO_ARISTAS])]
    ventana = VistaGrafo(datosGrafo)

