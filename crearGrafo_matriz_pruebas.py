from Ventanas import CrearGrafo_matriz2
from grafo import CAMPO_NODOS, CAMPO_DIRIGIDO, CAMPO_PONDERADO, \
    CAMPO_MATRIZ, generarAristas

if __name__ == '__main__':
    datosGrafo = [None for i in range(5)]
    datosGrafo[CAMPO_NODOS]     = ["a", "b", "c"]
    datosGrafo[CAMPO_DIRIGIDO]  = False
    datosGrafo[CAMPO_PONDERADO] = False
    #datosGrafo[CAMPO_MATRIZ]    = None
    CrearGrafo_matriz2(datosGrafo)
    generarAristas(datosGrafo)
    print(*datosGrafo, sep="\n")
