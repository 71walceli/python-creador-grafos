"""
    Módulo general con las definiciones como constantes, variables, clases y estructuras de datos de los grafos.
"""

CAMPO_NODOS     = 0
CAMPO_DIRIGIDO  = 1
CAMPO_PONDERADO = 2
CAMPO_MATRIZ    = 3
CAMPO_ARISTAS   = 4


def generarAristas(datosGrafo):
    aristas = []
    nodos = datosGrafo[CAMPO_NODOS]

    for i in range(len(nodos)): #   Agregar los aristas por debajo de la diagonal principal.
        for j in range(0, i + 1):
            valor = datosGrafo[CAMPO_MATRIZ][i][j]
            if valor != 0:
                arista = [nodos[j], nodos[i]]
                aristas.append(arista)

    if datosGrafo[CAMPO_DIRIGIDO]:  #   Si el grafo es dirigido, agregar los aristas por encima de
        for i in range(len(nodos)): # la diagonal principal.
            for j in range(i + 1, len(nodos)):
                valor = datosGrafo[CAMPO_MATRIZ][i][j]
                if valor != 0:
                    arista = [nodos[j], nodos[i]]
                    aristas.append(arista)

    if datosGrafo[CAMPO_PONDERADO]:
        for arista in aristas:
            nodo_a = nodos.index(arista[0])
            nodo_b = nodos.index(arista[1])
            arista.append(datosGrafo[CAMPO_MATRIZ][nodo_a][nodo_b])

    if len(datosGrafo) == CAMPO_ARISTAS +1:
        datosGrafo[CAMPO_ARISTAS] = aristas
    else:
        datosGrafo.append(aristas)
    return datosGrafo


if __name__ == "__main__":
    listaNodos = ["a","b","c"]
    grafo = GrafoMatrizAdyacencia(listaNodos)
    grafo.conectarNodos("a","b")
    #grafo.desconectarNodos("a","b")
    grafo.agregarNodo("d")
    grafo.eliminarNodo("c")
    grafo.imprimirGrafo()
    print("Nodos   :", grafo.getNodos())
    print("Aristas :", grafo.getAristas())
