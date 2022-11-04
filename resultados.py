from tkinter import *
from tkinter import ttk

root = Tk()


def resultados(b):
    frm = ttk.Frame(root, padding=50)
    frm.grid()
    ttk.Label(frm, text="Resultados").grid(column=0, row=0)
    ttk.Label(frm, text=f'y = {round(b[0], 4)} X + ({round(b[1], 4)})').grid(column=0, row=2)
    ttk.Button(frm, text="Salir", command=root.destroy).grid(column=1, row=5)
