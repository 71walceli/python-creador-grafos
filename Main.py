"""
    Programa principal. Coordina cada una de las ventanas, pasa los datosGrafo y realiza
validaciones.
"""

from Ventanas import CrearGrafo_matriz1, CrearGrafo_matriz2, VistaGrafo
from grafo import CAMPO_NODOS, CAMPO_MATRIZ, generarAristas

if __name__ == "__main__":
    # TODO Usar diccionario 
    datosGrafo = [[], False, False, [], []]
    """
        Estructura que contiene todos los datos que definen a un grafo: nodos, 
    aristas, vértices, tipo de grafo, matriz de adyacencia, entre otros.
    
    Propiedades:
        - lista de nodos  
        - bandera que indica si el grafo es dirigido  
        - bandera que indica si el grafo es ponderado  
        - matriz de adyacencia  
        - lista de aristas
    
        Debido a que esto es una referencia, los valores de este registro serán modificados por el 
    resto del programa. 
    """
    CrearGrafo_matriz1(datosGrafo)

    if len(datosGrafo[CAMPO_NODOS]) > 0:
        CrearGrafo_matriz2(datosGrafo)
    if datosGrafo[CAMPO_MATRIZ]:
        generarAristas(datosGrafo)
        VistaGrafo(datosGrafo)
