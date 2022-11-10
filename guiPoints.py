from tkinter import *
from rootCreation import root

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from regresion import main, plot_regression_line
from expo import get_exp_reg

matplotlib.use('TkAgg')

points = []
values = []

pointsFrame = Frame(root, width=500, height=500)
errorLabel = Label(pointsFrame, text="Error! Revise los campos", bg="yellow", font=(
    "Helvetica", 15))

funcBox = Entry(pointsFrame, font=("Helvetica", 15))
valueBox = Entry(pointsFrame, font=("Helvetica", 15))
grado = Entry(pointsFrame, font=("Helvetica", 15))


def calculate(e=None):
    try:
        for point in points:
            values.append((float(point[0].get()), float(point[1].get())))
        errorLabel.destroy()

        xi = np.array([])
        fi = np.array([])
        for point in values:
            xi = np.append(xi, point[0])
        for point in values:
            fi = np.append(fi, point[1])

        main(xi, fi, len(points))
        get_exp_reg(xi,fi)

    except:
        errorLabel.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


def createPointsFrame(numberOfPoints):
    pointsFrame.grid(row=0, column=0, padx=15, pady=15)
    pointsFrame.config(width=500, height=500)

    Label(pointsFrame, text="Metodos númericos", font=("Helvetica", 25)).grid(
        row=0, column=0, columnspan=2, padx=0, pady=5)

    Label(pointsFrame, text="", font=(
        "Helvetica", 15)).grid(row=5, column=0, padx=5, pady=5)

    for i in range(numberOfPoints):
        Label(pointsFrame, text="x:", font=(
            "Helvetica", 15)).grid(row=i+6, column=0, padx=5, pady=5)
        x = Entry(pointsFrame, font=("Helvetica", 15))
        x.grid(row=i+6, column=1, padx=5, pady=5)

        Label(pointsFrame, text="y:", font=(
            "Helvetica", 15)).grid(row=i+6, column=2, padx=5, pady=5)
        y = Entry(pointsFrame, font=("Helvetica", 15))
        y.grid(row=i+6, column=3, padx=5, pady=5)

        points.append((x, y))
    
    root.bind("<Return>", calculate)

    Button(pointsFrame, text="Calcular", font=(
        "Helvetica", 15), bg="LightSkyBlue1", command=calculate).grid(row=numberOfPoints + 8, column=2, columnspan=2, padx=5, pady=5)
