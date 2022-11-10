from tkinter import *


def resultados(r,sr,st,syx):
    root = Tk(screenName='Resultados')
    resultados = Frame(root, width=480,height=320)
    resultados.grid()
    Label(resultados, text=f'Valores importantes', font=("Helvetica", 15)).grid(
    row=1, column=0, padx=0, pady=5)
    Label(resultados, text=f'Coeficiente de correlación r: {round(r,4)} ', font=("Helvetica", 15)).grid(
    row=2, column=0, padx=0, pady=5)
    Label(resultados, text=f'St: {round(st,4)} ', font=("Helvetica", 15)).grid(
    row=3, column=0, padx=0, pady=5)
    Label(resultados, text=f'Sr: {round(sr,4)} ', font=("Helvetica", 15)).grid(
    row=4, column=0, padx=0, pady=5)
    Label(resultados, text=f'S(y/x): {round(syx,4)} ', font=("Helvetica", 15)).grid(
    row=5, column=0, padx=0, pady=5)