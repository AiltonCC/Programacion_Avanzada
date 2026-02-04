"""
Chavez Contreras Edgar Ailton Jave
2023640251
2MV4
"""
import math
import random
import os

def burbuja(li: list[int], b: int):
    """Metodo de burbuja

    Args:
        li (list[int]): Se ingresa la lista a ordenar
        b (int): El tamano de la lista
    """
    for i in range(0,b,1):
        for j in range(0,b,1):
            if li[i] <= li[j]:
                continue
            elif li[i] > li[j]:
                aux = li[i]
                li[i] = li[j]
                li[j] = aux

while 1:
    print('Mi programa\n1. Media Arimetica\n2. Desviacion Estandar\n3. Burbuja\n4. Salir')
    menu = int(input('Escriba la opcion que desea: '))
    
    if menu == 1:
        print('Media Arimetica\n')
        num = int(input('Numero de muestras: '))
        resultado=0
        for i in range(0,num,1):
            muestra = int(input(f"Muestra {i+1}: "))
            resultado += muestra
        print(f"Media = {resultado/num}")
    elif menu == 2:
        print('Desviacion Estandar\n')
        num = int(input('Numero de muestras: '))
        x1=x2=0
        for i in range(0,num,1):
            muestra = int(input(f"Muestra {i+1}: "))
            x1 += math.pow(muestra,2)              
            x2 += muestra
        desviacion = (x1-(math.pow(x2,2)/num))/(num-1)
        print(f"Desviacion Estandar = {math.sqrt(desviacion)}")
    elif menu == 3:
        print('Burbuja')
        num = int(input('Numero de muestras: '))
        lista = [random.randint(0,100)]             #Genera numeros aleatorios
        for i in range(0,num-1,1):
            lista.append(random.randint(0,100))     #Agrega numeros aleatorios
        burbuja(lista,num)
        print(lista)
    elif menu == 4:
        print('Vuelva pronto')
        exit(0)
    else:
        os.system('cls')
        
        
