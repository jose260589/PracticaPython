def calcular_descuento(precio):
    """
    Calcula el precio final después de aplicar un descuento.

    :precio: Precio original del producto.
    :return: Precio final después del descuento.
    """
    
    descuento = precio * (10 / 100)
    precio_final = precio - descuento
    return precio_final

precio = float(input("Ingrese el precio del producto: "))

print("El precio final después del descuento es:", calcular_descuento(precio))