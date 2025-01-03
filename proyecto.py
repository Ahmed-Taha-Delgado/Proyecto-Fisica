from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

print('\033[31mPractica 4: Gradiente de presión\033[0m')
print('Bienvenido a este programa, aquí podrás realizar todos los calculos de la práctica 4')
print('Solo con ingresar los datos experimentales obtenidos al realizar la practica')

n = int(input("¿De cuántas personas es tu brigada? (elige entre 4 y 6): "))
while n < 4 or n > 6:
    print("El numero debe estar entre 4 y 6.")
    n = int(input("¿De cuántas personas es tu brigada? (elige entre 4 y 6): "))

print("\nIngresa las alturas utilizadas en el experimento (en metros).")
print("Escribe todas las alturas separadas por un espacio:")
valx = list(map(float, input("Alturas: ").split()))
x = np.array(valx).reshape(-1, 1)

datos_presiones = []
for persona in range(1, n + 1):
    print(f"\n--- Datos para la Persona {persona} ---")
    presiones = []
    for i in range(len(valx)):
        presion = float(input(f"Ingresa la presión correspondiente a la altura {valx[i]} m (en Pa): "))
        presiones.append(presion)
    datos_presiones.append(presiones)

headers = ["Altura [m]"] + [f"Persona {i+1}" for i in range(n)]
tabla = [[valx[i]] + [datos_presiones[j][i] for j in range(n)] for i in range(len(valx))]

print("\n\033[34mTabla de datos experimentales:\033[0m")
print(tabulate(tabla, headers=headers, floatfmt=".2f", tablefmt="grid"))

y = np.mean(datos_presiones, axis=0)

modelo=LinearRegression()
modelo.fit(x,y)

m=modelo.coef_[0]
b=modelo.intercept_

print('\nEl modelo matemático lineal de tus datos experimentales es:')

if b>0:
    print("Pman[Pa] = %.6f[Pa/m]*h[m] + %.6f[Pa]\n"%(m,b))
else:
    print("Pman[Pa] = %.6f[Pa/m]*h[m] %.6f[Pa]\n"%(m,b))

px=np.mean(x)
py=np.mean(y)

print(f"El centroide de tu pendiente es {px, py}\n")

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
print('La ordenada al origen del modelo significa el error experimental')

gravedad = float ( input ("\nIngresa el valor de la gravedad con la que deseas realizar los calculos (en m/s^2): ") )
densidad = m / gravedad
print(f"\nLa densidad del fluido es {densidad:.6f} [kg/m^3]")

volumen_especifico = 1 / densidad
print(f"El volumen especifico es {volumen_especifico:.6f} [m^3/kg]")

print('\nPara obtener el porcentaje de error experimental, aqui estan las densidades de algunas sustancias en [kg/m^3]:')
print('Gasolina = 740')
print('Alcohol etilico = 789')
print('Acetona = 791')
print('Aceite de motor = 900')
print('Aceite vegetal = 920')
print('Agua = 1000')
print('Glicerina = 1260')
print('Cloro = 1560')

densidadteorica = float ( input ("\nIngresa el valor de la densidad teorica de tu fluido en [kg/m^3]: ") )

error_exactitud1 = abs(((densidad-densidadteorica)/densidadteorica) * 100)

print(f"\nEl error de exactitud de la densidad de tu experimento es {error_exactitud1:.6f} %")

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
