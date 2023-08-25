"Intereses"

capital = float(input("Digita capital: "))
tasa = (float(input("Digita interes: "))/100)/365
dias = int(input("Digita cantidad dias: "))

Total= capital*tasa*dias


print(f"Total : {Total}")

