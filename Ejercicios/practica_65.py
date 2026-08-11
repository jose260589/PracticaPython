#Práctica 65: Análisis de salarios de empleados.
def analizar_salarios(empleados):
    contador_salarios_altos = 0
    contador_valores_altos = 0
    nombre_empleado = ""
    salario_mayor = 0
    
    for empleado in empleados:
        if empleado["salario"] >= 50000:
            contador_salarios_altos += 1
            contador_valores_altos += empleado["salario"]
        if empleado["salario"] > salario_mayor:
            nombre_empleado = empleado["nombre"]
            salario_mayor = empleado["salario"]

    return {
        "salarios_altos": contador_salarios_altos,
        "valores_altos": contador_valores_altos,
        "empleado_mayor_salario": nombre_empleado,
        "salario_mayor": salario_mayor
    }


empleados = [
    {"nombre": "Ana", "salario": 45000},
    {"nombre": "Luis", "salario": 52000},
    {"nombre": "Pedro", "salario": 38000},
    {"nombre": "Maria", "salario": 61000},
    {"nombre": "Carlos", "salario": 47000}
]

resultados = analizar_salarios(empleados)
print("Empleados con salario alto:", resultados["salarios_altos"])
print("Sumatoria de salarios altos:", resultados["valores_altos"])  
print("Empleado con mayor salario:", resultados["empleado_mayor_salario"])
print("Mayor salario:", resultados["salario_mayor"])