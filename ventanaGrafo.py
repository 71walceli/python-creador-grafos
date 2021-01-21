
import tkinter as tk
from math import sin, pi, cos, atan2, sqrt
from random import randint, random
from tkinter import ttk

from grafo import CAMPO_ARISTAS, CAMPO_NODOS, CAMPO_PONDERADO, CAMPO_DIRIGIDO


def generarColorRGB(mínimo, máximo):
    """
        Devuelve una cadena de color hexadecimal en RGB, entre un mínimo y un máximo dados, en el
    formato #RRGGBB, donde RR, GG y BB son un número hexadecimal, cada uno corresponde al valor de
    rojo, verde y azul, respectivamente
    :param mínimo: Mínimo valor hexadecimal (color más oscuro)
    :param máximo: Mínimo valor hexadecimal (color más claro)
    :return: cadena de color hexadecimal en RGB.
    """
    def generarColorParcial(mínimo, máximo):
        """
            Genera un valor aleatorio hexadecimal para producir un color, entre un mínimo y un
        máximo dados.
        :param mínimo: Mínimo valor hexadecimal (color más oscuro)
        :param máximo: Mínimo valor hexadecimal (color más claro)
        """
        return hex(randint(mínimo, máximo))[2:].rjust(2,"0")
    return "#"+"".join(generarColorParcial(mínimo, máximo) for i in range (3))


