'''
## Ejercicio 3: La Paciencia de Marge con los Niños (Recursivo)

Escribir una función recursiva que calcule cuántas veces Bart ha interrumpido a Marge. Recibe como parámetros dos números (naturales) `a` (interrupciones por hora) y `b` (horas de la tarde), y devuelve el total de interrupciones.
'''

def interrupciones_rec(interrupciones_hora, horas):
    if not horas:
        interrupciones = 0
    # es el caso base, cuando ya no quedan horas, no hay más interrupciones
    else:
        interrupciones = interrupciones_hora + interrupciones_rec(interrupciones_hora, horas - 1)
    # llamada recursiva, se suman las interrupciones que se dan en una hora y se 
    # resta la hora calculada al hacer la llamada

    return interrupciones

    