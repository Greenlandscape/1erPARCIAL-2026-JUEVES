'''
## Ejercicio 5: El Inventario del Kwik-E-Mart

Definir una clase `ProductoKwikE` que represente un artículo en venta en el Kwik-E-Mart. Contiene los datos:
*   `descripcion`: 'string'
*   `id_producto`: 'integer'
*   `fecha_vencimiento`: `date` (importar `datetime`)
*   `precio`: 'float'
*   `stock`: 'integer'

La clase debe contener métodos para facilitar:
*   Cambiar uno o varios datos del producto (descripción, precio, stock).
*   Calcular en cuántos días expira un producto. Si el método detecta que el producto ha expirado, 
deberá informar al usuario y marcar el stock como 0.

**Importante:** Pueden agregar más atributos y métodos si lo consideran necesario (ej: `categoria`).
'''
from datatime import date

class ProductoKwikE:
        
    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock

    def cambiar_dato(self, tipo, nuevo_dato):
                
        if tipo == 'descripcion':
            self.descripcion = nuevo_dato
        elif tipo == 'id_producto':
            self.id_producto = nuevo_dato
        elif tipo == 'fecha_vencimiento':
            self.fecha_vencimiento = nuevo_dato
        elif tipo == 'precio':
            self.precio = nuevo_dato
        elif tipo == 'stock':
            self.stock = nuevo_dato
        else:
            print(f'No existe es tipo. Ingresó: {tipo}')
    
    def calcular_vencimiento(self):
        hoy = date.today()

        restan = (self.fecha_vencimiento - hoy).days
        # devuelva un número entero de días

        if restan < 0:
            print(f"El producto {self.id_producto} ya expiró.")
            self.stock = 0
            # se asigna agotado
        else:
            print(f"Faltan {restan} días para el vencimiento.")
        
        return restan

