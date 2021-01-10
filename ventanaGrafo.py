
import tkinter as tk
from math import sin, pi, cos
from random import randint
from tkinter import ttk

from crearGrafo_matriz import CAMPO_NODOS


def generarColorParcial(mínimo, máximo):
    """Genera un valor aleatorio hexadecimal para producir un color, entre un mínimo y un máximo
    dados."""
    return hex(randint(mínimo, máximo))[2:]

def generarColorRGB(mínimo, máximo):
    """
    Genera una cadena de color hexadecimal en RGB, entre un mínimo y un máximo dados, en el formato
    #RRGGBB, donde RR, GG y BB son un número hexadecimal, cada uno corresponde al valor de rojo,
    verde y azul, respectivamente
    """
    return "#"+"".join(generarColorParcial(mínimo, máximo) for i in range (3))\


class DibujoGrafo(ttk.Frame):
    def __init__(self, padre, datosGrafo, tamano, **kw):
        self.datosGrafo = datosGrafo
        self.padre          = padre
        self.ancho          = tamano[0]
        self.alto           = tamano[1]
        self.nodos          = []
        self.aristas        = []
        super().__init__(padre, **kw)

        self.area = tk.Canvas(self, bg="white", height=self.alto, width=self.ancho, borderwidth=0, **kw)
        self.area.grid(column=0, row=0)

        self.desplazamientoVertical   = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.area.yview)
        self.desplazamientoHorizontal = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.area.xview)
        self.desplazamientoVertical  .grid(column=1, row=0, sticky="NSW")
        self.desplazamientoHorizontal.grid(column=0, row=1, sticky="ESW")
        self.area.configure(
            xscrollcommand=self.desplazamientoHorizontal.set,
            yscrollcommand=self.desplazamientoVertical.set,
            #scrollregion=(0, 0, self.ancho, self.alto)
        )
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)

        nodos = self.datosGrafo[CAMPO_NODOS]
        self.dibujarNodos(nodos)
        self.bind("<Configure>", self.configurarDesplazamiento)
        self.bind("<Enter>", self.configurarDesplazamiento)

    def configurarDesplazamiento(self, event=None):
        """
            Configura las barras de sesplazamiento
        """
        self.area.config(scrollregion='0 0 %s %s' % (self.ancho, self.alto))
        if self.desplazamientoHorizontal.get() == (0.0, 1.0):   #   Si desplazamientoHorizontal
            self.desplazamientoHorizontal.grid_remove()         # abarca toda el área, quitarla
        else:   #   sino, poner desplazamientoHorizontal de nuevo y ajustar el área según espacio.
            self.config(width=self.area.winfo_reqwidth())
            self.desplazamientoHorizontal.grid()
        if self.desplazamientoVertical.get() == (0.0, 1.0):     #   La misma lógica para el
            self.desplazamientoVertical.grid_remove()           # desplazamientoVertical
        else:
            self.config(height=self.area.winfo_reqheight())
            self.desplazamientoVertical.grid()

    def dibujarNodos(self, nodos: list):
        """
            Dibuja cada uno de los nodos en un área, uno a uno, calculando las posiciones de cada
        una en relación al centro del área.
        """
        centro = self.area.winfo_reqwidth() / 2
        radio  = centro * .8
        ánguloMúltiplo = 2 * pi / len(nodos)
        for iNodo in range(len(nodos)):
            nodo = nodos[iNodo]
            ángulo = iNodo * ánguloMúltiplo
            x, y = centro + sin(ángulo) * radio, centro - cos(ángulo) * radio
            color = generarColorRGB(0xa0, 0xff)
            self.dibujarNodo(nodo, x, y, 25, fill=color, outline="white")
            #print(f"Nodo={nodos[iNodo]},posición={(x, y)},color={color}")

    def dibujarNodo(self, nodo, x, y, r, **kwargs):
        círculo = self.area.create_oval((x - r, y - r), (x + r, y + r), tag=nodo, **kwargs)
        self.area.create_text(x, y, text=nodo, tag=f"etiqueta_{nodo}")
        return círculo



