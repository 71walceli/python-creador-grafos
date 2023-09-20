
import tkinter as tk
import numpy as np
from math import pi, sin, cos, atan2, sqrt
from random import randint, random
from tkinter import ttk, messagebox, simpledialog

from grafo import CAMPO_NODOS, CAMPO_ARISTAS, CAMPO_DIRIGIDO, CAMPO_PONDERADO, CAMPO_MATRIZ

FORMATO_ARISTA_PESO_FONDO = "{}.peso.fondo"

FORMATO_ARISTA_PESO = '{}.peso'

FORMATO_ARISTA = "{}-{}"

FORMATO_NODO_NOMBRE = "{}.nombre"

FORMATO_NODO_GRAFICO = "{}.nodo"

ESPACIADO = {"padx": 10, "pady": 10}
"""Espaciado horizontal y vertical entre elementos de la interfaz gráfica."""


def generarColorRGB(mínimo: int, máximo: int) -> str:
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


def siNo(bandera: bool) -> str:
    """
        Según el dato lógico pasado, devuelve "Sí" o "No", para verdadera o falso, respectivamente.
    """
    return "Sí" if bandera else "No"


class CrearGrafo_matriz1(ttk.Frame):
    def __init__(self, datosGrafo: list, *args, **kwargs):
        """
            La ventana permite al usuario definir varios parámetros del grafo, como elegir el tipo y
        especificar los nodos. Esta ventana tiene un botón Generar matriz que, al dar clic y al
        validarse los nombres de los nodos, muestra la ventana CrearGrafo_matriz2.

        :param datosGrafo:  Estructura que contiene todos los datos que definen a un grafo
        :param args:        Argumentos opcionales para ttk.Frame.
        :param kwargs:      Argumentos opcionales para ttk.Frame.
        """
        self.datosGrafo = datosGrafo
        """
            Estructura que contiene todos los datos que definen a un grafo: nodos, 
        aristas, vértices, tipo de grafo, matriz de adyacencia, entre otros.
        """
        super().__init__(*args, **kwargs)

        # 1. Ventana(título="Crear grafo por matriz de adyacencia")
        self.master.resizable(False, False)
        self.master.title("Crear grafo por matriz de adyacencia")
        self.pack()

        # 1.1. Marco(título="Tipo de grafo")
        tipoGrafo_marco = ttk.Labelframe(self, text="Tipo de grafo")
        tipoGrafo_marco.grid(ESPACIADO, column=0, row=0, rowspan=2)

        # 1.1.1. CasillaVerificación("Dirigido")
        self.dirigido_valor          = tk.BooleanVar()
        dirigido_casillaVerificacion = ttk.Checkbutton(tipoGrafo_marco,
                                                       text="Dirigido",
                                                       variable=self.dirigido_valor)
        dirigido_casillaVerificacion.pack(ESPACIADO)

        # 1.1.2. CasillaVerificación("Ponderado")
        self.ponderado_valor          = tk.BooleanVar()
        ponderado_casillaVerificacion = ttk.Checkbutton(tipoGrafo_marco, text="Ponderado",
                                                        variable=self.ponderado_valor)
        ponderado_casillaVerificacion.pack(ESPACIADO)

        # 1.2.  EntradaTexto(líneas=1,etiqueta="Vértices")
        vertices_marco           = ttk.Labelframe(self, text="Vértices")
        vertices_marco.grid(ESPACIADO, column=1, row=0)
        self.vertices_entrada    = ttk.Entry(vertices_marco)
        self.vertices_entrada.pack(ESPACIADO)

        # 1.3.  Botón(texto="Generar matriz")
        generarMatriz_boton = ttk.Button(self, text="Generar matriz", command=self.validar)
        generarMatriz_boton.grid(ESPACIADO, column=1, row=1)

        self.master.bind('<Return>',   self.validar)    # Ejecutar validación al presionar Enter
        self.master.bind('<KP_Enter>', self.validar)    #
        self.mainloop()
        # FIN 1. Ventana(título="Crear grafo por matriz de adyacencia")

    def validar(self, event=None):
        """
            Realiza los procesos de validación necesarios para el formulario de la ventana..

            Para esta ventana, permite validar el campo de los vértices, enumerando cada uno.

        :param event: Evento pasado por Tkinter
        :return: None
        """
        nodos = self.vertices_entrada.get().split() # Lee el campo, como una lista de nombres.
        nodos = list(sorted(set(nodos)))    # Ordena cada vértice y elimina nombres redundantes.

        if len(nodos) < 2:
            messagebox.showerror(title="Error de validación",
                                 message="Se debe especificar al menos 2 nodos distintos.")
            return

        for nodo in nodos:
            if not nodo.replace("_", "").isalnum():
                messagebox.showerror(title="Error de validación",
                                     message="Asegúrese de haber usado solamente espacio, "
                                             "y caracteres alfanuméricos en el campo de vértices.")
                return

        self.datosGrafo[CAMPO_NODOS]     = nodos
        self.datosGrafo[CAMPO_DIRIGIDO]  = self.dirigido_valor.get()
        self.datosGrafo[CAMPO_PONDERADO] = self.ponderado_valor.get()
        self.master.destroy()