class DibujoGrafo(ttk.Frame):
    """
        Extensión de ttk.Frame que tiene la graficación de un grafo.
    """
    def __init__(self, padre, datosGrafo, tamano, **kw):
        self.radio_nodos = 25
        self.datosGrafo  = datosGrafo
        """
            Estructura que contiene todos los datos para definir que definen a un grafo: nodos, 
        aristas, vértices, tipo de grafo, matriz de adyacencia, entre otros.
        """
        self.padre       = padre
        self.ancho       = self.alto = tamano
        self.nodos       = []
        self.aristas     = []
        super().__init__(padre, **kw)

        self.area = tk.Canvas(self, bg="white", height=self.alto, width=self.ancho, borderwidth=0, **kw)
        self.area.grid(column=0, row=0)

        self.desplazamientoVertical   = ttk.Scrollbar(self, orient=tk.VERTICAL,
                                                      command=self.area.yview)
        self.desplazamientoHorizontal = ttk.Scrollbar(self, orient=tk.HORIZONTAL,
                                                      command=self.area.xview)
        self.desplazamientoVertical  .grid(column=1, row=0, sticky="NSW")
        self.desplazamientoHorizontal.grid(column=0, row=1, sticky="ESW")
        self.area.configure(
            xscrollcommand=self.desplazamientoHorizontal.set,
            yscrollcommand=self.desplazamientoVertical.set,
        )
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 0, weight=1)

        self.ancho, self.alto = self.area.winfo_reqwidth(), self.area.winfo_reqheight()
        self.altoMinimo       = self.alto  -self.desplazamientoHorizontal.winfo_height()
        self.anchoMinimo      = self.ancho -self.desplazamientoVertical.winfo_width()
        self.centro           = min(self.ancho, self.alto) / 2
        #self.radioInterno     = self.centro -1.5*max(self.desplazamientoHorizontal.winfo_height(),
        #                                             self.desplazamientoVertical.winfo_width()) \
        #                        -2.5*self.radio_nodos
        self.radioInterno     = self.centro -2.5*self.radio_nodos

        self.dibujar()
        self.bind("<Configure>", self.configurarDesplazamiento)
        #self.master.update_idletasks()
        self.padre.bind("<Configure>", self.configurarDesplazamiento)
        #self.bind("<Enter>", self.configurarDesplazamiento)

    def configurarDesplazamiento(self, event=None):
        """
            Configura las barras de sesplazamiento
        """
        #print("x:", self.desplazamientoHorizontal.get())
        if (self.winfo_width() >= self.ancho):          #   Si desplazamientoHorizontal
            self.desplazamientoHorizontal.grid_remove() # abarca toda el área, quitarla
            self.area["height"] = self.alto
        else:   #   sino, poner desplazamientoHorizontal de nuevo y ajustar el área según espacio.
            self.config(width=self.area.winfo_reqwidth())
            self.desplazamientoHorizontal.grid()
            self.area["height"] = self.altoMinimo

        #print("y:", self.desplazamientoVertical.get())
        if (self.winfo_height() >= self.alto):
            self.desplazamientoVertical.grid_remove()           # desplazamientoVertical
            self.area["width"] = self.ancho
        else:
            self.config(height=self.area.winfo_reqheight())
            self.desplazamientoVertical.grid()
            self.area["width"] = self.anchoMinimo

        #print(self.winfo_geometry())
        self.area.config(scrollregion='0 0 %s %s' % (self.anchoMinimo, self.altoMinimo))

    def dibujar(self):
        """
            Dibuja cada uno de los nodos en un área, uno a uno, en disposición poligonal..
        """
        nodos             = self.datosGrafo[CAMPO_NODOS]
        ánguloMúltiplo = 2 * pi / len(nodos)
        for iNodo in range(len(nodos)):
            nodo = nodos[iNodo]
            ángulo = iNodo * ánguloMúltiplo
            x, y = self.centro + sin(ángulo) * self.radioInterno, self.centro - cos(ángulo) * self.radioInterno
            color = generarColorRGB(0xa0, 0xff)
            self.dibujarNodo(nodo, x, y, self.radio_nodos, fill=color, outline="white")

        aristas = self.datosGrafo[CAMPO_ARISTAS]
        for arista in aristas:
            self.dibujarArista(arista)


    def dibujarNodo(self, nodo, x, y, r, **kwargs):
        círculo = self.area.create_oval((x - self.radio_nodos, y - self.radio_nodos),
                                        (x + self.radio_nodos, y + self.radio_nodos),
                                        tag=nodo, **kwargs)
        self.area.create_text(x, y, text=nodo, tag=f"{nodo}.nombre")


    def dibujarArista(self, arista):
        nodo_a = arista[0]
        nodo_b = arista[1]
        coords_a = self.area.bbox(nodo_a)
        coords_b = self.area.bbox(nodo_b)

        centro_a = (coords_a[0] +self.radio_nodos +1, coords_a[1] +self.radio_nodos +1)
        centro_b = (coords_b[0] +self.radio_nodos +1, coords_b[1] +self.radio_nodos +1)

        angulo_a = atan2(centro_a[1] -centro_b[1], centro_a[0] -centro_b[0])
        angulo_b = angulo_a +2*pi

        color    = generarColorRGB(0x00, 0xb0)
        etiqueta = f"{nodo_a}-{nodo_b}"

        inicio = (
            centro_a[0] -cos(angulo_a)*(self.radio_nodos -3),
            centro_a[1] -sin(angulo_a)*(self.radio_nodos -3),
        )
        fin = (
            centro_b[0] +cos(angulo_b)*(self.radio_nodos -3),
            centro_b[1] +sin(angulo_b)*(self.radio_nodos -3),
        )

        if nodo_a == nodo_b:
            centro_a = (centro_a[0] +0.3*self.radio_nodos, centro_a[1] -0.3*self.radio_nodos)
            puntos_n = 7
            puntos = [(
                centro_a[0] -0.5*cos(pi *i*2/puntos_n) *self.radio_nodos,
                centro_a[1] -0.5*sin(pi *i*2/puntos_n) *self.radio_nodos
            ) for i in range(puntos_n)]
            self.area.create_line(puntos, smooth=True, tag=etiqueta, fill=color)

            if self.datosGrafo[CAMPO_PONDERADO]:
                peso = arista[2]
                posicionPeso = centro_a
                self.area.create_text(posicionPeso, text=str(peso), fill="white",
                                      tag=f"{etiqueta}.peso")

                self.area.create_rectangle(self.area.bbox(f"{etiqueta}.peso"), fill=color,
                                           outline=color, tag=f"{etiqueta}.peso.borde")
                self.area.tag_raise(f"{etiqueta}.peso")
        else:
            self.area.create_line(inicio, fin, smooth=True, tag=etiqueta, fill=color)

            if self.datosGrafo[CAMPO_PONDERADO]:
                peso = arista[2]

                modulo = (sqrt((inicio[0] -fin[0])**2+ (inicio[1] -fin[1])**2)
                          )
                multiplo = 0.55 +random()*0.25
                posicionPeso = (
                    inicio[0] - cos(angulo_a) *modulo *multiplo,
                    inicio[1] - sin(angulo_a) *modulo *multiplo,
                )

                self.area.create_text(posicionPeso, text=str(peso), fill="white",
                                      tag=f"{etiqueta}.peso")

                self.area.create_rectangle(self.area.bbox(f"{etiqueta}.peso"), fill=color,
                                           outline=color, tag=f"{etiqueta}.peso.borde")
                self.area.tag_raise(f"{etiqueta}.peso")

        if self.datosGrafo[CAMPO_DIRIGIDO]:
            self.area.itemconfigure(etiqueta, arrow=tk.LAST)

