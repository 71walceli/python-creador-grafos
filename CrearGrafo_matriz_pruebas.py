from CrearGrafo_matriz import *

if __name__ == '__main__':
    datosTipoGrafo[CAMPO_NODOS]     = ["a", "b", "c"]
    datosTipoGrafo[CAMPO_DIRIGIDO]  = False
    datosTipoGrafo[CAMPO_PONDERADO] = False
    #datosTipoGrafo[CAMPO_MATRIZ]    = None
    CrearGrafo_matriz2(datosTipoGrafo)
    print(datosTipoGrafo[CAMPO_MATRIZ])
