from tkinter import Tk
from tkinter.ttk import Frame

from grafo import *
from ventanaGrafo import DibujoGrafo

if __name__ == '__main__':
    datosGrafo = [[], False, False, []]
    datosGrafo[CAMPO_NODOS]     = [str(i) for i in range(1,11)]
    datosGrafo[CAMPO_DIRIGIDO]  = False
    datosGrafo[CAMPO_PONDERADO] = False
    #datosGrafo[CAMPO_MATRIZ]    = None
    ventana = Tk()
    #ventana.geometry("200x200")
    marco = Frame(ventana)
    marco.pack()
    dibujo = DibujoGrafo(marco, datosGrafo, (300, 300))
    dibujo.pack()
    ventana.mainloop()
