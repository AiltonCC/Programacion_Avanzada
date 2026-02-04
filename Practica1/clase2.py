"""x = 4
pi = 3.1416
str = 'Valor 1 {1:010.5}, valor 2 {0}'
print(str.format(x,pi))

edad = int(input('proporcione edad'))
print(f'Tu edad es {edad**2}')  #La f significa format y se ahorra lo demas

l1 = [1,2,3]
l2 = l1
print(l1 is l2)
print(2 in l1)


edad = int(input('Dame tu edad: '))
if edad < 18:
    print('ZI')
elif edad >= 18 and edad<30:
    print('Chambea')
else:
    print('Gracias')


y = 7
for x in range(1,11):
    if x != 6 and x!= 10:
        print(f'{y} x {x} = {y*x}')

y = 7
cont = 1
while cont <= 10:
    print(f'{y} x {cont} = {y*cont}')
    cont += 1

while cont < 100:
    pass
"""
#funciones

def tablas(n: int):
    """Genera la tabla hasta el diez de n

    Args:
        n (int): La tabla que se desea
    """
    for x in range(1,11):
        print(f'{n} x {x} = {n*x}')

numero = int(input('Numero de la tabla: '))
tablas(numero)

def multiplicacion(a:int = 0,b:int = 0) -> int:
    """Multiplca dos numeros

    Args:
        a (int, optional): _description_. Defaults to 0.
        b (int, optional): _description_. Defaults to 0.

    Returns:
        int: La multiplicacion de a * b 
    """
    return a * b

def mult_mul(*numeros):
    mul = 1
    for i in numeros:
        mul = mul*i
    return mul
print(mult_mul(1,2,3,4,5))

mul_lambda = lambda a,b: a*b
print(mul_lambda(5,5))