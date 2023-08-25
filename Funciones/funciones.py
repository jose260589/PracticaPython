numeros = [4,7,7,42,15,1-1]
"""
#encontrar numero alto y minimo
numero_maximo = max(numeros)
numero_minimo = min(numeros)

print(f"el numero maximo es {numero_maximo} y el numero minimo es {numero_minimo}")
"""
"""
#usando la funcion round a decimales, si se deja round(numero) va a redonder sin decimales, 
#para usar decimales tienes que colocarlo asi round(numero,cantidad decimales)
numero = round(12.55678)
print(numero)
"""

#retorna False -> 0, vacio, False, None \ True, cadena,lista,etc, datos no vacios
#retorna false si no devuelve nada, y true si tiene algo, puede validar variables
#bool and all se pueden usar para validar los datos de una base de datos.
valor = 0
resultado_bool = bool(valor)
print(resultado_bool)

#este es lo mismoa que bool pero este puede revisar mas de un elemento
resultado_all = all([valor,1,"true",[344,23]])
print(resultado_all)

#funcion sum, para sumar
suma_total = sum(numeros)
print(suma_total)