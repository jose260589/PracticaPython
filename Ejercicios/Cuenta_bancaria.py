class CuentaBancaria:
    
    def __init__(self, num_cuenta, nombre_titular, balance):
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance
        
    def generar_balance(self):
        print(self.balance)
        
    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
    
    def retirar(self,monto):
        if monto <= self.balance:
            self.balance -= monto
            
mi_cuenta = CuentaBancaria("456123","JoseInoa",100000)

mi_cuenta.generar_balance()
mi_cuenta.depositar(5000)
mi_cuenta.generar_balance()
mi_cuenta.retirar(4000)
mi_cuenta.generar_balance()