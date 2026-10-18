"""
Tu función deberá obtener estos cinco resultados:
1. Cantidad de empleados activos.
2. Suma de los salarios de los empleados activos.
3. Cantidad de empleados activos del departamento "IT".
4. Nombre y salario del empleado activo con el salario más alto.
5. Promedio salarial de los empleados activos del departamento "IT".
"""

def analisis_empleados(empleados_list):
    cantidad_activos = 0
    suma_salarios = 0
    cantidad_it = 0
    mayor_salario = 0
    nombre_empleado = ""
    promedio_it = 0

    for empleado in empleados_list:
        if empleado["activo"]:
            cantidad_activos += 1
            suma_salarios += empleado["salario"]
            if empleado["departamento"] == "IT":
                cantidad_it += 1
                if empleado["salario"] > mayor_salario:
                    mayor_salario = empleado["salario"]
                    nombre_empleado = empleado["nombre"]

    if cantidad_it > 0:
        promedio_it = suma_salarios / cantidad_it
    else:
        print("No hay empleados activos en el departamento IT para calcular el promedio salarial.")

    return {
        "empleados_activos": cantidad_activos,
        "suma_salarios": suma_salarios,
        "empleados_activos_IT": cantidad_it,
        "empleado_mayor_salario": nombre_empleado,
        "mayor_salario": mayor_salario,
        "promedio_salarial_IT": promedio_it
    }



empleados = [
    {"nombre": "Ana", "salario": 45000, "departamento": "IT", "activo": True},
    {"nombre": "Luis", "salario": 52000, "departamento": "Ventas", "activo": True},
    {"nombre": "Pedro", "salario": 38000, "departamento": "IT", "activo": False},
    {"nombre": "Maria", "salario": 61000, "departamento": "IT", "activo": True},
    {"nombre": "Carlos", "salario": 47000, "departamento": "Ventas", "activo": True},
    {"nombre": "Laura", "salario": 58000, "departamento": "IT", "activo": False}
]

resultados = analisis_empleados(empleados)
print("Cantidad de empleados activos:", resultados["empleados_activos"])
print("Suma de los salarios de los empleados activos:", resultados["suma_salarios"])
print("Cantidad de empleados activos del departamento 'IT':", resultados["empleados_activos_IT"])
print("Empleado con el salario más alto:", resultados["empleado_mayor_salario"])
print("Mayor salario:", resultados["mayor_salario"])
print("Promedio salarial del departamento 'IT':", resultados["promedio_salarial_IT"])

