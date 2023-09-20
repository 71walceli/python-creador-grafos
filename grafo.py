"""
    Módulo general con las definiciones como constantes, variables, clases y estructuras de datos de los grafos.
"""

CAMPO_NODOS     = 0
"""Índice a la lista de nodos"""
CAMPO_DIRIGIDO  = 1
"""Índice a la bandera que indica si el grafo es dirigido"""
CAMPO_PONDERADO = 2
"""Índice a la bandera que indica si el grafo es ponderado"""
CAMPO_MATRIZ    = 3
"""Índice a la matriz de adyacencia"""
CAMPO_ARISTAS   = 4
"""Índice a la lista de aristas"""


def generarAristas(datosGrafo: list):
    """
        Genera los aristas del grafo a partir de la matriz de adyacencia y las agrega a este
    registro.

        La lista de aristas consta de registros compuestos de la siguiente manera:

        - primer  nodo
        - segundo nodo
        - opcionalmente peso

    :param datosGrafo: registro de datos del grafo que debecontener la metriz de adyacencia
    """
    aristas = []    #   Lista de aristas
    nodos = datosGrafo[CAMPO_NODOS]
    matriz = datosGrafo[CAMPO_MATRIZ]

    for i in range(len(nodos)):     #   Agregar los aristas por debajo de la diagonal principal,
        for j in range(0, i + 1):   # único proceso cuando el grafo es no dirigido.
            if matriz[i][j] != 0:
                arista = [nodos[j], nodos[i]]
                aristas.append(arista)

    if datosGrafo[CAMPO_DIRIGIDO]:  #   Si el grafo es dirigido, agregar los aristas por encima de
        for i in range(len(nodos)): # la diagonal principal.
            for j in range(i + 1, len(nodos)):
                if matriz[i][j] != 0:
                    arista = [nodos[j], nodos[i]]
                    aristas.append(arista)

    if datosGrafo[CAMPO_PONDERADO]: #   Si el grafo es ponderado, agregar los pesos a cada arista.
        for arista in aristas:
            indice_i = nodos.index(arista[0])   #   índices para buscar el valor correspondiente en
            indico_j = nodos.index(arista[1])   # la matriz de adyacencia.
            arista.append(matriz[indice_i][indico_j])

    if len(datosGrafo) == CAMPO_ARISTAS +1:
        datosGrafo[CAMPO_ARISTAS] = aristas
    else:   # Añadir el campo en caso de no existir en la lista.
        datosGrafo.append(aristas)

