from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

print('\033[31mPractica 4: Gradiente de presión\033[0m')
print('Bienvenido a este programa, aquí podrás realizar todos los calculos de la práctica 4')
print('Solo con ingresar los datos experimentales obtenidos al realizar la practica')
nombre = input("\n¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")
print('\nIngresa tus datos obtenidos en el laboratorio:')
print('Ingresa los datos de la variable independiente "x", la Altura en metros')

valx = input("Ingresa los valores con un espacio entre cada uno\n")

x = np.array([float(valor) for valor in valx.split()]).reshape(-1, 1)

print('Ingresa los valores la variable dependiente "y", la Presión Manométrica en pascales')
 
valy = input ("Ingresa los valores con un espacio entre cada uno\n")
 
y = np.array([float(valor) for valor in valy.split()]) 

modelo=LinearRegression()
modelo.fit(x,y)

m=modelo.coef_[0]
b=modelo.intercept_

if b>0:
    print("Pman[Pa] = %.6f[Pa/m]*h[m] + %.6f[Pa]"%(m,b))
else:
    print("Pman[Pa] = %.6f[Pa/m]*h[m] %.6f[Pa]"%(m,b))

px=np.mean(x)
py=np.mean(y)

print(f"El centroide de tu pendiente es {px, py}")

highlight=[px, 0]
highlight=[py, b]


c=[0, px]
d=[b, py]

plt.figure(1)
plt.scatter(x,y, color='b')
plt.title("Gráfica de mediciones")
plt.xlabel("h[m]")
plt.ylabel("Pman[Pa]")
plt.legend()
plt.savefig("Grafica de mediciones.png")

plt.figure(2)
plt.plot(c,d, color='b')
plt.title("Gráfica de Peso Específico")
plt.xlabel("h[m]")
plt.ylabel("Pman[Pa]")  
plt.legend()
plt.savefig("Gráfica de Peso Específico")

plt.show()