class CrearGrafo_matriz2(ttk.Frame):
    def __init__(self, datosGrafo: list, *args, **kwargs):
        """
            Tiene el fin de permitir al usuario definir la matriz de adyacencia del grafo
        correspondiente, Los datos se ingresarán en una matriz, en la cual se debe ingresar
        números que describan las aristas, de acuerdo al tipo de grafo.

        :param datosGrafo:  Estructura que contiene todos los datos que definen a un grafo
        :param args:        Argumentos opcionales para ttk.Frame.
        :param kwargs:      Argumentos opcionales para ttk.Frame.
        """
        self.datosGrafo = datosGrafo
        """
            Estructura que contiene todos los datos para definir que definen a un grafo: nodos, 
        aristas, vértices, tipo de grafo, matriz de adyacencia, entre otros.
        """
        super().__init__(*args, **kwargs)

        # 1. Ventana(título="Crear grafo por matriz de adyacencia")
        self.master.resizable(False, False)
        self.master.title("Crear grafo por matriz de adyacencia")
        self.pack()

        # 1.1.Etiqueta(texto=descripciónTipoGrafo, alineación=centrado)
        etiquetaTipoGrafo = ttk.Label(self, text="Dirigido:"
                                                 f" {siNo(datosGrafo[CAMPO_DIRIGIDO])}"
                                                 "\nPonderado:"
                                                 f" {siNo(datosGrafo[CAMPO_PONDERADO])}"
                                      )
        etiquetaTipoGrafo.pack(ESPACIADO)

        # 1.2.Marco(título="Matriz de adyacencia")
        matrizAdyacencia_marco = ttk.Labelframe(self, text="Matriz de adyacencia")
        matrizAdyacencia_marco.pack(ESPACIADO)

        # 1.2.1.MatrizAdyacencia(nodos)
        matrizAdyacencia_marco2 = ttk.Frame(matrizAdyacencia_marco) #   Marco interior centrado que
                                                                    # contiene la matriz de
                                                                    # adyacencia
        matrizAdyacencia_marco2.pack(ESPACIADO, anchor=tk.CENTER)
        nodos = datosGrafo[CAMPO_NODOS]

        self.matrizEntradas = []
        tamaño = range(len(nodos) + 1)
        for i in tamaño:    # Creación de la matriz de entradas de texto para definir la matriz.
            fila = []
            for j in tamaño:
                entrada = ttk.Entry(matrizAdyacencia_marco2, width=4, justify=tk.CENTER)
                self.escribir(entrada, "0")
                entrada.grid(row=i, column=j, sticky=tk.NSEW, ipadx=4, ipady=4)
                fila.append(entrada)
            self.matrizEntradas.append(fila)

        self.escribir(self.matrizEntradas[0][0], "")
        self.matrizEntradas[0][0]["state"] = tk.DISABLED
        for i in range(1, len(nodos)+1):    # Se crea con encabezados de fila y de columna.
            self.escribir(self.matrizEntradas[0][i], nodos[i - 1])
            self.matrizEntradas[0][i]["state"] = tk.DISABLED
            self.escribir(self.matrizEntradas[i][0], nodos[i - 1])
            self.matrizEntradas[i][0]["state"] = tk.DISABLED

        # 1.3.Botón(texto="Dibujar grafo")
        botón = ttk.Button(self, text="Dibujar grafo", command=self.validar)
        botón.pack(ESPACIADO)

        self.master.bind('<Return>', self.validar)
        self.master.bind('<KP_Enter>', self.validar)
        self.mainloop()
        # FIN 1

    def validar(self, event=None):
        """
            Realiza los procesos de validación necesarios para el formulario de la ventana..

            Para esta ventana, valida los valores de cada una de las celdas, según el tipo de grafo
        definido.

        :param event: Evento pasado por Tkinter
        :return: None
        """
        matriz = []
        for fila in self.matrizEntradas[1:]:    #   Chequeo valor a valor de la matriz de entrada,
            fila_ = []                          # saltando la fila de encabezados.
            for entrada in fila[1:]:    #   Desde la segunda columna.
                dato = entrada.get()
                if not dato.isdigit() or int(dato) < 0:
                    messagebox.showerror(title="Error de validación",
                                         message="Solo se permiten ingresar números naturales en la"
                                                 " matriz.")
                    return

                dato = int(dato)
                if not self.datosGrafo[CAMPO_PONDERADO] and not dato in [0, 1]:
                    messagebox.showerror(title="Error de validación",
                                         message="Solo se permiten ingresar 0 o 1 para grafos no "
                                                 "ponderados.")
                    return

                fila_.append(int(dato))
            matriz.append(fila_)

        if not self.datosGrafo[CAMPO_DIRIGIDO]:
            for i in range(len(matriz)):
                for j in range(i +1):
                    if matriz[i][j] != matriz[j][i]:
                        messagebox.showerror(title="Error de validación",
                                             message="Los valores en A_ij deben ser iguales que en "
                                                     "A_ji para grafos no dirigidos")
                        return

        self.datosGrafo[CAMPO_MATRIZ] = matriz
        self.master.destroy()   # Cerrar y destruir la ventana

    def escribir(self, entrada: ttk.Entry, texto: str):
        """
            Procedimiento que escribe o sobrescribe la entrada de texto dada.

        :param entrada: Entrada de texto ttk.Entry
        :param texto:   Cadena de texto que se escribirá en la caja de texto.
        """
        entrada.delete(0, tk.END)
        entrada.insert(0, texto)


