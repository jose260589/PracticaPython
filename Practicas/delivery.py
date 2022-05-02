print("\n ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\n"
                      "           Tipo de panes         "
                    "\n ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─\n"
                      "- 1. Amasado: $1.500.             \n"
                      "- 2. Ciabatta: $1.950.           \n"
                      "- 3. Dobladitas: $2.100.   \n"
                      "- 4. Frica: $1.800.       \n")
print("Ingrese cantidad de productos a comprar: ")
cant_ama=int(input("PAN AMASADO:\n"))
cant_ciab=int(input("PAN CIABATTA:\n"))
cant_dob=int(input("PAN DOBLADITAS:\n"))
cant_frica=int(input("PAN FRICA:\n"))

ama=1500
ciab=1950
dob=2100
frica=1800
total_global=0
descuento=0

if cant_ama>0:
    total_global=(ama*cant_ama)+total_global

if cant_ciab>0:
    total_global=(ciab*cant_ciab)+total_global

if cant_dob>0:
    total_global=(dob*cant_dob)+total_global

if cant_frica>0:
    total_global=(frica*cant_frica)+total_global

if total_global<=5000:
    descuento=total_global*0.10
    print("Total Factura es: ",total_global,"\n",
    "Costo de envio: ",descuento,"\n",
      "Total a Pagar es: ",total_global+descuento,"\n")
else:
    print("Total Factura es: ",total_global,"\n",
    "Costo de envio: Gratis \n",
    "Total a Pagar es: ",total_global,"\n"
    )