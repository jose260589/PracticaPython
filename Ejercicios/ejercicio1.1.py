"""
a) Diferencia en porcentaje entre el curso actual y:
-el mas rapido de otros cursos
-el mas lento de otros cursos
-el promedio de los cursos

b) porcentaje de material inservible que se reduce en:

-el promedio de los cursos
-el curso actual(este curso)

c) ver 10 horas de este curso a cuantas de otros cursos equivale ? y al reves?
"""

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#Diferencia de duracion

diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

print("-------------------")
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento")
print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio")

#b) crudo
crudo_promedio = 5
crudo_dalto = 3.5

tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10
print("-------------------")
print(f" Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f" este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")
print("-------------------")

#c) mostrando diferencia si los cursos duraran 10 horas
print(f"ver 10 horas de este curso equivale a ver {otros_cursos_promedio *100 // dalto_curso / 10} horas de otros cursos")
print(f"ver 10 horas de otros curso equivale a ver {dalto_curso *100 // otros_cursos_promedio / 10} horas de este curso")