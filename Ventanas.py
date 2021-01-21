
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from grafo import CAMPO_NODOS, CAMPO_ARISTAS, CAMPO_DIRIGIDO, CAMPO_PONDERADO, CAMPO_MATRIZ
from ventanaGrafo import DibujoGrafo

ESPACIADO = {"padx": 10, "pady": 10}


class CrearGrafo_matriz1(ttk.Frame):
    """
        Implementación de la ventana que permite definir el tipo de grafo y los vértices, antes de
    definir la matriz de adyacencio.

        La ventana permite al usuario definir varios parámetros del grafo, como elegir el tipo y
    especificar los nodos. Esta ventana tiene un botón Generar matriz que, al dar clic y al
    validarse los nombres de los nodos, muestra la ventana CrearGrafo_matriz2.
    """
    def __init__(self, datosGrafo: list, *args, **kwargs):
        """
            Implementación de la ventana que permite definir el tipo de grafo y los vértices, antes
        de definir la matriz de adyacencio.

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
        self.ponderado_valor = tk.BooleanVar()
        ponderado_casillaVerificacion = ttk.Checkbutton(tipoGrafo_marco, text="Ponderado",
                                                        variable=self.ponderado_valor)
        ponderado_casillaVerificacion.pack(ESPACIADO)

        # 1.2.  EntradaTexto(líneas=1,etiqueta="Vértices")
        vertices_marco      = ttk.Labelframe(self, text="Vértices")
        vertices_marco.grid(ESPACIADO, column=1, row=0)
        self.vertices_entrada    = ttk.Entry(vertices_marco)
        self.vertices_entrada.pack(ESPACIADO)

        # 1.3.  Botón(texto="Generar matriz")
        generarMatriz_boton = ttk.Button(self, text="Generar matriz", command=self.validar)
        generarMatriz_boton.grid(ESPACIADO, column=1, row=1)

        self.master.bind('<Return>',   self.validar)
        self.master.bind('<KP_Enter>', self.validar)
        self.mainloop()
        # FIN 1. Ventana(título="Crear grafo por matriz de adyacencia")


    def validar(self, event=None):
        """
            Realiza los procesos de validación necesarios para el formulario de la ventana..

            Para esta ventana, permite validar el campo de los vértices, enumerando cada uno.

        :param event: Evento pasado por Tkinter
        :return: None
        """
        nodos = self.vertices_entrada.get().split() # Lee en campo
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
        self.cerrarVentana()

    def cerrarVentana(self, event=None):
        """
            Destruye y cierra esta ventana, terminado ka recepción de eventos y destruyendo la
        ventana.
        :param event: evento pasado internamente por Tkinter
        :return: None
        """
        #self.master.unbind('<Return>')
        #self.master.unbind('<KP_Enter>')
        self.quit()
        self.update()
        self.destroy()
        self.master.destroy()
        #del self.master


def siNo(bandera):
    """
        Según el dato lógico pasado, devuelve sí o no, según bandera ver verdadera o falsea.
    """
    return "Sí" if bandera else "No"


class VistaGrafo(ttk.Frame):
    def __init__(self, datosGrafo, **kw):
        self.datosGrafo = datosGrafo
        """
            Estructura que contiene todos los datos para definir que definen a un grafo: nodos, 
        aristas, vértices, tipo de grafo, matriz de adyacencia, entre otros.
        """

        super().__init__(**kw)

        # 1. Ventana(título="Dibujo de grafo desde matriz")
        self.master.resizable(True, True)
        self.master.title("Dibujo de grafo desde matriz")
        self.pack()

        # 1.1. DibujoGrafo(datosGrafo)
        self.dibujoGrafo = DibujoGrafo(self, self.datosGrafo, 600)
        #self.dibujoGrafo.pack(side=tk.LEFT)
        self.dibujoGrafo.grid(row=0, column=0, sticky="nsew")

        # 1.2. Marco(título="Propiedades")
        propiedades = ttk.Frame(self)
        #propiedades.pack(side=tk.RIGHT, fill=tk.BOTH)
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
        ttk.Label(propiedades_tabla, text="N° nodos")\
            .grid(ESPACIADO, row=0, column=0, sticky="nsw")

        # 1.2.1.2. Etiqueta(fila=1, columna=2)
        ttk.Label(propiedades_tabla, text=f"{len(self.datosGrafo[CAMPO_NODOS])}")\
            .grid(ESPACIADO, row=0, column=1, sticky="nse")

        # 1.2.1.3. Etiqueta(fila=2, columna=1, texto="N° aristas")
        ttk.Label(propiedades_tabla, text="N° aristas")\
            .grid(ESPACIADO, row=1, column=0, sticky="nsw")

        # 1.2.1.4. Etiqueta(fila=2, columna=2)
        ttk.Label(propiedades_tabla, text=f"{len(self.datosGrafo[CAMPO_ARISTAS])}")\
            .grid(ESPACIADO, row=1, column=1, sticky="nse")

        # 1.2.1.5. Etiqueta(fila=3, columna=1, texto="Dirigido")
        ttk.Label(propiedades_tabla, text="Dirigido")\
            .grid(ESPACIADO, row=2, column=0, sticky="nsw")

        # 1.2.1.6. Etiqueta(fila=3, columna=2)
        ttk.Label(propiedades_tabla, text=f"{siNo(self.datosGrafo[CAMPO_DIRIGIDO])}")\
            .grid(ESPACIADO, row=2, column=1, sticky="nse")

        # 1.2.1.7. Etiqueta(fila=4, columna=1, texto="Ponderado")
        ttk.Label(propiedades_tabla, text="Ponderado")\
            .grid(ESPACIADO, row=3, column=0, sticky="nsw")

        # 1.2.1.8. Etiqueta(fila=4, columna=2)
        ttk.Label(propiedades_tabla, text=f"{siNo(self.datosGrafo[CAMPO_PONDERADO])}")\
            .grid(ESPACIADO, row=3, column=1, sticky="nse")

        # 1.2.2. Botón(texto="Matriz de adyacencia")
        ttk.Button(propiedades_marco, text="Matriz de adyacencia", command=self.matrizAdyacencia)\
            .pack(ESPACIADO)

        # 1.2.3. Botón(texto="Matriz de incidencia")
        ttk.Button(propiedades_marco, text="Matriz de incidencia", command=self.matrizIncidencia)\
            .pack(ESPACIADO)

        # 1. Fin Ventana

        self.update_idletasks()
        self.master.maxsize(self.master.winfo_width(), self.master.winfo_height())
        #self.master.minsize(int(self.master.winfo_width()/2), int(self.master.winfo_height()/2))
        self.mainloop()

    def matrizAdyacencia(self, event=None):
        class DialogoMatrizAdyacencia(Dialogo):
            def body(self, master):
                matriz = []
                matriz.append([""]+self.datosGrafo[CAMPO_NODOS])

                for i in range(len(self.datosGrafo[CAMPO_NODOS])):
                    fila  = [self.datosGrafo[CAMPO_NODOS][i]]
                    fila += [str(j)
                             for j in self.datosGrafo[CAMPO_MATRIZ][i]]
                    matriz.append(fila)

                marco = ttk.Frame(master)
                marco.pack()

                for i in range(len(matriz)):
                    for j in range(len(matriz[i])):
                        ttk.Label(marco, text=matriz[i][j]).grid(ESPACIADO, row=i, column=j)

        DialogoMatrizAdyacencia(self, self.datosGrafo, title="Matriz de adyacencia")

    def matrizIncidencia(self, event=None):
        class DialogoMatrizIncidencia(Dialogo):
            def body(self, master):
                aristas = self.datosGrafo[CAMPO_ARISTAS]
                nodos   = self.datosGrafo[CAMPO_NODOS]
                matriz  = []
                matriz.append([""])
                for i in aristas:
                    matriz[0].append("({},{})".format(i[0], i[1]))

                for i in range(len(nodos)):
                    fila  = [nodos[i]]
                    fila += ["0" for j in aristas]
                    matriz.append(fila)


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


class CrearGrafo_matriz2(ttk.Frame):
    """
        Permite definir la matriz que corresponde al tipo de grafo.
    """
    def __init__(self, datosGrafo, *args, **kwargs):
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
        matrizAdyacencia_marco2 = ttk.Frame(matrizAdyacencia_marco) #   Marco interior centrado
                                                                    # que contiene la matriz de
                                                                    # adyacencia
        matrizAdyacencia_marco2.pack(ESPACIADO, anchor=tk.CENTER)

        nodos = datosGrafo[CAMPO_NODOS]
        self.matriz = []
        tamaño = range(len(nodos) + 1)
        for i in tamaño:
            fila = []
            for j in tamaño:
                entrada = ttk.Entry(matrizAdyacencia_marco2, width=4, justify=tk.CENTER)
                self.escribir(entrada, "0")
                entrada.grid(row=i, column=j, sticky=tk.NSEW, ipadx=4, ipady=4)
                fila.append(entrada)
            self.matriz.append(fila)

        self.escribir(self.matriz[0][0], "")
        self.matriz[0][0]["state"] = tk.DISABLED
        for i in range(1, len(nodos)+1):
            self.escribir(self.matriz[0][i], nodos[i -1])
            self.matriz[0][i]["state"] = tk.DISABLED
            self.escribir(self.matriz[i][0], nodos[i -1])
            self.matriz[i][0]["state"] = tk.DISABLED

        # 1.3.Botón(texto="Dibujar grafo")
        botón = ttk.Button(self, text="Dibujar grafo", command=self.validar)
        botón.pack(ESPACIADO)

        self.master.bind('<Return>', self.validar)
        #self.master.bind('<Intro>', self.validar)
        self.mainloop()
        # FIN 1

    def validar(self, event=None):
        matriz_temp = []
        for fila in self.matriz[1:]:
            fila_ = []
            for entrada in fila[1:]:
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
            matriz_temp.append(fila_)

        if not self.datosGrafo[CAMPO_DIRIGIDO]:
            for i in range(len(matriz_temp)):
                for j in range(i +1):
                    if matriz_temp[i][j] != matriz_temp[j][i]:
                        messagebox.showerror(title="Error de validación",
                                             message="Los valores en A_ij deben ser iguales que en "
                                                     "A_ji para grafos no dirigidos")
                        return

        self.datosGrafo[CAMPO_MATRIZ] = matriz_temp
        self.cerrarVentana()

    def cerrarVentana(self, event=None):
        """
            Destruye y cierra esta ventana, terminado ka recepción de eventos y destruyendo la
        ventana.
        :param event: evento pasado internamente por Tkinter
        """
        self.quit()
        self.update()
        self.destroy()

    def escribir(self, entrada: tk.Entry, texto: str):
        entrada.delete(0, tk.END)
        entrada.insert(0, texto)


class Dialogo(simpledialog.Dialog):
    def __init__(self, parent, datosGrafo, *args, **kwargs):
        self.datosGrafo = datosGrafo
        super().__init__(parent, *args, **kwargs)

    def buttonbox(self):
        ttk.Button(self, text="Cerrar", command=self.destroy).pack()

