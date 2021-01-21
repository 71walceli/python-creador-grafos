"""
    Programa principal
"""

from Ventanas import CrearGrafo_matriz1, CrearGrafo_matriz2, VistaGrafo
from grafo import CAMPO_NODOS, CAMPO_MATRIZ, generarAristas

if __name__ == "__main__":
    datosGrafo = [[], False, False, []] #   Datos que `CrearGrado_matriz1` envía a la ventana para
                                        # definir la matriz.
    CrearGrafo_matriz1(datosGrafo)

    if len(datosGrafo[CAMPO_NODOS]) > 0:
        CrearGrafo_matriz2(datosGrafo)
    else:
        exit()
    if datosGrafo[CAMPO_MATRIZ] != []:
        datosGrafo = generarAristas(datosGrafo)
        VistaGrafo(datosGrafo)
