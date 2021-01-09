from tkinter import *

win = Frame()
win.grid(sticky=N+S+E+W)

def validarEntero(widgetId):
    print(f"text={entry.get()}, valid={entry.get().isdigit()}, id={widgetId}")
    return entry.get().isdigit()

okayCommand = win.register(validarEntero)
entry = Entry(win, validate="focusout", validatecommand=(okayCommand, "%W"))
entry.grid(row=0, column=0)
btn = Button(text="Send")
btn["command"] = lambda: print(entry.get())
btn.grid(row=0, column=1)

win.mainloop()
