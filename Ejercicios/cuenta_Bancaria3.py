class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
       
        if monto > 0:
            self.saldo += monto

    def retirar(self, monto):
       
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Monto inválido o saldo insuficiente.")

    def transferir(self, otra_cuenta, monto):
    
        if monto > 0 and monto <= self.saldo:
            self.retirar(monto)
            otra_cuenta.depositar(monto)
        else:
            print("Monto inválido o saldo insuficiente para la transferencia.")


#Ejemplo de ejecucion
carlos = CuentaBancaria("Carlos", 1500)
ana = CuentaBancaria("Ana", 500)

carlos.transferir(ana, 400)

print(carlos.saldo)  # Esperado: 1100
print(ana.saldo)     # Esperado: 900

carlos.transferir(ana, 2000)  # Monto inválido o saldo insuficiente para la transferencia.

print(carlos.saldo)  # Esperado: 1100, ya que no debe haber cambiado por transferencia inválida
print(ana.saldo)     # Esperado: 900, ya que no debe haber cambiado por transferencia inválida

ana.transferir(carlos, 200)  # Monto inválido o saldo insuficiente para la transferencia.

print(carlos.saldo)  # Esperado: 1300, ya que no debe haber cambiado por transferencia inválida
print(ana.saldo)     # Esperado: 700, ya que no debe haber cambiado por transferencia inválida