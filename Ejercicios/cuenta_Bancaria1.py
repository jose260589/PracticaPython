
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        # Completa este método
        if monto > 0:
            self.saldo += monto



cuenta = CuentaBancaria("Carlos", 1000)

cuenta.depositar(500)
print(cuenta.saldo)  # Esperado: 1500

cuenta.depositar(-200)
print(cuenta.saldo)  # Esperado: 1500