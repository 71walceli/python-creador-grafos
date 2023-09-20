
from tkinter import Tk
from tkinter.ttk import Frame
from itertools import combinations

from grafo import *
from Ventanas import DibujoGrafo

if __name__ == '__main__':
    datosGrafo = [[], False, False, [], []]
    datosGrafo[CAMPO_NODOS]     = [chr(0x40+i) for i in range(1, 12+1)]
    datosGrafo[CAMPO_DIRIGIDO]  = True
    datosGrafo[CAMPO_PONDERADO] = True
    datosGrafo[CAMPO_MATRIZ]    = []
    datosGrafo[CAMPO_ARISTAS]   = [
        ["B", "D", 100],
        ["A", "D", 20],
    ]
    datosGrafo[CAMPO_ARISTAS]   = list(combinations(datosGrafo[CAMPO_NODOS], 2))
    datosGrafo[CAMPO_ARISTAS]   = [list(arista)+[n +1] for n, arista in
                                   enumerate(datosGrafo[CAMPO_ARISTAS])]
    print(datosGrafo[CAMPO_ARISTAS])
    ventana = Tk()
    #ventana.geometry("200x300")
    marco = Frame(ventana)
    marco.pack()
    dibujo = DibujoGrafo(marco, datosGrafo, 700)
    dibujo.pack()
    ventana.mainloop()
