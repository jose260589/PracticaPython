"""
1.0 contar los usuarios activos.
2.0 contar las compras de los usuarios activos.
3.0 contar todos los usuarios mayores a 30 años.
4.0 identificar el usuario con la mayor cantidad de compras.
    debe estar activo, identicar nombre y cantidad de compras.
5.0 promedio de compras de los usuarios activos.
"""

def analisis_usuarios(usuarios_list):
    cantidad_activos = 0
    suma_compras = 0
    cantidad_mayores = 0  #usuarios mayores a 30 años
    mayor_compra = 0
    nombre_usuario = ""
    promedio = 0

    for usuario in usuarios_list:
        if usuario["activo"]:
            cantidad_activos += 1
            suma_compras += usuario["compras"]
            if usuario["compras"] > mayor_compra:
                mayor_compra = usuario["compras"]
                nombre_usuario = usuario["nombre"]
        if usuario["edad"] > 30:
            cantidad_mayores += 1

    if cantidad_activos > 0:
        promedio = suma_compras / cantidad_activos
    else:
        print("No hay usuarios activos para calcular el promedio de compras.")

    return {
            "usuarios_activos": cantidad_activos,
            "total_compras": suma_compras,
            "usuarios_mayores_30": cantidad_mayores,
            "usuario_mayor_compra": nombre_usuario,
            "mayor_compra": mayor_compra,
            "promedio_compras": promedio
    }

#user list
usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True, "compras": 1200},
    {"nombre": "Luis", "edad": 34, "activo": False, "compras": 800},
    {"nombre": "Pedro", "edad": 19, "activo": True, "compras": 2500},
    {"nombre": "Maria", "edad": 42, "activo": True, "compras": 450},
    {"nombre": "Carlos", "edad": 31, "activo": False, "compras": 1800},
    {"nombre": "Laura", "edad": 28, "activo": True, "compras": 3200}
]

resultados = analisis_usuarios(usuarios)

print("Cantidad de usuarios activos:", resultados["usuarios_activos"])
print("Total de compras:", resultados["total_compras"])
print("Usuarios mayores a 30 años:", resultados["usuarios_mayores_30"])
print(f"Usuario con mayor compra: {resultados['usuario_mayor_compra']} (Cantidad: {resultados['mayor_compra']})")
print("Promedio de compras:", resultados["promedio_compras"])