# TODO Documentar funciones de Tkinter

import tkinter as tk
from tkinter import ttk, messagebox

datosTipoGrafo = ["", False, False] #   Datos que `CrearGrado_matriz1` envía a la ventana para
                                    # definir la matriz.
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
        tipoGrafo_marco.grid(padx=10, pady=10, column=0, row=0, rowspan=2)

        # 1.1.1. CasillaVerificación("Dirigido")
        self.dirigido_valor               = tk.BooleanVar()
        dirigido_casillaVerificacion = ttk.Checkbutton(tipoGrafo_marco,
                                                       text="Dirigido",
                                                       variable=self.dirigido_valor)
        dirigido_casillaVerificacion.pack(padx=10, pady=10)

        # 1.1.2. CasillaVerificación("Ponderado")
        self.ponderado_valor = tk.BooleanVar()
        ponderado_casillaVerificacion = ttk.Checkbutton(tipoGrafo_marco,text="Ponderado",
                                                        variable=self.ponderado_valor)
        ponderado_casillaVerificacion.pack(padx=10, pady=10)

        # 1.2.  EntradaTexto(líneas=1,etiqueta="Vértices")
        vertices_marco      = ttk.Labelframe(self, text="Vértices")
        vertices_marco.grid(padx=10, pady=10, column=1, row=0)
        self.vertices_valor = tk.StringVar()
        vertices_entrada    = ttk.Entry(vertices_marco, textvariable=self.vertices_valor)
        vertices_entrada.pack(padx=10, pady=10)

        # 1.3.  Botón(texto="Generar matriz")
        generarMatriz_boton = ttk.Button(self, text="Generar matriz", command=self.validar)
        generarMatriz_boton.grid(padx=10, pady=10, column=1, row=1)

        #self.bind('<Return>', generarMatriz_boton.invoke)
        self.master.bind('<Return>', self.validar)
        #self.focus_set()
        self.mainloop()
        # FIN 1. Ventana(título="Crear grafo por matriz de adyacencia")


    def validar(self, event):
        # TODO Validar compo self.vertices_valor.get()
        global datosTipoGrafo
        nodos = self.vertices_valor.get().split()
        nodos = list(set(nodos))  # eliminarNodosDuplicados(nodos)

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
        self.master.unbind('<Return>')
        self.quit()
        self.update()
        self.destroy()


#class CasillaVerificacion(tk.Frame):
#    def __init__(self, *args, **kwargs):
#        super().__init__(**kwargs)
#        self.estado  = tk.BooleanVar()
#        self.casilla = ttk.Checkbutton(*args, variable=self.estado)
#        self.pack(padx=10, pady=10)


if __name__ == "__main__":
    CrearGrafo_matriz1()
    print(datosTipoGrafo)

