def filtrar_usuarios(usuarios):
    # Filtrar usuarios activos
    usuarios_activos = [usuario for usuario in usuarios if usuario["activo"]]
    print("Usuarios activos:")
    for usuario in usuarios_activos:
        print(usuario)

    # Filtrar usuarios con compras mayores a 1000
    usuarios_compras_altas = [usuario for usuario in usuarios if usuario["compras"] > 1000]
    print("\nUsuarios con compras mayores a 1000:")
    for usuario in usuarios_compras_altas:
        print(usuario)

    return usuarios_activos,  usuarios_compras_altas




usuarios = [
    {"nombre": "Ana", "edad": 25, "activo": True, "compras": 1200},
    {"nombre": "Luis", "edad": 34, "activo": False, "compras": 800},
    {"nombre": "Pedro", "edad": 19, "activo": True, "compras": 2500},
    {"nombre": "Maria", "edad": 42, "activo": True, "compras": 450},
    {"nombre": "Carlos", "edad": 31, "activo": False, "compras": 1800},
    {"nombre": "Laura", "edad": 28, "activo": True, "compras": 3200}
]

resultados = filtrar_usuarios(usuarios)

print(f"\nCantidad de usuarios activos: {len(resultados[0])}")
print(f"Cantidad de usuarios con compras altas: {len(resultados[1])}")

