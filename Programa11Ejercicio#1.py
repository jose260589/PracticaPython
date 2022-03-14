"""preguntar por la clave del departamento, solo son 3
antiguedad
los clave 1 atencion al cliente
antiguedad
1 año 6 dias de vacaciones
2 a 6 años 14
7 años 20 dias

clave 2 logistica
antiguedad
1 año 7 dias
2 a 6 años 15
7 años 22 dias

clave 3 gerencia
antiguedad
1 año 10 dias
2 a 6 años 20
7 años 30 dias

nombre, clave y antiguedad
mensaje nombre, y dias que le corresponde
"""

print("Compañia Multinacional Rappi \n")

print("Programa para calcular Vaciones Empleados. \n")

nombre= input("Favor Digitar su nombre: ")
clave = int(input("Favor Digitar su clave de departamento: "))
antiguedad = int(input("Favor Digitar su antiguedad en la empresa: "))

if clave==1:
    print("\n Departamento 'Servicio al cliente'")
    if antiguedad==1:
        print("\n El Señor "+ nombre + " le tocan 6 dias de vacaciones ")
    elif antiguedad >=2 and antiguedad <=6:
        print("\n El Señor "+ nombre + " le tocan 14 dias de vacaciones ")
    else:
        print("\n El Señor "+ nombre + " le tocan 20 dias de vacaciones ")
elif clave==2:
    print("\n Departamento 'Logistica'")
    if antiguedad==1:
        print("\n El Señor "+ nombre + " le tocan 7 dias de vacaciones ")
    elif antiguedad >=2 and antiguedad <=6:
        print("\n El Señor "+ nombre + " le tocan 15 dias de vacaciones ")
    else:
        print("\n El Señor "+ nombre + " le tocan 22 dias de vacaciones ")
elif clave==3:
    print("\n Departamente de 'Gerencia'")
    if antiguedad==1:
        print("\n El Señor "+ nombre + " le tocan 10 dias de vacaciones ")
    elif antiguedad >=2 and antiguedad <=6:
        print("\n El Señor "+ nombre + " le tocan 20 dias de vacaciones ")
    else:
        print("\n El Señor "+ nombre + " le tocan 30 dias de vacaciones ")
else:
    print("\n Clave digitada no es correcta")

print("\n Fin.")
