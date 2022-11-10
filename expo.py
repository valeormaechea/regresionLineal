"""
The get_exp_reg(x, y) function takes in two lists and will do exponential regression on them to return an exponential
function of the form y=ae^(bx) that can be used to make predictions for given x values.
"""

import math
import matplotlib.pyplot as plt
import numpy as np
from error import resultados
from tkinter import *


def get_pearson_correlation_coefficient(x, y):
    """
    Returns correlation coefficient of two lists x, y.
    r = sum((x - mean_x) * (y - mean_y)) / sqrt(sum((x - mean_x)^2) * sum((y - mean_y)^2))
    """
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    numerator = 0

    for i in range(len(x)):
        numerator += (x[i] - mean_x) * (y[i] - mean_y)

    # SXX
    sum_squares_x = 0

    for i in range(len(x)):
        sum_squares_x += (x[i] - mean_x)**2

    # SYY
    sum_squares_y = 0

    # St
    for i in range(len(y)):
        sum_squares_y += (y[i] - mean_y)**2

    
    denominator = (sum_squares_x * sum_squares_y)**.5

    return numerator / denominator


def get_sample_std_dev(x):
    """
    Returns sample std dev. x must have a length greater than 1 as the denominator will be length - 1.
    sample_std_dev = sqrt(sum(x - mean_x)^2 / length_x - 1)
    """
    mean_x = sum(x) / len(x)

    sum_squares_x = 0

    for num in x:
        sum_squares_x += (num - mean_x)**2

    return (sum_squares_x / (len(x) - 1))**.5


def get_exp_reg(x, y):
    """
    Exponential regression.
    x and y are lists. x and y must be longer than 1, as length - 1 will be used on denominator for sample std dev.
    Returns function of the form y=ae^(bx).
    To get this, the original formula is manipulated such that linear regression can be used, then it is converted back.
    y=ae^(bx)
    ln(y)=ln(ae^(bx))
    ln(y)=ln(a)+ln(e^(bx))
    ln(y)=ln(a)+bx
    Let z = ln(y). Let c = ln(a).
    z = c + bx
    Linear regression formula being used is:
    b = pearson_correlation_coefficient * sample_std_dev_z / sample_std_dev_x
    c = mean_z - b * mean_x
    """
    # z values = ln(y)
    z_data = []
    for num in y:
        z_data.append(math.log(num, math.e))

    r = get_pearson_correlation_coefficient(x, z_data)
    b = get_pearson_correlation_coefficient(
        x, z_data) * get_sample_std_dev(z_data) / get_sample_std_dev(x)

    mean_z = sum(z_data) / len(z_data)
    mean_x = sum(x) / len(x)

    c = mean_z - (b * mean_x)

    a = math.e**c

    # Sr
    sr=0
    for i in range(len(y)):
        sr += (y[i] - a - b*x[i])**2

    # St
    mean_y = sum(y) / len(y)
    st=0
    for i in range(len(y)):
        st += (y[i] - mean_y)**2

    #Syx
    syx = math.sqrt(sr/(len(z_data)-2))

    # Prints the formula.
    print(f'y={a}*e^({b}*x)')
    plot_regresion(x, y, a, b,r, sr,st,syx)
    # resultados(r)


def func(x, a, b):
    return a * np.exp(b * x)


def plot_regresion(x, y, a, b,r,sr,st,syx):

    y_bar = np.sum(y) / len(y)
    sst = 0.0
    for i in range(len(y)):
        sst += pow(y[i] - y_bar, 2)
    ss_reg = 0.0
    y_hat = func(x, a, b)
    for i in range(len(y_hat)):
        ss_reg += pow(y_hat[i] - y_bar, 2)
    d = ss_reg / sst

    plt.title(f"Regresión no lineal - Exponencial")
    new_x = np.linspace(0, max(x), 200)

    plt.plot(new_x, func(new_x, a, b), 'r-',
             label=f'y = {"{0:.4f}".format(a)}*e^{"{0:.4f}x".format(b)}')

    # plt.text(min(x), max(y)/2, f'Coeficiente de correlación r: {r}')
    plt.plot(x, y, 'o', color='m')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    resultados(r,sr,st,syx)
    # root = Tk()
    # resultados = Frame(root, width=480,height=320)
    # resultados.grid()
    # Label(resultados, text=f'Coeficiente de correlación r: {r} ', font=("Helvetica", 25)).grid(
    # row=2, column=0, padx=0, pady=5)

    plt.show()
