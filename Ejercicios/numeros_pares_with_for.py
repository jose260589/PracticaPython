# Generar un código que imprima los números pares del 10 al 50 utilizando un bucle for.
count_even = 0

for numero in range(10, 51):
    if numero % 2 == 0:
        count_even += 1
        
print(f"count_even = {count_even}")