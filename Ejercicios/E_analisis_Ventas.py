#Analisis de ventas.
def analizar_ventas(ventas):
    contador_ventas_altas = 0
    contador_valores_altos = 0
    total_ventas = sum(ventas)
    for venta in ventas:
        if venta >= 500:
            contador_ventas_altas += 1
            contador_valores_altos += venta

    return {
        "ventas_altas": contador_ventas_altas,
        "valores_altos": contador_valores_altos
    }

ventas = [120, 450, 800, 90, 600, 150]

resultados = analizar_ventas(ventas)
print("Ventas altas:", resultados["ventas_altas"]) 
print("Sumatoria de Ventas altas:", resultados["valores_altos"]) 