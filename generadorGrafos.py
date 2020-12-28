from math import ceil


class grafoMatrizAdyacencia:
    """Grafo no dirigido y no ponderado, cuya representación interna es una matriz de adyacencia."""
    def __init__(self, nodos):
        tamaño = len(nodos)
        self.__nodos  = list(set(nodos))  # Elimina duplicados.
        self.__matriz = [[0 for i in range(tamaño)] for j in range(tamaño)]

    def imprimirGrafo(self):
        print("\t" +"\t".join(self.__nodos))
        for iNodo in range(len(self.__nodos)):
            print(str(self.__nodos[iNodo]) + "\t" + "\t".join(str(celda) for celda in self.__matriz[iNodo]))

    def conectarNodos(self, nodoA, nodoB):
        if nodoA not in self.__nodos or nodoB not in self.__nodos:
            print(f"ADVERTENCIA: nodo {nodoA if nodoA not in self.__nodos else nodoB} no existe. No habrá "
                  f"ningún efecto.")
            return
        grafo_i = self.__nodos.index(nodoA)
        grafo_j = self.__nodos.index(nodoB)
        self.__matriz[grafo_i][grafo_j] = 1
        self.__matriz[grafo_j][grafo_i] = 1

    def desconectarNodos(self, nodoA, nodoB):
        if nodoA not in self.__nodos or nodoB not in self.__nodos:
            print(f"ADVERTENCIA: nodo {nodoA if nodoA not in self.__nodos else nodoB} no existe. No habrá "
                  f"ningún efecto.")
            return
        grafo_i = self.__nodos.index(nodoA)
        grafo_j = self.__nodos.index(nodoB)
        self.__matriz[grafo_i][grafo_j] = 0
        self.__matriz[grafo_j][grafo_i] = 0

    def agregarNodo(self, nodo):
        if nodo in self.__nodos:
            print(f"Advertencia: {nodo} ya es un vértice de este grafo. No habrá ningún efecto.")
            return
        self.__nodos.append(nodo)
        for fila in self.__matriz:
            fila.append(0)  # Agrega un cero en cada fila, el cual corresponde al nodo nuevo.
        self.__matriz.append([0 for i in range(len(self.__nodos))]) # Última fila, para el nodo nuevo.

    def eliminarNodo(self, nodo):
        if nodo not in self.__nodos:
            print(f"Advertencia: {nodo} no es un vértice de este grafo. No habrá ningún efecto.")
            return
        índiceNodo = self.__nodos.index(nodo)
        del self.__nodos[índiceNodo]    # Borra este nodo de la lista de nodos de este grafo.
        del self.__matriz[índiceNodo]   # Borra la fila correspondiente al nodo en cuestión.
        for fila in self.__matriz:
            del fila[índiceNodo]  # Elimina la columna correspondiente a este nodo.

    def getNodos(self):
        return self.__nodos

    # TODO Hacerlo por lista en forma de comprensión.
    def getAristas(self):
        aristas = []
        for i in range(len(self.__nodos)):  # En una gráfica no dirigida, basta con recorrer por
            for j in range(0, i+1):         #   encima o por debajo de la diagonal principal,
                #   incluyéndola, para poder determinar cada uno de
                #   los pares de nodos que forman un vértice.
                if self.__matriz[i][j] != 0:
                    aristas.append((self.__nodos[j], self.__nodos[i]))  # Devolver los nodos en este
                    #   orden, procurando que
                    #   se dén de forma
                    #   organizada.
        return aristas

if __name__ == "__main__":
    listaNodos = ["a","b","c"]
    grafo = grafoMatrizAdyacencia(listaNodos)
    grafo.conectarNodos("a","b")
    #grafo.desconectarNodos("a","b")
    grafo.agregarNodo("d")
    grafo.eliminarNodo("c")
    grafo.imprimirGrafo()
    print("Nodos   :", grafo.getNodos())
    print("Aristas :", grafo.getAristas())
