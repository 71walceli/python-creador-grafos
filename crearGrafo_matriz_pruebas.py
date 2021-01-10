from crearGrafo_matriz import *

if __name__ == '__main__':
    datosGrafo[CAMPO_NODOS]     = ["a", "b", "c"]
    datosGrafo[CAMPO_DIRIGIDO]  = True
    datosGrafo[CAMPO_PONDERADO] = True
    #datosGrafo[CAMPO_MATRIZ]    = None
    CrearGrafo_matriz2(datosGrafo)
    print(datosGrafo[CAMPO_MATRIZ])
