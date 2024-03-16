#Vamos a crear un programa para eliminar una palabra de una frase y que imprima la frase resultante, debe ser pedido desde el teclado..

oracion_original = input("Escribe la oracion a analizar: ")

Buscar_palabra = input("Digita la palabra a buscar: ")

Palabra_cambiar = input("Escribe la nueva palabra.(Nota: si dejas en blanco la palabra buscada se eliminara.): ")

nueva_oracion=oracion_original.replace(Buscar_palabra,Palabra_cambiar)
      
print(f"Oracion original: {oracion_original}")
print(f"Nueva oracion: {nueva_oracion}")