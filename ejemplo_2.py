from tkinter import *

win = Frame()
win.grid(sticky=N+S+E+W)

frame_a = LabelFrame(win, text='Top frame', padx=5, pady=5)
frame_b = LabelFrame(win, text='Bottom frame', padx=5, pady=5)
frame_a.grid(sticky=E+W)
frame_b.grid(sticky=E+W)

for frame in frame_a, frame_b:
    for col in 0, 1, 2:
        frame.columnconfigure(col, weight=1)

Label(win, text='Hi').grid(in_=frame_a, sticky=W)
Label(win, text='Longer label, shorter box').grid(in_=frame_b, sticky=W)

entry = Entry(win)
entry.grid(in_=frame_a, row=0, column=1, sticky=W)
btn = Button(text="Send")
btn["command"] = lambda: print(entry.get())
btn.grid(in_=frame_b, row=0, column=1, sticky=W)

win.mainloop()
