"""
Chavez Contreras Edgar Ailton Jave
2023640251
2MV4
"""

import numpy as np

print('Solucion de Sistemas de Ecuaciones')
a = np.array([[0,0,0],[0,0,0],[0,0,0]])
b = np.array([0,0,0])

for fila in range(0,3,1):
    for colum in range(0,3,1):
        a[fila,colum] = int(input(f'A{fila+1}{colum+1}: '))
    b[fila] = int(input(f'B{fila+1}: '))

#Solucion del sistema de ecuaciones con funcion de la libreria NumPy
x = np.linalg.solve(a,b)
print(f'Solucion: x={x[0]:0.2f}, y={x[1]:0.2f}, z={x[2]:0.2f}')

#Solucion del sistema de ecuaciones sin solve()
ai = np.linalg.inv(a)   #Saca la metriz inversa
x1 = (ai @ b)           #Producto matricial dot()
print(f'Solucion: x={x1[0]:0.2f}, y={x1[1]:0.2f}, z={x1[2]:0.2f}')