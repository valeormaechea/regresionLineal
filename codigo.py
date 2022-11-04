import numpy as np
import matplotlib.pyplot as plt 
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

#Inputs
x = np.array([1,2,3,4,5,6]) #periodo de entrenamiento
y = np.array([7000,  9000, 5000, 11000, 10000, 13000])
z = np.array([7, 8, 9, 10, 11, 12]) #Periodos que deseo pronosticar

plt.scatter(x,y,label='data', color='blue')
plt.title('Distribución entre meses y demanda');

regresion_lineal = linear_model.LinearRegression()
regresion_lineal.fit(x.reshape(-1,1), y) 
print('\nParámetros del modelo de regresión')
print('b (Pendiente) = ' + str(regresion_lineal.coef_) + ', a (Punto de corte) = ' + str(regresion_lineal.intercept_))

# vamos a predecir el periodo 7 (z = [7]
pronostico = regresion_lineal.predict(z.reshape(-1,1))

print('\nPronósticos')
for i in range(len(z)):
    print('Pronóstico para el periodo {0} = {1} '.format(z[i], pronostico[i]))

pronostico_entrenamiento = regresion_lineal.predict(x.reshape(-1,1))
mse = mean_squared_error(y_true = y, y_pred = pronostico_entrenamiento)
rmse = np.sqrt(mse)
print('\nEvaluación de calidad de la regresión')
print('Error Cuadrático Medio (MSE) = ' + str(mse))
print('Raíz del Error Cuadrático Medio (RMSE) = ' + str(rmse))

r2 = regresion_lineal.score(x.reshape(-1,1), y)
print('Coeficiente de Determinación R2 = ' + str(r2))

plt.plot(x,pronostico_entrenamiento,label='data', color='red')
plt.xlabel('Meses')
plt.ylabel('Demanda')
plt.show()