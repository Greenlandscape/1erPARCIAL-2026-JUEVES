'''
## Ejercicio 2: La Eficiencia de Homer en la Barbacoa (Iterativo)

Escribir una función iterativa que calcule la cantidad total de donas consumidas en una fiesta. Recibe como parámetros dos números (naturales) `a` (donas por persona) y `b` (cantidad de personas), y devuelve el total de donas consumidas.
'''

def donas_consumidas(a,b):
    consumidas = 0
    for i in range (b):
        consumidas += a
    return consumidas

 # se recorre el bucle a partir de la cantidad de personas 
 # y se va sumando lo que consume cada una en un contador   