'''
## Ejercicio 6: La Etiqueta de los Productos del Kwik-E-Mart (Sobrecarga de Métodos)

Sobrecargar los siguientes métodos en la clase `ProductoKwikE`:
*   `__str__`: Para representar el producto de forma legible (ej: "Producto: Donuts Glaseadas | ID: 123 | Precio: $1.50 | Stock: 50").
*   `__eq__`: Para comparar si dos productos son iguales basándose en su `id_producto` y `descripcion`.
'''
# Copio el código del punto anterior para más claridad.
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

    def __str__(self):
        cadena = f"Producto: {str(self.descripcion)} | ID: {str(self.id_producto)} | Precio: {str(self.precio)} | Stock: {str(self.stock)}"
        return cadena

    def __eq__(self, producto_2):
        return (
            self.id_producto == producto_2.id_producto and 
            self.descripcion == producto_2.descripcion
        )

        # así evaluará las condiciones y devolverá True o False según corresponda
            
