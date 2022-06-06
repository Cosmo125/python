import numpy as np
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol
from sympy import diff

def dim(nombre):
    n=0
    with  open(nombre,"r") as datos:
        for i in datos:
            n+=1
    return n
def f1(x):
    return - 482.901439 + 645.385520*(x) - 349.945506*(x**2) + 99.616569*(x**3) - 15.750822*(x**4) + 1.313687*(x**5) - 0.045210*(x**6)
def f2(x):
    return 843.836399*(x**0) - 963.109750*(x**1) + 410.965677*(x**2) - 77.342101*(x**3) + 5.416562*(x**4)
nombre="Data_UTP_P1.csv"
n=dim(nombre)

x=[0 for i in range(n)]
y=[0 for i in range(n)]

with  open(nombre,"r") as datos:
    i=0
    for linea in datos:
        linea=linea.strip()
        lista=linea.split(",")
        x[i]=(float(lista[0])-9.02)*1000
        y[i]=(float(lista[1])-79.53)*1000
        i+=1
y1 = [0 for i in range(n)]
y2 = [0 for i in range(n)]
#print(y)
for i in range(n) :
    if i<=70 :
        y1[i] = f1(x[i])
    if i>70 :
        y2[i] = f2(x[i])
#print(y1)
#print(y2)
plt.xlim(3, 6.6)
plt.ylim(0, 5)
plt.plot(x,y,x,y1,x,y2)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('grafica')
plt.show()
