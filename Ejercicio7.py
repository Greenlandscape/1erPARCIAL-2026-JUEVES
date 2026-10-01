'''
## Ejercicio 7: La Gestión del Kwik-E-Mart

Crear una clase `KwikEMart`, la cual estará representada (atributos internos) 
mediante varias listas de objetos del tipo `ProductoKwikE`. Cada lista corresponde a un 
pasillo o sección del mercado (ej: "Bebidas", "Snacks", "Conveniencia").

La clase debe contener métodos para facilitar:
*   Controlar el stock de productos (añadir un nuevo producto a un pasillo, remover un 
producto del inventario, actualizar stock).
*   Calcular cuántos productos expiran en las próximas 24 horas y removerlos 
del inventario (simulando que Apu los desecha).
'''

class KwikEMart:

    def __init__(self):
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []
        # dentro de estas lista van los objetos de los productos: 'ProductoKwikE'

    # Para mayor legibilidad creamos una fución que devuelva 
    # la lista atributo necesaria para trabajar con ella
    def dame_lista_seccion(self, seccion):
        if seccion == 'bebidas':
            return self.bebidas
        elif seccion == 'snacks':
            return self.snacks
        elif seccion == 'conveniencia':
            return self.conveniencia
        else:
            return None

    def agregar_prodducto(self, producto, seccion):
        lista_atributo = self.dame_lista_seccion(seccion)
        if lista_atributo:
            lista_atributo.append(producto)
        else:
            print(f"Esa sección no existe!. Ingresó: {seccion}")

    def remover_producto(self, producto, seccion):
        lista_atributo = self.dame_lista_seccion(seccion)
        # Debemos asegurarnos de que el producto está en la sección
        producto_remover = None
        for p in lista_atributo:
            if p.id_producto == producto.id_producto:
                producto_remover = p
                break # una vez que lo encontró ya podemos salir del bucle

        # Ahora intentamos removerlo
        if producto_remover:
            lista_atributo.remove(producto_remover)
        else:
            print(f"No se encontró el {producto.descripcion} en {seccion}.")

