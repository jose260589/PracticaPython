"""
FIbonacci
0 1 1
"""
# se puede asignar variables juntas, ejemplo
# x,y = 0 , 1, si son mas, x, y, z = 0 , 1, 2
x=0
y=1

while y<=1597:
    print(x, end=" ")
    print(y, end=" ")
    x+=y
    y+=x
print("\n Fin.")
    
"""
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 

x=987
y=1597
"""
