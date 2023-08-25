#Crea una función que dados dos números mostrará todos los números que hay entre ellos.

def mostrarnum(num1, num2):
    if(num1>num2):
        change=num1
        num1=num2
        num2=change
    
    for i in range(num1+1,num2):
        print(i)
        
def mostrarnum2(num1, num2):
        if(num1>num2):
            change=num1
            num1=num2
            num2=change
        
        contar = num1
        
        while contar < num2-1:
            contar+=1
            print(contar)

mostrarnum2(10,1)

