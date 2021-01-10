
import tkinter as tk
from tkinter import ttk, messagebox

from grafo import *

SEPARACION = 10 # espaciado entre controles de la ventana

# TODO Agregar a este regustro campo para la matriz


class CrearGrafo_matriz1(ttk.Frame):
    """
        Implementación de la ventana que permite definir el tipo de grafo y los vértices, antes de
    definir la matriz de adyacencio.
    """
    def __init__(self, datosGrafo, *args, **kwargs):
        self.datosGrafo = datosGrafo
        super().__init__(*args, **kwargs)

        # 1. Ventana(título="Crear grafo por matriz de adyacencia")
        self.master.resizable(False, False)
        self.master.title("Crear grafo por matriz de adyacencia")
        self.pack()

        # 1.1. Marco(título="Tipo de grafo")
        tipoGrafo_marco         = ttk.Labelframe(self, text="Tipo de grafo")
        tipoGrafo_marco.grid(padx=SEPARACION, pady=SEPARACION, column=0, row=0, rowspan=2)

        # 1.1.1. CasillaVerificación("Dirigido")
        self.dirigido_valor          = tk.BooleanVar()
        dirigido_casillaVerificacion = ttk.Checkbutton(tipoGrafo_marco,
                                                       text="Dirigido",
                                                       variable=self.dirigido_valor)
        dirigido_casillaVerificacion.pack(padx=SEPARACION, pady=SEPARACION)

        # 1.1.2. CasillaVerificación("Ponderado")
        self.ponderado_valor = tk.BooleanVar()
        ponderado_casillaVerificacion = ttk.Checkbutton(tipoGrafo_marco,text="Ponderado",
                                                        variable=self.ponderado_valor)
        ponderado_casillaVerificacion.pack(padx=SEPARACION, pady=SEPARACION)

        # 1.2.  EntradaTexto(líneas=1,etiqueta="Vértices")
        vertices_marco      = ttk.Labelframe(self, text="Vértices")
        vertices_marco.grid(padx=SEPARACION, pady=SEPARACION, column=1, row=0)
        self.vertices_valor = tk.StringVar()
        vertices_entrada    = ttk.Entry(vertices_marco, textvariable=self.vertices_valor)
        vertices_entrada.pack(padx=SEPARACION, pady=SEPARACION)

        # 1.3.  Botón(texto="Generar matriz")
        generarMatriz_boton = ttk.Button(self, text="Generar matriz", command=self.validar)
        generarMatriz_boton.grid(padx=SEPARACION, pady=SEPARACION, column=1, row=1)

        self.master.bind('<Return>', self.validar)
        self.master.protocol("WM_DELETE_WINDOW", self.cerrarVentana)    # TODO Documentar
        # TODO Citar https://stackoverflow.com/questions/50875060/execute-a-certain-command-before-closing-window-in-tkinter
        self.mainloop()
        # FIN 1. Ventana(título="Crear grafo por matriz de adyacencia")


    def validar(self, event=None):
        """
            Permite validar el campo de los vértices
        :param event: Evento pasado por Tkinter
        :return: None
        """
        nodos = self.vertices_valor.get().split()
        nodos = list(sorted(set(nodos)))  # eliminarNodosDuplicados(nodos)

        if len(nodos) < 2:
            messagebox.showerror(title="Error de validación",
                                 message="Asegúrese de especificar al menos 3 nodos distintos")
            return

        for nodo in nodos:
            if not nodo.isalnum():
                messagebox.showerror(title="Error de validación",
                                     message="Asegúrese de haber usado solamente espacio, subguión "
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
        self.master.unbind('<Return>')  # TODO Documentar
        self.quit()
        self.update()
        self.destroy()


def siNo(bandera):
    """
        Según el dato lógico pasado, devuelve sí o no, según bandera ver verdadera o falsea.
    """
    return "sí" if bandera else "no"


class CrearGrafo_matriz2(ttk.Frame):
    """
        Permite definir la matriz que corresponde al tipo de grafo.
    """
    def __init__(self, datosGrafo, *args, **kwargs):
        self.datosGrafo = datosGrafo
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
        etiquetaTipoGrafo.pack(padx=SEPARACION, pady=SEPARACION)

        # 1.2.Marco(título="Matriz de adyacencia")
        #matrizAdyacencia_marco = ttk.Labelframe(self, text="Matriz de adyacencia", width=100,
        #                                        height=100)
        matrizAdyacencia_marco = ttk.Labelframe(self, text="Matriz de adyacencia")
        matrizAdyacencia_marco.pack(padx=SEPARACION, pady=SEPARACION)

        # 1.2.1.MatrizAdyacencia(nodos)
        matrizAdyacencia_marco2 = ttk.Frame(matrizAdyacencia_marco) #   Marco interior centrado
                                                                    # que contiene la matriz de
                                                                    # adyacencia
        matrizAdyacencia_marco2.pack(anchor=tk.CENTER, padx=SEPARACION, pady=SEPARACION)

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
        botón = ttk.Button(text="Dibujar grafo", command=self.validar)
        botón.pack(padx=SEPARACION, pady=SEPARACION)

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


if __name__ == "__main__":
    datosGrafo = [[], False, False, []] #   Datos que `CrearGrado_matriz1` envía a la ventana para
                                        # definir la matriz.
    CrearGrafo_matriz1(datosGrafo)

    if len(datosGrafo[CAMPO_NODOS]) > 0:
        CrearGrafo_matriz2(datosGrafo)
    if datosGrafo[CAMPO_MATRIZ] is not None:
        print(datosGrafo)
