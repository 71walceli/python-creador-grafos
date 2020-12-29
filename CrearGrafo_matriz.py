
import tkinter as tk
from tkinter import ttk, messagebox

SEPARACION = 10

datosTipoGrafo = [[], False, False]    #   Datos que `CrearGrado_matriz1` envía a la
                                       # ventana para definir la matriz.
CAMPO_NODOS     = 0
CAMPO_DIRIGIDO  = 1
CAMPO_PONDERADO = 2

class CrearGrafo_matriz1(tk.Frame):
    """
        Implementación de la ventana que permite crear un grafo por medio de una matriz de
    adyacencio
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 1. Ventana(título="Crear grafo por matriz de adyacencia")
        self.master.resizable(False, False)
        self.master.title("Crear grafo por matriz de adyacencia")
        self.pack()

        # 1.1. Marco(título="Tipo de grafo")
        tipoGrafo_marco         = ttk.Labelframe(self, text="Tipo de grafo")
        tipoGrafo_marco.grid(padx=SEPARACION, pady=SEPARACION, column=0, row=0, rowspan=2)

        # 1.1.1. CasillaVerificación("Dirigido")
        self.dirigido_valor               = tk.BooleanVar()
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
        global datosTipoGrafo
        nodos = self.vertices_valor.get().split()
        nodos = list(sorted(set(nodos)))  # eliminarNodosDuplicados(nodos)

        if len(nodos) < 2:
            messagebox.showerror(title="Error de validación",
                                 message="Asegúrese de especificar al menos 3 nodos distintos")
            return

        for nodo in nodos:
            if not nodo.isalpha():
                messagebox.showerror(title="Error de validación",
                                     message="Asegúrese de haber usado solamente espacio, subguión "
                                             "y caracteres alfanuméricos en el campo de vértices.")
                return

        datosTipoGrafo = [
            nodos,
            self.dirigido_valor.get(),
            self.ponderado_valor.get(),
        ]
        self.cerrarVentana()

    def cerrarVentana(self, event=None):
        self.master.unbind('<Return>')  # TODO Documentar
        self.quit()
        self.update()
        self.destroy()
        #print("Ventana cerrada correctamente")


def siNo(bandera):
    return "sí" if bandera else "no"


class CrearGrafo_matriz2(tk.Frame):
    def __init__(self, datosTipoGrafo, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 1. Ventana(título="Crear grafo por matriz de adyacencia")
        self.master.resizable(False, False)
        self.master.title("Crear grafo por matriz de adyacencia")
        self.pack()

        # 1.1.Etiqueta(texto=descripciónTipoGrafo, alineación=centrado)
        etiquetaTipoGrafo = ttk.Label(self, text="Dirigido:"
                                                 f" {siNo(datosTipoGrafo[CAMPO_DIRIGIDO])}"
                                                 "\nPonderado:"
                                                 f" {siNo(datosTipoGrafo[CAMPO_PONDERADO])}"
                                      )
        etiquetaTipoGrafo.pack(padx=SEPARACION, pady=SEPARACION)

        # 1.2.Marco(título="Matriz de adyacencia")
        matrizAdyacencia_marco = ttk.Labelframe(self, text="Matriz de adyacencia", width=100,
                                                height=100)  # TODO Definir matriz
        #matrizAdyacencia_marco.winfo_geometry("200x200")
        matrizAdyacencia_marco.pack(padx=SEPARACION, pady=SEPARACION)

        # 1.2.1.MatrizAdyacencia(nodos)
        # 1.3.Botón(texto="Dibujar grafo")

        self.mainloop()
        # FIN 1


if __name__ == "__main__":
    CrearGrafo_matriz1()

    if len(datosTipoGrafo[0]) > 0:
        print(datosTipoGrafo)

