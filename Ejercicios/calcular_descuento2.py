def calcular_descuento(precio):
    """
    Calcula el precio final después de aplicar un descuento.

    :precio: Precio original del producto.
    :return: Precio final después del descuento.
    :descuento: Porcentaje de descuento a aplicar.
    :precio_final: guarda el precio final después de restar el descuento al preccio.
    """
    if precio >= 1000:
           descuento = precio * (15 / 100)
    else:
           descuento = precio * (5 / 100)
    
    precio_final = precio - descuento
    return precio_final

precio = float(input("Ingrese el precio del producto: "))
precio_final = calcular_descuento(precio)

print("Precio final:", precio_final)