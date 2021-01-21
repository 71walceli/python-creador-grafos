from tkinter import *
from tkinter import simpledialog, ttk


class Dialogo(simpledialog.Dialog):
    def __init__(self, parent, content: Frame, *args, **kwargs):
        self.content = content
        super().__init__(parent, *args, **kwargs)

    def body(self, master):
        internal = Frame(master)
        internal.pack()

        Label(internal, text="Diálogo "*5).pack()
        #self.content.destroy()
        #self.content.pack()
        #c = Canvas(self)
        #c.create_window(0, 0, window=self.content)
        #c["width"] = self.content.winfo_width()
        #c["height"] = self.content.winfo_height()
        #c.pack()

    def buttonbox(self):
        Button(self, text="Cerrar", command=self.destroy).pack()


t = Tk()
f = Frame()
f.pack()

c = Button(f, text="Abrir otro diálogo", command=lambda: Dialogo(t, f, title="Diálogo"))

b = Button(t, text="Abrir diálogo", command=lambda: Dialogo(t, f, title="Diálogo"))
b.pack()

t.mainloop()
