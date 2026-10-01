'''
## Ejercicio 8: La Gestión del Kwik-E-Mart

8.1 Se deberán implementar la listas utilizadas en las clases definidad 
anteriormente utilizando Listas Enlazadas. Encontraran el prototipo en su 
archivo correspondiente.

8.2 Implementar Iteradores para las listas enlazadas.
'''

class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

class Iterador:
    def __init__(self, primer_nodo):
        self.actual = primer_nodo
    
    def __iter__(self):
        return self

    def __next__(self):
        if not self.actual:
            raise StopIteration
        dato = self.actual._elem # el elemento iterado
        self.actual = self.actual._nxt # el elemento siguiente
        return dato

class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)
    
    def append(self, dato):
        nuevo_nodo = Nodo(dato)
        actual = self.header

        while actual._nxt: # nos movemos a partir del primer nodo real
            actual = actual._nxt # actualiza el nodo
        actual._next = nuevo_nodo # aquí agrego el nuevo nodo al final de la lista
    
    def remove(self, dato):
        actual = self.header
        while actual._next:
            if actual._nxt._elen == dato:
                actual._nxt = actual._nxt._nxt # se "mueve" el puntero al siguiente nodo, desenlazando al que eliminamos
                return
            actual = actual._nxt
    def __iter_(self):
        # necesario para iterar
        return Iterador(self.header._nxt)
