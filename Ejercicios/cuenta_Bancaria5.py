class CuentaBancaria:
    def __init__(self, titular, saldo):

        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")


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
cuenta1 = CuentaBancaria("Carlos", 1500)
print("Saldo inicial de la cuenta de Carlos:", cuenta1.consultar_saldo())
cuenta2 = CuentaBancaria("Ana", -500)
print("Saldo inicial de la cuenta de Ana:", cuenta2.consultar_saldo())
