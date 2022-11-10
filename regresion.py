import math
import numpy as np
import matplotlib.pyplot as plt
from error import resultados
from expo import get_pearson_correlation_coefficient

def estimate_coef(x, y, tamaño):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x

    # Sr
    sr=0
    for i in range(tamaño):
        sr += (y[i]-b_0 - b_1*x[i])**2

    # St
    st=0
    for i in range(len(y)):
        st += (y[i] - m_y)**2

    #Syx
    syx = math.sqrt(sr/(n-2))

    return (b_0, b_1,sr,st,syx)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)
    plt.title("Regresión lineal - método de mínimos cuadrados")

    # predicted response vector
    y_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, y_pred, 'r-',
             label=f'y = {round(b[0], 4)} + ({round(b[1], 4)}) X')
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    r=get_pearson_correlation_coefficient(x,y)
    resultados(r,b[2],b[3],b[4])
    # function to show plot
    plt.show()


def main(x, y, tamaño):
    # estimating coefficients
    b = estimate_coef(x, y, tamaño)
    # print("Estimated coefficients:\nb_0 = {}  \
    #       \nb_1 = {}".format(b[0], b[1]))

    # plotting regression line
    plot_regression_line(x, y, b)


if __name__ == "__main__":
    main()
