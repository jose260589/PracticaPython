class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto):
       
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
       
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
        else:
            print("Monto inválido o saldo insuficiente.")

    def transferir(self, otra_cuenta, monto):
    
        if monto > 0 and monto <= self.__saldo:
            self.retirar(monto)
            otra_cuenta.depositar(monto)
        else:
            print("Monto inválido o saldo insuficiente para la transferencia.")

    def consultar_saldo(self):
        return self.__saldo


#Ejemplo de ejecucion
carlos = CuentaBancaria("Carlos", 1500)

print(carlos.consultar_saldo())

carlos.depositar(500)
print(carlos.consultar_saldo())

carlos.retirar(300)
print(carlos.consultar_saldo())
