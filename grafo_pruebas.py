from grafo import generarAristas, CAMPO_ARISTAS

if __name__ == '__main__':
    datosGrafo = [
        ["a", "b"],
        True,
        True,
        [
            [1,2],
            [3,4],
        ],
    ]
    print(generarAristas(datosGrafo)[CAMPO_ARISTAS])

