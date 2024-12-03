from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt


print('\033[31mPractica 4: Gradiente de presión\033[0m')
print('Bienvenido a este programa, aquí podrás realizar todos los calculos de la práctica 4')
print('Solo con ingresar los datos experimentales obtenidos al realizar la practica')
nombre = input("\n¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")
print('\nIngresa tus datos obtenidos en el laboratorio:')

valx = input('Ingresa los datos de la variable independiente "x" (la Altura en metros). Escribe los valores con un espacio entre cada uno\n')

x = np.array([float(valor) for valor in valx.split()]).reshape(-1, 1)

print('Ingresa los valores la variable dependiente "y", la Presión Manométrica en pascales')
 
valy = input ('Ingresa los valores la variable dependiente "y"(la Presión Manométrica en pascales). Escribe los con un espacio entre cada uno\n')
 
y = np.array([float(valor) for valor in valy.split()]) 

modelo=LinearRegression()
modelo.fit(x,y)

m=modelo.coef_[0]
b=modelo.intercept_

print('El modelo matemático lineal de tus datos experimentales es:')

if b>0:
    print("Pman[Pa] = %.6f[Pa/m]*h[m] + %.6f[Pa]"%(m,b))
else:
    print("Pman[Pa] = %.6f[Pa/m]*h[m] %.6f[Pa]"%(m,b))

px=np.mean(x)
py=np.mean(y)

print(f"El centroide de tu pendiente es {px, py}")

highlight1=[px, 0]
highlight2=[py, b]

max_x=x.max()
max_y = m * max_x + b

t=[max_x,0]
q=[max_y,b]

c=[0, px]
d=[b, py]

print("El significado del modelo matematico es el siguiente:")
print(f"El peso especifico es la pendiente: {m:.6f} en [Pa/m] ó [N/m^3]")

gravedad = float ( input ("Ingresa el valor de la gravedad con la que deseas realizar los calculos (en m/s^2): ") )
densidad = m / gravedad
print(f"La densidad del fluido es {densidad:.6f} [kg/m^3]")

volumen_especifico = 1 / densidad
print(f"El volumen especifico es {volumen_especifico:.6f} [m^3/kg]")

print('Para obtener el porcentaje de error experimental, aqui estan las densidades de algunas sustancias en [kg/m^3]:')
print('Gasolina = 740')
print('Alcohol etilico = 789')
print('Acetona = 791')
print('Aceite de motor = 900')
print('Aceite vegetal = 920')
print('Agua = 1000')
print('Glicerina = 1260')
print('Cloro = 1560')

densidadteorica = float ( input ("Ingresa el valor de la densidad teorica de tu fluido en [kg/m^3]: ") )

error_exactitud1 = abs(((densidad-densidadteorica)/densidadteorica) * 100)

print(f"El error de exactitud de la densidad de tu experimento es {error_exactitud1:.6f} %")


plt.figure(1)
plt.scatter(x,y, color='b', label="Datos experimentales")
plt.axhline(0, color='black', linewidth=1)  
plt.axvline(0, color='black', linewidth=1) 
plt.title("Gráfica de mediciones")
plt.xlabel("h[m]")
plt.ylabel("Pman[Pa]")
plt.legend()
plt.grid(True)
plt.savefig("Grafica de mediciones.png")

plt.figure(2)
plt.plot(c,d, color='b', label="Pendiente") 
plt.plot(t,q, color='b')
plt.scatter(highlight1, highlight2, color='c', label="Ordenada y Centroide", s=100, zorder=5)
plt.axhline(0, color='black', linewidth=1)  
plt.axvline(0, color='black', linewidth=1) 
plt.title("Gráfica de Peso Específico")
plt.xlabel("h[m]")
plt.ylabel("Pman[Pa]") 
plt.legend()
plt.grid(True)
plt.savefig("Gráfica de Peso Específico")

plt.show()
