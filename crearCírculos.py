# DONE Documentadas funciones de Tkinter

import tkinter as tk
from math import sin, pi, cos
from random import randint
from threading import Thread

área = None

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

def dibujarNodos(área: tk.Canvas, nodos: list):
    """Dibuja cada uno de los nodos en un área, uno a uno, calculando las posiciones de cada una en
    relación al centro del área."""
    centro = área.winfo_reqwidth()/2
    radio  = centro*.8
    ánguloMúltiplo = 2*pi/len(nodos)
    for iNodo in range(len(nodos)):
        nodo = nodos[iNodo]
        ángulo = iNodo*ánguloMúltiplo
        x, y = centro+sin(ángulo)*radio, centro-cos(ángulo)*radio
        color = generarColorRGB(0xa0, 0xff)
        dibujarNodo(área, nodo, x, y, 25, fill=color, outline="white")
        print(f"Nodo={nodos[iNodo]},posición={(x,y)},color={color}")

def dibujarNodo(área: tk.Canvas, nodo, x, y, r, **kwargs):
    círculo = área.create_oval((x-r, y-r), (x+r, y+r), tag=nodo, **kwargs)
    área.create_text(x,y,text=nodo, tag=f"etiqueta_{nodo}")
    return círculo


def programa(área):
    ventana = tk.Tk()
    área = tk.Canvas(ventana, width=600, height=600, bg="white")
    área.pack()

    nodos = [chr(i) for i in range(0x41, ord("E")+1)]
    dibujarNodos(área, nodos)
    ventana.mainloop()


if __name__ == '__main__':
    ventana = Thread(target=programa, args=(área, ))
    ventana.start()
    ventana.join()
