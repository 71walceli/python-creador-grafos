
# Copiado de https://stackoverflow.com/a/40021793

import tkinter

logWindowExists = False

class LogWindow():
    def __init__(self, parent):
        global logWindowExists, root
        logWindowExists = True

        self.parent = parent
        self.frame = tkinter.Frame(self.parent)

    def on_closing(self):
        global logWindowExists
        logWindowExists = False
        self.parent.destroy()


class MainWindow(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent

        frame = tkinter.Frame(self, borderwidth=1)
        frame.pack(fill=tkinter.BOTH, expand=True, padx=5, pady=5)

        self.LogButton = tkinter.Button(frame, text="Log Viewer", command= self.openLogWindow)
        self.LogButton.grid(sticky=tkinter.E+tkinter.W)

        self.pack(fill=tkinter.BOTH,expand=True)

    def openLogWindow(self):
        #if not logWindowExists:
        #    self.logWindow = tkinter.Toplevel(self.parent)
        #    self.app = LogWindow(self.logWindow)
        #else:
        #    self.logWindow.deiconify()
        self.logWindow = tkinter.Toplevel(self.parent)
        self.logWindow.transient(self.parent)
        self.app = LogWindow(self.logWindow)
        self.logWindow.protocol("WM_DELETE_WINDOW", self.app.on_closing)

def main():
    global app, stopRead, root
    root = tkinter.Tk()
    root.geometry("300x300")
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