class Dialogo(simpledialog.Dialog):
    def __init__(self, parent, datosGrafo, *args, **kwargs):
        """
            Clase genérica para cuadros de diálogo.
        """
        self.datosGrafo = datosGrafo
        super().__init__(parent, *args, **kwargs)

    def buttonbox(self):
        """
            Agregar un botón para cerrar cada una de los cuadros de diálogo.
        """
        ttk.Button(self, text="Cerrar", command=self.destroy).pack()


class DibujoGrafo(ttk.Frame):
    def __init__(self, padre: tk.Widget, datosGrafo: list, tamano: int, **kw):
        """
            Un marco ttk.Frame que contiene graficación de un grafo, continida en sí mismo con
        todos sus aristas

        :param padre:       Usado internamente por Tkinter para indicar a qué contenedor corresponde
        :param datosGrafo:  Estructura que contiene todos los datos que definen a un grafo
        :param tamano:      Entero que es la cantidad de pixeles de ancho y de alto.
        :param kw:          Argumentos especiales usados por Tkinter
        """
        self.radioNodos  = 25
        self.datosGrafo  = datosGrafo
        self.padre       = padre
        self.ancho       = self.alto = tamano

        super().__init__(padre, **kw)
        self.area = tk.Canvas(self, bg="white", height=self.alto, width=self.ancho, borderwidth=0,
                              **kw)
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
        self.radioInterno     = self.centro -2.5*self.radioNodos

        self.dibujar()
        self.bind("<Configure>", self.configurarDesplazamiento)
        self.padre.bind("<Configure>", self.configurarDesplazamiento)

    def configurarDesplazamiento(self, event=None):
        """
            Configura las barras de desplazamiento según el tamaño del gráfico relativo al tamaño de
        la ventana.
        """
        if (self.winfo_width() >= self.ancho):          #   Si desplazamientoHorizontal
            self.desplazamientoHorizontal.grid_remove() # abarca toda el área, quitarla
            self.area["height"] = self.alto
        else:   #   sino, poner desplazamientoHorizontal de nuevo y ajustar el área según espacio.
            self.config(width=self.area.winfo_reqwidth())
            self.desplazamientoHorizontal.grid()
            self.area["height"] = self.altoMinimo

        if (self.winfo_height() >= self.alto):
            self.desplazamientoVertical.grid_remove()           # desplazamientoVertical
            self.area["width"] = self.ancho
        else:
            self.config(height=self.area.winfo_reqheight())
            self.desplazamientoVertical.grid()
            self.area["width"] = self.anchoMinimo

        self.area.config(scrollregion='0 0 %s %s' % (self.anchoMinimo, self.altoMinimo))

    def dibujar(self):
        """
            Dibuja cada uno de los nodos y los vértices en el área correspondiente.
        """
        nodos          = self.datosGrafo[CAMPO_NODOS]
        ánguloMúltiplo = 2 * pi / len(nodos)
        for iNodo in range(len(nodos)):
            nodo     = nodos[iNodo]
            ángulo   = iNodo * ánguloMúltiplo
            x        = self.centro + sin(ángulo) * self.radioInterno   # Cálculo de posición del
            y        = self.centro - cos(ángulo) * self.radioInterno   # vértice
            color    = generarColorRGB(0xa0, 0xff)
            self.dibujarNodo(nodo, x, y, self.radioNodos, fill=color, outline="white")

        aristas = self.datosGrafo[CAMPO_ARISTAS]
        for arista in aristas:
            color = generarColorRGB(0x00, 0x80)
            self.dibujarArista(arista, color)

    def dibujarNodo(self, nodo: str, x: int, y: int, r: int, **kwargs):
        """
            Dibuja cada uno de los nodos del grafo.

        :param nodo: Nombre del nodo
        :param x: coordenada horizontal
        :param y: coordenada vertical
        :param r: radio del círculo
        :param kwargs: argumento especiales de Tkinter
        """
        etiqueta_grafico = FORMATO_NODO_GRAFICO.format(nodo)
        etiqueta_nombre  = FORMATO_NODO_NOMBRE.format(nodo)
        self.area.create_oval((x -r, y -r), (x +r, y +r), tag=etiqueta_grafico, **kwargs)
        self.area.create_text(x, y, text=nodo, tag=etiqueta_nombre)

    def dibujarArista(self, arista: list, color: str):
        """
            Dibuja una línea que conecte los dos nodos.

            Si el grafo es ponderado, etiquetará cada arista con la ponderación.

            Si el grafo es dirigido, dibuja una flecha hacia el segundo nodo.

        :param arista: arreglo que especifica los dos aristas y el peso entre ellos.
        :param color:  color para este arista.
        :return:
        """
        nodo_a   = arista[0]
        nodo_b   = arista[1]
        coords_a = self.area.bbox(FORMATO_NODO_GRAFICO.format(nodo_a)) #   Obtener las coordenadas
        centro_a = (coords_a[0] + self.radioNodos + 1,                 # del primer nodo en el
                    coords_a[1] + self.radioNodos + 1)                 # gráfico
        etiqueta            = FORMATO_ARISTA.format(nodo_a, nodo_b)
        etiqueta_peso       = FORMATO_ARISTA_PESO.format(etiqueta)
        etiqueta_fondo_peso = FORMATO_ARISTA_PESO_FONDO.format(etiqueta)

        if nodo_a == nodo_b:    #   El nodo se conecta con sí mismo.
            centro_a = (centro_a[0] + 0.3 * self.radioNodos, centro_a[1] - 0.3 * self.radioNodos)
            puntos_n = 7
            puntos   = [    # Puntos intermedios para dibular una línea en forma circular.
                (
                    centro_a[0] -0.5*cos(pi *i*2/puntos_n) *self.radioNodos,
                    centro_a[1] -0.5*sin(pi *i*2/puntos_n) *self.radioNodos
                ) for i in range(puntos_n)
            ]
            self.area.create_line(puntos, smooth=True, tag=etiqueta, fill=color)

            if self.datosGrafo[CAMPO_PONDERADO]:    # Agregarle la ponderación con una etiqueta
                peso = arista[2]
                peso_posicion = centro_a
                self.area.create_text(peso_posicion, text=str(peso), fill="white", tag=etiqueta_peso)
                self.area.create_rectangle(self.area.bbox(etiqueta_peso), fill=color,
                                           outline=color, tag=etiqueta_fondo_peso)
                self.area.tag_raise(f"{etiqueta}.peso")
        else:   # nodo_a != nodo_b
            coords_b = self.area.bbox(FORMATO_NODO_GRAFICO.format(nodo_b))
            centro_b = (coords_b[0] + self.radioNodos + 1, coords_b[1] + self.radioNodos + 1)
            angulo_a = atan2(centro_a[1] -centro_b[1], centro_a[0] -centro_b[0])    # ángulo
                                                                                    # entre los dos
                                                                                    # vértices
            inicio = (    # desde el primer vértice
                centro_a[0] - cos(angulo_a) * (self.radioNodos - 3),
                centro_a[1] - sin(angulo_a) * (self.radioNodos - 3),
            )
            fin    = (    # hasta aquel que conecta
                centro_b[0] +cos(angulo_a)*(self.radioNodos - 3),
                centro_b[1] +sin(angulo_a)*(self.radioNodos - 3),
            )
            self.area.create_line(inicio, fin, smooth=True, tag=etiqueta, fill=color)

            if self.datosGrafo[CAMPO_PONDERADO]:    # Agregarle la ponderación con una etiqueta
                peso          = arista[2]
                distancia     = (sqrt((inicio[0] -fin[0])**2+ (inicio[1] -fin[1])**2))
                multiplo      = 0.55 +random()*0.25
                peso_posicion = (    # Punto intermedio en donde colocar etiqueta del peso.
                    inicio[0] - cos(angulo_a) *distancia *multiplo,
                    inicio[1] - sin(angulo_a) *distancia *multiplo,
                )
                self.area.create_text(peso_posicion, text=str(peso), fill="white",
                                      tag=etiqueta_peso)
                self.area.create_rectangle(
                    self.area.bbox(etiqueta_peso), fill=color,
                    outline=color, tag=etiqueta_fondo_peso)
                self.area.tag_raise(etiqueta_peso)

        if self.datosGrafo[CAMPO_DIRIGIDO]: # Agregar punta de flecha al segundo elemento.
            self.area.itemconfigure(etiqueta, arrow=tk.LAST)


