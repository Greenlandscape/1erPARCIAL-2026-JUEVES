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

    def actualizar_stock(self, producto, seccion, nuevo_stock):
        lista_atributo = self.dame_lista_seccion(seccion)

        if lista_atributo:
            for p in lista_atributo:
                if p.id_producto == producto.id_producto:
                    p.stock = nuevo_stock
                return # ya cumplió su función
            else:
                print(f"No se encotró el producto {producto.descripcion} en {seccion}")
    
    def procesar_vencidos(self):
        import datatime
        hoy = datatime.date.today()

        t_limite = hoy + datatime.timedelta(days=1) # las proximas 24h según el enunciado, o sea, se suma un día
        vencidos = 0
        secciones = [self.bebidas, self.snacks, self.conveniencia]
        # recorremos las secciones, luego los productos en cada seccion
        for seccion in secciones:
            productos_a_eliminar = []
            # recorremos toda la seccion buscando vencidos
            for p in seccion:
                if p.fecha_vencimiento <= t_limite:
                    vencidos += 1
                    productos_a_eliminar.append(p)
        
            # ahora eliminamos todos los productos vencidos de la seccion
            for vencido in productos_a_eliminar:
                seccion.remove(vencido)
        return vencidos
