
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        # Completa este método
        if monto > 0:
            self.saldo += monto

    def retirar(self, monto):
        # Completa este método
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Monto inválido o saldo insuficiente.")


#caso 1
cuenta = CuentaBancaria("Carlos", 1500)

cuenta.retirar(500)
print(cuenta.saldo)  # Esperado: 1000

#caso 2
cuenta = CuentaBancaria("Carlos", 1000)

cuenta.retirar(1200)  # Monto mayor al saldo
print(cuenta.saldo)  # Esperado: 1000

#caso 3
cuenta = CuentaBancaria("Carlos", 1000)

cuenta.retirar(-100)  # Monto negativo
print(cuenta.saldo)  # Esperado: 1000