class VistaGrafo(ttk.Frame):
    def __init__(self, datosGrafo: list, **kw):
        """
            Esta ventana se encarga de mostrar el grafo terminado y permite ver algunas
        propiedades del mismo, como el número de aristas y de nodos, el tipo de grafo y las
        matrices de adyacencia y de incidencia.

        :param datosGrafo:  Estructura que contiene todos los datos que definen a un grafo
        :param args:        Argumentos opcionales para ttk.Frame.
        :param kwargs:      Argumentos opcionales para ttk.Frame.
        """

        self.datosGrafo = datosGrafo
        super().__init__(**kw)

        # 1. Ventana(título="Dibujo de grafo desde matriz")
        self.master.resizable(True, True)
        self.master.title("Dibujo de grafo desde matriz")
        self.pack()

        # 1.1. DibujoGrafo(datosGrafo)
        self.dibujoGrafo = DibujoGrafo(self, self.datosGrafo, 600)
        self.dibujoGrafo.grid(row=0, column=0, sticky="nsew")

        # 1.2. Marco(título="Propiedades")
        propiedades = ttk.Frame(self)
        propiedades.grid(row=0, column=1, sticky="nsew")

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)

        propiedades_marco = ttk.Labelframe(propiedades, text="Propiedades")
        propiedades_marco.pack(ESPACIADO)

        # 1.2.1. Tabla()
        propiedades_tabla = ttk.Frame(propiedades_marco)
        propiedades_tabla.pack()

        # 1.2.1.1. Etiqueta(fila=1, columna=1, texto="N° nodos")
        ttk.Label(propiedades_tabla, text="N° nodos") \
            .grid(ESPACIADO, row=0, column=0, sticky="nsw")

        # 1.2.1.2. Etiqueta(fila=1, columna=2)
        ttk.Label(propiedades_tabla, text=f"{len(self.datosGrafo[CAMPO_NODOS])}") \
            .grid(ESPACIADO, row=0, column=1, sticky="nse")

        # 1.2.1.3. Etiqueta(fila=2, columna=1, texto="N° aristas")
        ttk.Label(propiedades_tabla, text="N° aristas") \
            .grid(ESPACIADO, row=1, column=0, sticky="nsw")

        # 1.2.1.4. Etiqueta(fila=2, columna=2)
        ttk.Label(propiedades_tabla, text=f"{len(self.datosGrafo[CAMPO_ARISTAS])}") \
            .grid(ESPACIADO, row=1, column=1, sticky="nse")

        # 1.2.1.5. Etiqueta(fila=3, columna=1, texto="Dirigido")
        ttk.Label(propiedades_tabla, text="Dirigido") \
            .grid(ESPACIADO, row=2, column=0, sticky="nsw")

        # 1.2.1.6. Etiqueta(fila=3, columna=2)
        ttk.Label(propiedades_tabla, text=f"{siNo(self.datosGrafo[CAMPO_DIRIGIDO])}") \
            .grid(ESPACIADO, row=2, column=1, sticky="nse")

        # 1.2.1.7. Etiqueta(fila=4, columna=1, texto="Ponderado")
        ttk.Label(propiedades_tabla, text="Ponderado") \
            .grid(ESPACIADO, row=3, column=0, sticky="nsw")

        # 1.2.1.8. Etiqueta(fila=4, columna=2)
        ttk.Label(propiedades_tabla, text=f"{siNo(self.datosGrafo[CAMPO_PONDERADO])}") \
            .grid(ESPACIADO, row=3, column=1, sticky="nse")

        # 1.2.2. Botón(texto="Matriz de adyacencia")
        ttk.Button(propiedades_marco, text="Matriz de adyacencia", command=self.matrizAdyacencia) \
            .pack(ESPACIADO)

        # 1.2.3. Botón(texto="Matriz de incidencia")
        ttk.Button(propiedades_marco, text="Matriz de incidencia", command=self.matrizIncidencia) \
            .pack(ESPACIADO)

        # 1.2.4. Botón(texto="Grados de los vértices")
        ttk.Button(propiedades_marco, text="Grados de los vértices", command=self.gradosVertices) \
            .pack(ESPACIADO)

        # 1. Fin Ventana

        self.update_idletasks() # Para que finalice las tareas de ubicar cada elemento de la
                                # ventana,
        self.master.maxsize(self.master.winfo_width(), self.master.winfo_height())
        self.mainloop()

    def matrizAdyacencia(self, event=None):
        """
        Genera un cuadro de díalogo con la matriz de adyacencia del grafo que se visualiza.

        :param event:
        """
        class DialogoMatrizAdyacencia(Dialogo):
            """
            Implementación de díájogo para mostrar la matriz de adyacencia.
            """
            def body(self, master):
                matriz = []
                matriz.append([""]+self.datosGrafo[CAMPO_NODOS])

                for i in range(len(self.datosGrafo[CAMPO_NODOS])):  #   Obtiene cada valor de la
                                                                    # matriz de adacencia que
                                                                    # especfica al grafo que se
                                                                    # muestra.
                    fila  = [self.datosGrafo[CAMPO_NODOS][i]]
                    fila += [str(j) for j in self.datosGrafo[CAMPO_MATRIZ][i]]
                    matriz.append(fila)

                marco = ttk.Frame(master)
                marco.pack()

                for i in range(len(matriz)):        # Coloca cada elemento en una etiqueta para ser
                    for j in range(len(matriz[i])): # mostrado.
                        ttk.Label(marco, text=matriz[i][j]).grid(ESPACIADO, row=i, column=j)

        # Mostrar el diálogo generado
        DialogoMatrizAdyacencia(self, self.datosGrafo, title="Matriz de adyacencia")

    def matrizIncidencia(self, event=None):
        """
        Genera un cuadro de díalogo con la matriz de incidencia del grafo que se visualiza.

        :param event: Evento pasado por Tkinter
        """
        class DialogoMatrizIncidencia(Dialogo):
            """
            Implementación de díájogo para mostrar la matriz de incidencia.
            """
            def body(self, master):
                aristas = self.datosGrafo[CAMPO_ARISTAS]
                nodos   = self.datosGrafo[CAMPO_NODOS]
                matriz  = []
                matriz.append([""])
                for i in aristas:
                    matriz[0].append("({},{})".format(i[0], i[1]))  #   Genera encabezados de cada
                                                                    # arista.

                for i in range(len(nodos)):
                    fila  = [nodos[i]]
                    fila += ["0" for j in aristas]
                    matriz.append(fila)

                # TODO Seguir documentando esta función
                for i in range(len(nodos)):
                    for j in range(len(aristas)):
                        peso   = 1 if not self.datosGrafo[CAMPO_PONDERADO] else aristas[j][2]
                        if   nodos[i] in aristas[j] and not self.datosGrafo[CAMPO_PONDERADO]:
                            matriz[i +1][j +1] = str(int(matriz[i +1][j +1]) +peso)
                        elif nodos[i] == aristas[j][1]:
                            matriz[i +1][j +1] = str(int(matriz[i +1][j +1]) +peso)

                marco = ttk.Frame(master)
                marco.pack()

                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        ttk.Label(marco, text=matriz[i][j]).grid(ESPACIADO, row=i, column=j)

        if len(self.datosGrafo[CAMPO_ARISTAS]) > 0:
            DialogoMatrizIncidencia(self, self.datosGrafo, title="Matriz de incidencia")
        else:
            messagebox.showinfo(title="Matriz de incidencia",
                                message="No se puede generar una matriz de incidencia ya que el"
                                        "grafo no tiene aristas.")

    def gradosVertices(self, event=None):
        """
            Genera un cuadro de diálogo que muestra los grados de todos los vértices definidos.

        :param event: Evento pasado por Tkinter
        """
        class DialogoGradosVertices(Dialogo):
            def body(self, parent, **kwargs):
                tabla = ttk.Frame(self)
                tabla.pack()

                ttk.Label(tabla, text="Nodo").grid(ESPACIADO, row=0, column=0)  # Encabezado
                cabecera_columna1 = ttk.Label(tabla, text="Grado")
                cabecera_columna1.grid(ESPACIADO, row=0, column=1) #

                grados = [[nodo] for nodo in self.datosGrafo[CAMPO_NODOS]]
                for i in range(len(grados)):
                    grado = sum(1 for _ in self.datosGrafo[CAMPO_MATRIZ][i] if _ != 0)  # Valen 1
                                                                                    # los grados
                                                                                    # diferentes de
                                                                                    # 0.
                    if self.datosGrafo[CAMPO_MATRIZ][i][i] != 0:    # Vértice se enlaza consígo.
                        grado += 1
                    grados[i].append(grado)

                if self.datosGrafo[CAMPO_DIRIGIDO]:
                    traspuesta = np.array(self.datosGrafo[CAMPO_MATRIZ]).transpose().tolist()
                    cabecera_columna1["text"] = "Grado entrante"
                    ttk.Label(tabla, text="Grado saliente").grid(ESPACIADO, row=0, column=2)

                    for i in range(len(self.datosGrafo[CAMPO_NODOS])):
                        grado = sum(1 for _ in traspuesta[i] if _ != 0)
                        grados[i].append(grado)

                for i in range(len(grados)):
                    for j in range(len(grados[i])):
                        ttk.Label(tabla, text=str(grados[i][j])).grid(ESPACIADO, row=i+1, column=j)

        DialogoGradosVertices(self, self.datosGrafo)



