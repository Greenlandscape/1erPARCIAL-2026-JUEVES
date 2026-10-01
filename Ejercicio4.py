'''
## Ejercicio 4: La Organización de Springfield (Condicional)

Escribir una función que reciba dos parámetros:
(i) una lista desordenada de "eventos" (ej: "Kermés", "Concurso de Comida", "Reunión del Concejo Municipal"); y
(ii) una expresión booleana (que puede ser evaluada a `True` o `False`).

Si el valor de la expresión es `True`, la lista de eventos se ordenará alfabéticamente en orden descendente (de la Z a la A). En caso contrario, 
se ordenará de forma ascendente (de la A a la Z). Por defecto, si la función es llamada sin una "expresión" (solo la lista de eventos), 
la lista debe retornar ordenada de forma ascendente.

'''

def ordenar_lista(lista, descendente = False):
    if descendente:
        lista_ordenada = sorted(lista, reverse = True)
        # orden descendente (de la Z a la A)
    else:
        lista_ordenada = sorted(lista)
        # orden ascendente (de la A a la Z)
    
    return lista_ordenada
    


