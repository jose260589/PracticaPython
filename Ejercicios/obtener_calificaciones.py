def obtener_calificaciones(nota):
    """
    Solicita al usuario que ingrese las calificaciones de los estudiantes y devuelve una lista con las calificaciones ingresadas.

    :return: Lista de calificaciones ingresadas por el usuario.
    notas: el valor debe estar entre 0 y 100.
    """
    if nota < 0 or nota > 100:
        raise ValueError("Nota inváliday 100.")
    elif nota >= 90:
        calificaciones = "A"
    elif nota >= 80:
        calificaciones = "B"
    elif nota >= 70:
        calificaciones = "C"
    elif nota >= 60:
        calificaciones = "D"
    else:
        calificaciones = "F"

    return calificaciones

calificacion = float(input("Ingrese la calificación del estudiante (0-100): "))

print("Calificación: ",obtener_calificaciones(calificacion))